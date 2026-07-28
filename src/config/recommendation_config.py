import yaml


class RecommendationConfig:


    def __init__(
        self,
        config_path="config/recommendation.yaml"
    ):

        with open(
            config_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.config = yaml.safe_load(file)


        self.validate()



    def validate(self):

        if "criteria" not in self.config:

            raise ValueError(
                "Recommendation config missing criteria section"
            )


        total_weight = sum(

            item["weight"]

            for item in self.config["criteria"].values()

        )


        if round(total_weight, 5) != 1:

            raise ValueError(
                f"Recommendation weights must equal 1. Current: {total_weight}"
            )



    def get_weights(self):

        criteria = self.config["criteria"]

        return {

            key: value["weight"]

            for key, value in criteria.items()

        }