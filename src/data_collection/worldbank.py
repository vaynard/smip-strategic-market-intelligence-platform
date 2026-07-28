import requests
import pandas as pd
import time


class WorldBankCollector:


    BASE_URL = (
        "https://api.worldbank.org/v2"
    )


    def __init__(
        self,
        retries=3,
        timeout=30,
        delay=1
    ):

        self.retries = retries
        self.timeout = timeout
        self.delay = delay



    def get_indicator(
        self,
        country,
        indicator
    ):


        url = (
            f"{self.BASE_URL}/country/"
            f"{country}/indicator/"
            f"{indicator}"
        )


        params = {

            "format": "json",

            "per_page": 100

        }



        for attempt in range(
            self.retries
        ):

            try:


                response = requests.get(

                    url,

                    params=params,

                    timeout=self.timeout

                )


                response.raise_for_status()


                data = response.json()


                records = []


                for item in data[1]:


                    if item["value"] is not None:


                        records.append({

                            "country":
                                country,

                            "indicator":
                                indicator,

                            "year":
                                int(item["date"]),

                            "value":
                                item["value"]

                        })


                time.sleep(
                    self.delay
                )


                return pd.DataFrame(records)



            except requests.exceptions.RequestException as error:


                print(
                    f"Attempt {attempt + 1}/{self.retries} failed:"
                )


                print(error)


                if attempt < self.retries - 1:

                    time.sleep(
                        3
                    )



        raise ConnectionError(

            f"Unable to collect {indicator} for {country}"

        )



    def get_multiple_countries(
        self,
        countries,
        indicators
    ):


        datasets = []


        failed_requests = []



        for country in countries:


            for indicator in indicators:


                print(
                    f"Collecting {indicator} - {country}"
                )


                try:


                    df = self.get_indicator(

                        country,

                        indicator

                    )


                    datasets.append(df)



                except Exception as error:


                    failed_requests.append({

                        "country":
                            country,

                        "indicator":
                            indicator,

                        "error":
                            str(error)

                    })


        if failed_requests:


            print("\nFAILED REQUESTS")

            print(
                pd.DataFrame(
                    failed_requests
                )
            )



        if len(datasets) == 0:

            return pd.DataFrame()



        return pd.concat(

            datasets,

            ignore_index=True

        )