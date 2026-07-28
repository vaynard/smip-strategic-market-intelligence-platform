import pandas as pd


class RecommendationModel:

    def __init__(
        self,
        topsis,
        npv,
        irr,
        payback,
        weights
    ):

        self.topsis = topsis.copy()
        self.npv = npv.copy()
        self.irr = irr.copy()
        self.payback = payback.copy()
        self.weights = weights



    # --------------------------------------------------
    # Min Max Normalization
    # --------------------------------------------------

    def normalize(self, series):

        minimum = series.min()
        maximum = series.max()

        if maximum == minimum:
            return series * 0 + 1

        relative = (
            series - minimum
        ) / (
            maximum - minimum
        )

        return (
            0.5
            +
            relative * 0.5
        )



    # --------------------------------------------------
    # Run
    # --------------------------------------------------

    def run(self):


        result = (

            self.topsis

            .merge(
                self.npv,
                on=[
                    "country",
                    "country_name"
                ]
            )

            .merge(
                self.irr,
                on=[
                    "country",
                    "country_name"
                ]
            )

            .merge(
                self.payback,
                on=[
                    "country",
                    "country_name"
                ],
                how="left"
            )

        )


        # Market

        result["market_score"] = (
            result["topsis_score"]
        )


        # Financial

        result["npv_score"] = self.normalize(
            result["npv"]
        )


        result["irr_score"] = self.normalize(
            result["irr"]
        )


        # Lower payback is better

        result["payback_score"] = (
            1 -
            self.normalize(result["payback_period"])
        )

        result["payback_score"] = (
            0.5 +
            result["payback_score"] * 0.5
        )



        # Investment attractiveness

        result["investment_score"] = (

            result["market_score"]
            *
            self.weights["Market Attractiveness"]

            +

            result["npv_score"]
            *
            self.weights["Value Creation"]

            +

            result["irr_score"]
            *
            self.weights["Return Profile"]

            +

            result["payback_score"]
            *
            self.weights["Capital Recovery"]

        )


        result["investment_score"] = (
            result["investment_score"]
            .round(3)
        )


        result["recommendation"] = (

            result["investment_score"]

            .apply(
                self.classify
            )

        )


        return (

            result

            .sort_values(
                "investment_score",
                ascending=False
            )

            .reset_index(drop=True)

        )



    def classify(self, score):

        if score >= 0.75:

            return "Priority Entry"


        elif score >= 0.50:

            return "Strong Candidate"


        elif score >= 0.25:

            return "Monitor"


        else:

            return "Avoid"