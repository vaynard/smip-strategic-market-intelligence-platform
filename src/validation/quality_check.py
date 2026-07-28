import pandas as pd


class DataQualityChecker:


    def __init__(self, df):

        self.df = df.copy()

        self.results = {}


    # -------------------------
    # Completeness Check
    # -------------------------

    def check_missing_values(self):

        missing = self.df.isnull().sum()

        missing_columns = (
            missing[missing > 0]
            .to_dict()
        )

        self.results["missing_values"] = {

            "status":
                "PASS"
                if len(missing_columns) == 0
                else "FAIL",

            "details":
                missing_columns

        }


    # -------------------------
    # Duplicate Check
    # -------------------------

    def check_duplicates(self):

        duplicates = self.df.duplicated(
            subset=[
                "country",
                "indicator_code",
                "year"
            ]
        ).sum()

        self.results["duplicates"] = {

            "status":
                "PASS"
                if duplicates == 0
                else "FAIL",

            "count":
                int(duplicates)

        }


    # -------------------------
    # Numeric Validation
    # -------------------------

    def check_numeric_values(self):

        valid = pd.api.types.is_numeric_dtype(
            self.df["value"]
        )

        self.results["numeric_validation"] = {

            "status":
                "PASS"
                if valid
                else "FAIL"

        }


    # -------------------------
    # Business Rule Validation
    # -------------------------

    def check_indicator_rules(self):

        errors = []

        for _, row in self.df.iterrows():

            indicator = row["indicator_name"]

            value = row["value"]

            rules = row["validation"]


            # ---------------------
            # Positive Only
            # ---------------------

            if rules.get(
                "positive_only",
                False
            ):

                if value <= 0:

                    errors.append({

                        "indicator":
                            indicator,

                        "value":
                            value,

                        "issue":
                            "Value must be positive"

                    })


            # ---------------------
            # Minimum Value
            # ---------------------

            if "min" in rules:

                if value < rules["min"]:

                    errors.append({

                        "indicator":
                            indicator,

                        "value":
                            value,

                        "issue":
                            f"Below minimum ({rules['min']})"

                    })


            # ---------------------
            # Maximum Value
            # ---------------------

            if "max" in rules:

                if value > rules["max"]:

                    errors.append({

                        "indicator":
                            indicator,

                        "value":
                            value,

                        "issue":
                            f"Above maximum ({rules['max']})"

                    })


        self.results["business_rules"] = {

            "status":
                "PASS"
                if len(errors) == 0
                else "FAIL",

            "errors":
                errors

        }


    # -------------------------
    # Source Validation
    # -------------------------

    def check_source(self):

        missing_source = (

            self.df["source"]

            .isnull()

            .sum()

        )

        self.results["source_validation"] = {

            "status":
                "PASS"
                if missing_source == 0
                else "FAIL",

            "missing_sources":
                int(missing_source)

        }


    # -------------------------
    # Confidence Score
    # -------------------------

    def calculate_confidence(self):

        checks = []

        for result in self.results.values():

            if "status" in result:

                checks.append(
                    result["status"] == "PASS"
                )

        score = (

            sum(checks)

            /

            len(checks)

            *

            100

        )

        self.results["confidence_score"] = round(
            score,
            2
        )


    # -------------------------
    # Run All Checks
    # -------------------------

    def run_all_checks(self):

        self.check_missing_values()

        self.check_duplicates()

        self.check_numeric_values()

        self.check_indicator_rules()

        self.check_source()

        self.calculate_confidence()

        return self.results