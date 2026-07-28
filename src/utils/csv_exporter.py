from pathlib import Path
import pandas as pd


class CSVExporter:


    def __init__(self):

        self.base_path = Path("data")


    # --------------------------------------------------
    # Export Dataset
    # --------------------------------------------------

    def export(

        self,

        data,

        folder,

        filename

    ):

        output_dir = self.base_path / folder

        output_dir.mkdir(

            parents=True,

            exist_ok=True

        )


        # -------------------------
        # DataFrame
        # -------------------------

        if isinstance(data, pd.DataFrame):

            data.to_csv(

                output_dir / filename,

                index=False

            )

            return


        # -------------------------
        # Dictionary
        # -------------------------

        if isinstance(data, dict):

            simple_values = {}

            table = None

            for key, value in data.items():

                if isinstance(value, pd.DataFrame):

                    table = value

                else:

                    simple_values[key] = value

            if simple_values:

                pd.DataFrame(

                    [simple_values]

                ).to_csv(

                    output_dir / filename,

                    index=False

                )

            if table is not None:

                table.to_csv(

                    output_dir / f"{Path(filename).stem}_details.csv",

                    index=False

                )

            return


        raise TypeError(

            f"Unsupported export type: {type(data)}"

        )


    # --------------------------------------------------
    # Export All Pipeline Outputs
    # --------------------------------------------------

    def export_pipeline(

        self,

        results

    ):

        exports = [

            ("raw_data", "raw", "worldbank_data.csv"),

            ("enriched_data", "enriched", "market_indicators.csv"),

            ("aggregated_data", "processed", "aggregated.csv"),

            ("normalized_data", "processed", "normalized.csv"),

            ("weighted_data", "processed", "weighted.csv"),

            ("dimension_scores", "analysis", "mcda_dimension_scores.csv"),

            ("market_scores", "analysis", "mcda_market_scores.csv"),

            ("topsis_ranking", "analysis", "topsis_ranking.csv"),

            ("recommendation", "analysis", "investment_recommendation.csv"),

            ("npv", "finance", "npv.csv"),

            ("irr", "finance", "irr.csv"),

            ("payback", "finance", "payback.csv"),

            ("sensitivity", "finance", "sensitivity.csv"),

            ("revenue_projection", "finance", "revenue_projection.csv"),

            ("cashflow", "finance", "cashflow.csv"),
            ("financial_input", "finance", "financial_input.csv")

        ]


        for key, folder, filename in exports:

            if key in results:

                self.export(

                    results[key],

                    folder,

                    filename

                )