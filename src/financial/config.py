import yaml


class FinancialConfig:

    def __init__(

        self,

        config_path="config/financial.yaml"

    ):

        with open(

            config_path,

            "r",

            encoding="utf-8"

        ) as file:

            config = yaml.safe_load(file)


        # --------------------------------------------------
        # General
        # --------------------------------------------------

        self.currency = config["currency"]

        self.initial_investment = float(
            config["initial_investment"]
        )

        self.discount_rate = float(
            config["discount_rate"]
        )

        self.project_years = int(
            config["project_years"]
        )


        # --------------------------------------------------
        # Revenue
        # --------------------------------------------------

        self.base_revenue = float(
            config["base_revenue"]
        )

        self.base_growth_rate = float(
            config["base_growth_rate"]
        )


        self.market_multiplier = config[
            "market_multiplier"
        ]


        self.revenue_score_weights = config[
            "revenue_score_weights"
        ]


        self.growth_adjustment = config[
            "growth_adjustment"
        ]


        # --------------------------------------------------
        # Operating
        # --------------------------------------------------

        self.operating_margin = float(
            config["operating_margin"]
        )

        self.tax_rate = float(
            config["tax_rate"]
        )


        # --------------------------------------------------
        # Sensitivity Scenarios
        # --------------------------------------------------

        self.scenarios = config.get(
            "scenarios",
            []
        )


    # --------------------------------------------------
    # Dictionary
    # --------------------------------------------------

    def to_dict(self):

        return {

            "currency":
                self.currency,

            "initial_investment":
                self.initial_investment,

            "discount_rate":
                self.discount_rate,

            "project_years":
                self.project_years,

            "base_revenue":
                self.base_revenue,

            "base_growth_rate":
                self.base_growth_rate,

            "market_multiplier":
                self.market_multiplier,

            "revenue_score_weights":
                self.revenue_score_weights,

            "growth_adjustment":
                self.growth_adjustment,

            "operating_margin":
                self.operating_margin,

            "tax_rate":
                self.tax_rate,

            "scenarios":
                self.scenarios

        }