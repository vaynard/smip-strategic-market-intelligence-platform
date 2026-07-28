import yaml
import pandas as pd
from datetime import datetime


class MetadataEnricher:

    def __init__(self, config_path):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        self.indicators = self.config["indicators"]


    def enrich(self, df):

        enriched = []


        for _, row in df.iterrows():

            indicator_code = row["indicator"]


            metadata = self.indicators.get(
                indicator_code
            )


            if metadata is None:
                raise ValueError(
                    f"Indicator {indicator_code} not found in configuration"
                )


            new_row = row.to_dict()


            new_row.update({

                "indicator_code":
                    indicator_code,

                "indicator_name":
                    metadata["name"],

                "description":
                    metadata["description"],

                "dimension":
                    metadata["dimension"],

                "role":
                    metadata["role"],

                "direction":
                    metadata["direction"],

                "unit":
                    metadata["unit"],

                "source":
                    metadata["source"],

                "collection_date":
                    datetime.now().date(),
                "aggregation": metadata["aggregation"],
				"lookback_years": metadata["lookback_years"],
				"normalization": metadata["normalization"],
				"required": metadata["required"],
				"validation":metadata["validation"],

            })


            enriched.append(new_row)


        return pd.DataFrame(enriched)