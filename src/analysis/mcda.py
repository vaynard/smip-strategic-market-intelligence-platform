import pandas as pd


class MCDAModel:

    def __init__(self, df):

        self.df = df.copy()

    # -------------------------
    # Calculate Dimension Scores
    # -------------------------

    def calculate_dimension_scores(self):

        dimension_scores = (

            self.df

            .groupby(
                [
                    "country",
                    "country_name",
                    "dimension",
                    "dimension_weight"
                ],
                as_index=False
            )

            .agg(

                normalized_score=(

                    "normalized_score",

                    "mean"

                )

            )

        )

        dimension_scores["weighted_score"] = (

            dimension_scores["normalized_score"]

            *

            dimension_scores["dimension_weight"]

        )

        dimension_scores = (

            dimension_scores

            .sort_values(
                [
                    "country",
                    "dimension"
                ]
            )

            .reset_index(
                drop=True
            )

        )

        return dimension_scores

    # -------------------------
    # Calculate Overall Score
    # -------------------------

    def calculate_market_score(

        self,

        dimension_scores

    ):

        market_scores = (

            dimension_scores

            .groupby(
                [
                    "country",
                    "country_name"
                ],
                as_index=False
            )

            .agg(

                market_priority_score=(

                    "weighted_score",

                    "sum"

                )

            )

        )

        market_scores = (

            market_scores

            .sort_values(
                "market_priority_score",
                ascending=False
            )

            .reset_index(
                drop=True
            )

        )

        return market_scores

    # -------------------------
    # Full Analysis
    # -------------------------

    def run(self):

        dimension_scores = (

            self.calculate_dimension_scores()

        )

        market_scores = (

            self.calculate_market_score(
                dimension_scores
            )

        )

        return {

            "dimension_scores": dimension_scores,

            "market_scores": market_scores

        }