import numpy as np
import pandas as pd


class RevenueProjection:

    def __init__(

        self,

        financial_input,

        financial_config

    ):

        self.financial_input = financial_input.copy()

        self.config = financial_config

        self.prepare_scaling()

    # --------------------------------------------------
    # Prepare Log Scaling
    # --------------------------------------------------

    def prepare_scaling(self):

        self.financial_input["population_log"] = np.log(

            self.financial_input["population"]

        )

        self.financial_input["income_log"] = np.log(

            self.financial_input["gdp_per_capita"]

        )

        self.population_min = self.financial_input["population_log"].min()

        self.population_max = self.financial_input["population_log"].max()

        self.income_min = self.financial_input["income_log"].min()

        self.income_max = self.financial_input["income_log"].max()

    # --------------------------------------------------
    # Normalize
    # --------------------------------------------------

    def normalize(

        self,

        value,

        minimum,

        maximum

    ):

        if maximum == minimum:

            return 1.0

        return (

            value - minimum

        ) / (

            maximum - minimum

        )

    # --------------------------------------------------
    # Market Multiplier
    # --------------------------------------------------

    def calculate_market_multiplier(

        self,

        topsis_score,

        population,

        gdp_per_capita

    ):

        population_score = self.normalize(

            np.log(population),

            self.population_min,

            self.population_max

        )

        income_score = self.normalize(

            np.log(gdp_per_capita),

            self.income_min,

            self.income_max

        )

        weights = self.config.revenue_score_weights

        revenue_score = (

            weights["topsis"] * topsis_score

            +

            weights["population"] * population_score

            +

            weights["income"] * income_score

        )

        minimum = self.config.market_multiplier["minimum"]

        maximum = self.config.market_multiplier["maximum"]

        multiplier = (

            minimum

            +

            revenue_score

            *

            (

                maximum

                -

                minimum

            )

        )

        return (

            multiplier,

            population_score,

            income_score,

            revenue_score

        )

    # --------------------------------------------------
    # Growth Rate
    # --------------------------------------------------

    def calculate_growth_rate(

        self,

        gdp_growth

    ):

        return (

            self.config.base_growth_rate

            +

            (

                gdp_growth / 100

            )

            *

            self.config.growth_adjustment["gdp_growth_weight"]

        )

    # --------------------------------------------------
    # Revenue Projection
    # --------------------------------------------------

    def run(self):

        rows = []

        for _, row in self.financial_input.iterrows():

            (

                multiplier,

                population_score,

                income_score,

                revenue_score

            ) = self.calculate_market_multiplier(

                row["topsis_score"],

                row["population"],

                row["gdp_per_capita"]

            )

            growth_rate = self.calculate_growth_rate(

                row["gdp_growth"]

            )

            revenue = (

                self.config.base_revenue

                *

                multiplier

            )

            for year in range(

                1,

                self.config.project_years + 1

            ):

                rows.append({

                    "country": row["country"],

                    "country_name": row["country_name"],

                    "year": year,

                    "topsis_score": round(

                        row["topsis_score"],

                        4

                    ),

                    "population_score": round(

                        population_score,

                        4

                    ),

                    "income_score": round(

                        income_score,

                        4

                    ),

                    "revenue_score": round(

                        revenue_score,

                        4

                    ),

                    "market_multiplier": round(

                        multiplier,

                        4

                    ),

                    "growth_rate": round(

                        growth_rate,

                        4

                    ),

                    "projected_revenue": round(

                        revenue,

                        2

                    )

                })

                revenue *= (

                    1

                    +

                    growth_rate

                )

        return pd.DataFrame(

            rows

        )