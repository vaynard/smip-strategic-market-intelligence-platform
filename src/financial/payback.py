import pandas as pd


class PaybackCalculator:


    def __init__(

        self,

        cashflow_df,

        financial_config

    ):

        self.cashflow = cashflow_df.copy()

        self.config = financial_config


    # --------------------------------------------------
    # Calculate Payback Period
    # --------------------------------------------------

    def run(self):

        results = []

        grouped = self.cashflow.groupby(

            [

                "country",

                "country_name"

            ]

        )


        for (

            (country, country_name),

            group

        ) in grouped:

            group = group.sort_values(

                "year"

            )

            cumulative = 0

            payback = None


            for _, row in group.iterrows():

                previous = cumulative

                cumulative += row["net_cash_flow"]


                if cumulative >= self.config.initial_investment:

                    remaining = (

                        self.config.initial_investment

                        -

                        previous

                    )

                    fraction = (

                        remaining

                        /

                        row["net_cash_flow"]

                    )

                    payback = (

                        row["year"]

                        -

                        1

                        +

                        fraction

                    )

                    break


            results.append({

                "country":
                    country,

                "country_name":
                    country_name,

                "payback_period":

                    None

                    if payback is None

                    else round(

                        payback,

                        2

                    )

            })


        return pd.DataFrame(

            results

        )