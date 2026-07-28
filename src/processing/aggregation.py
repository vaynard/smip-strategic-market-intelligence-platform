import pandas as pd


class AggregationEngine:


    def __init__(

        self,

        df

    ):

        self.df = df.copy()


    # --------------------------------------------------
    # Aggregate Historical Data
    # --------------------------------------------------

    def aggregate(self):

        aggregated_rows = []

        grouped = self.df.groupby(

            [

                "country",

                "indicator_code"

            ]

        )


        for (_, _), group in grouped:

            group = group.sort_values(

                "year",

                ascending=False

            )

            metadata = group.iloc[0]

            method = metadata["aggregation"]

            lookback = metadata["lookback_years"]

            recent = group.head(

                lookback

            )


            if method == "latest":

                aggregated_value = self._latest(

                    recent

                )


            elif method == "mean":

                aggregated_value = self._mean(

                    recent

                )


            else:

                raise ValueError(

                    f"Unsupported aggregation method: {method}"

                )


            result = metadata.to_dict()

            result["value"] = aggregated_value

            result["year"] = recent["year"].max()

            aggregated_rows.append(

                result

            )


        return pd.DataFrame(

            aggregated_rows

        )


    # --------------------------------------------------
    # Latest Value
    # --------------------------------------------------

    def _latest(

        self,

        df

    ):

        return df.iloc[0]["value"]


    # --------------------------------------------------
    # Mean Value
    # --------------------------------------------------

    def _mean(

        self,

        df

    ):

        return df["value"].mean()