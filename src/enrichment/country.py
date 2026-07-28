import yaml
import pandas as pd


class CountryEnricher:

    def __init__(self, config_path):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        self.countries = self.config["countries"]


    def enrich(self, df):

        enriched = []


        for _, row in df.iterrows():

            country_code = row["country"]


            country = self.countries.get(
                country_code
            )


            if country is None:
                raise ValueError(
                    f"Country {country_code} not found"
                )


            new_row = row.to_dict()

            new_row["country_name"] = country["name"]


            enriched.append(new_row)


        return pd.DataFrame(enriched)