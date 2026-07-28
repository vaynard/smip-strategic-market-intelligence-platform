import pandas as pd


class NPVCalculator:

    def __init__(

        self,

        cashflow_df,

        financial_config

    ):

        self.cashflow = cashflow_df.copy()

        self.config = financial_config

    # --------------------------------------------------
    # Calculate Present Value
    # --------------------------------------------------

    def calculate_present_value(

        self,

        cash_flow,

        year,

        discount_rate

    ):

        return (

            cash_flow

            /

            (

                1

                +

                discount_rate

            ) ** year

        )

    # --------------------------------------------------
    # Calculate NPV
    # --------------------------------------------------

    def run(self):

        summary_rows = []

        detail_rows = []

        discount_rate = self.config.discount_rate

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

            cumulative_discounted_cash_flow = 0

            discounted_cash_flows = []

            for _, row in group.iterrows():

                discounted_cash_flow = self.calculate_present_value(

                    row["net_cash_flow"],

                    row["year"],

                    discount_rate

                )

                cumulative_discounted_cash_flow += discounted_cash_flow

                discounted_cash_flows.append(

                    discounted_cash_flow

                )

                detail_rows.append({

                    "country":
                        country,

                    "country_name":
                        country_name,

                    "year":
                        row["year"],

                    "cash_flow":
                        round(row["net_cash_flow"], 2),

                    "discounted_cash_flow":
                        round(discounted_cash_flow, 2),

                    "cumulative_discounted_cash_flow":
                        round(cumulative_discounted_cash_flow, 2)

                })

            npv = (

                sum(

                    discounted_cash_flows

                )

                -

                self.config.initial_investment

            )

            summary_rows.append({

                "country":
                    country,

                "country_name":
                    country_name,

                "discount_rate":
                    discount_rate,

                "initial_investment":
                    self.config.initial_investment,

                "npv":
                    round(npv, 2)

            })

        return {

            "summary":
                pd.DataFrame(summary_rows),

            "details":
                pd.DataFrame(detail_rows)

        }