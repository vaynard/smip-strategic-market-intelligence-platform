import pandas as pd

from src.financial.npv import NPVCalculator
from src.financial.irr import IRRCalculator
from src.financial.payback import PaybackCalculator


class SensitivityAnalysis:


    def __init__(

        self,

        cashflow_df,

        financial_config,

        scenarios

    ):

        self.cashflow = cashflow_df.copy()

        self.config = financial_config

        self.scenarios = scenarios


    # --------------------------------------------------
    # Run Sensitivity Analysis
    # --------------------------------------------------

    def run(self):

        results = []


        for scenario in self.scenarios:


            scenario_name = scenario["name"]

            revenue_factor = scenario["revenue_factor"]

            discount_rate = scenario["discount_rate"]

            operating_margin = scenario.get(
                "operating_margin",
                self.config.operating_margin
            )

            tax_rate = scenario.get(
                "tax_rate",
                self.config.tax_rate
            )


            adjusted = self.cashflow.copy()


            # --------------------------------------------------
            # Adjust Revenue
            # --------------------------------------------------

            adjusted["revenue"] = (

                adjusted["revenue"]

                *

                revenue_factor

            )


            # --------------------------------------------------
            # Recalculate Operating Model
            # --------------------------------------------------

            adjusted["operating_cost"] = (

                adjusted["revenue"]

                *

                (1 - operating_margin)

            )


            adjusted["operating_profit"] = (

                adjusted["revenue"]

                *

                operating_margin

            )


            adjusted["tax"] = (

                adjusted["operating_profit"]

                *

                tax_rate

            )


            adjusted["net_cash_flow"] = (

                adjusted["operating_profit"]

                -

                adjusted["tax"]

            )


            # --------------------------------------------------
            # Scenario Config
            # --------------------------------------------------

            class ScenarioConfig:

                pass


            config = ScenarioConfig()

            config.initial_investment = (

                self.config.initial_investment

            )

            config.discount_rate = discount_rate


            # --------------------------------------------------
            # Financial Metrics
            # --------------------------------------------------

            npv_result = NPVCalculator(

                adjusted,

                config

            ).run()


            npv = npv_result["summary"]


            irr = IRRCalculator(

                adjusted,

                config

            ).run()


            payback = PaybackCalculator(

                adjusted,

                config

            ).run()


            merged = (

                npv

                .merge(

                    irr,

                    on=[

                        "country",

                        "country_name"

                    ]

                )

                .merge(

                    payback,

                    on=[

                        "country",

                        "country_name"

                    ]

                )

            )


            # --------------------------------------------------
            # Scenario Metadata
            # --------------------------------------------------

            merged["scenario"] = scenario_name

            merged["revenue_factor"] = revenue_factor

            merged["discount_rate"] = discount_rate

            merged["operating_margin"] = operating_margin

            merged["tax_rate"] = tax_rate


            results.append(

                merged

            )


        return pd.concat(

            results,

            ignore_index=True

        )