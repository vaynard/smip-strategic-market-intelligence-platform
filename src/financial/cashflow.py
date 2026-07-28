import pandas as pd


class CashFlowGenerator:

    def __init__(

        self,

        revenue_projection,

        financial_config

    ):

        self.revenue = revenue_projection.copy()

        self.config = financial_config


    # --------------------------------------------------
    # Generate Cash Flows
    # --------------------------------------------------

    def run(self):

        rows = []

        operating_margin = self.config.operating_margin
        tax_rate = self.config.tax_rate

        for _, row in self.revenue.iterrows():

            revenue = row["projected_revenue"]

            operating_cost = (

                revenue

                *

                (

                    1

                    -

                    operating_margin

                )

            )

            operating_profit = (

                revenue

                -

                operating_cost

            )

            tax = (

                operating_profit

                *

                tax_rate

            )

            net_cash_flow = (

                operating_profit

                -

                tax

            )

            rows.append({

                "country":
                    row["country"],

                "country_name":
                    row["country_name"],

                "year":
                    row["year"],

                "revenue":
                    round(revenue, 2),

                "operating_cost":
                    round(operating_cost, 2),

                "operating_profit":
                    round(operating_profit, 2),

                "tax":
                    round(tax, 2),

                "net_cash_flow":
                    round(net_cash_flow, 2)

            })

        return pd.DataFrame(rows)