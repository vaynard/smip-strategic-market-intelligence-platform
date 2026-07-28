import pandas as pd


class DataNormalizer:

    def __init__(self, df):

        self.df = df.copy()

        required_columns = [
            "indicator_code",
            "value",
            "direction",
            "normalization"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in self.df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

    # -------------------------
    # Min-Max Normalization
    # -------------------------

    def min_max_normalize(
        self,
        series
    ):

        minimum = series.min()

        maximum = series.max()

        # All countries have identical value
        if maximum == minimum:

            return pd.Series(
                [100.0] * len(series),
                index=series.index
            )

        normalized = (
            (series - minimum)
            /
            (maximum - minimum)
        )

        return normalized * 100

    # -------------------------
    # Benefit Indicator
    # Higher = Better
    # -------------------------

    def normalize_benefit(
        self,
        series,
        method
    ):

        if method == "min_max":

            return self.min_max_normalize(
                series
            )

        raise ValueError(
            f"Unsupported normalization method: {method}"
        )

    # -------------------------
    # Cost Indicator
    # Higher = Worse
    # -------------------------

    def normalize_cost(
        self,
        series,
        method
    ):

        if method == "min_max":

            return (
                100
                -
                self.min_max_normalize(
                    series
                )
            )

        raise ValueError(
            f"Unsupported normalization method: {method}"
        )

    # -------------------------
    # Normalize All Indicators
    # -------------------------

    def normalize(self):

        normalized_rows = []

        grouped = self.df.groupby(
            "indicator_code"
        )

        for indicator_code, group in grouped:

            group = group.copy()

            direction = (
                group["direction"]
                .iloc[0]
            )

            normalization_method = (
                group["normalization"]
                .iloc[0]
            )

            if direction == "benefit":

                scores = self.normalize_benefit(
                    group["value"],
                    normalization_method
                )

            elif direction == "cost":

                scores = self.normalize_cost(
                    group["value"],
                    normalization_method
                )

            else:

                raise ValueError(
                    f"Unknown direction '{direction}' for indicator '{indicator_code}'"
                )

            group["normalized_score"] = scores

            normalized_rows.append(
                group
            )

        return pd.concat(
            normalized_rows,
            ignore_index=True
        )