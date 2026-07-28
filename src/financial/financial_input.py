import pandas as pd


class FinancialInputBuilder:

    def __init__(
        self,
        ranking,
        aggregated_df
    ):

        self.ranking = ranking.copy()
        self.aggregated_df = aggregated_df.copy()

    # --------------------------------------------------
    # Extract Indicator Values
    # --------------------------------------------------

    def extract_indicator(
        self,
        indicator_code,
        column_name
    ):

        indicator = (

            self.aggregated_df

            .loc[
                self.aggregated_df["indicator_code"] == indicator_code,
                [
                    "country",
                    "value"
                ]
            ]

            .rename(
                columns={
                    "value": column_name
                }
            )

        )

        return indicator

    # --------------------------------------------------
    # Build Financial Inputs
    # --------------------------------------------------

    def run(self):

        population = self.extract_indicator(
            "SP.POP.TOTL",
            "population"
        )

        gdp_per_capita = self.extract_indicator(
            "NY.GDP.PCAP.CD",
            "gdp_per_capita"
        )

        gdp_growth = self.extract_indicator(
            "NY.GDP.MKTP.KD.ZG",
            "gdp_growth"
        )

        financial_input = (

            self.ranking

            .merge(
                population,
                on="country",
                how="left"
            )

            .merge(
                gdp_per_capita,
                on="country",
                how="left"
            )

            .merge(
                gdp_growth,
                on="country",
                how="left"
            )

        )

        return financial_input