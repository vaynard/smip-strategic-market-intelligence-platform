import pandas as pd
import numpy as np
import numpy_financial as npf


class IRRCalculator:


    def __init__(

        self,

        cashflow_df,

        financial_config

    ):

        self.cashflow = cashflow_df.copy()

        self.config = financial_config


    # --------------------------------------------------
    # Calculate IRR
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

            cash_flows = [

                -self.config.initial_investment

            ]

            cash_flows.extend(

                group["net_cash_flow"].tolist()

            )

            irr = npf.irr(

                cash_flows

            )

            if np.isnan(

                irr

            ):

                irr = None

            else:

                irr = round(

                    irr * 100,

                    2

                )

            results.append({

                "country":
                    country,

                "country_name":
                    country_name,

                "irr":
                    irr

            })

        return pd.DataFrame(results)