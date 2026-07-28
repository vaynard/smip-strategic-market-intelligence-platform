import yaml


class IndicatorConfig:

    def __init__(
        self,
        config_path
    ):

        with open(
            config_path,
            "r"
        ) as file:

            self.config = yaml.safe_load(file)

        self.indicators = self.config["indicators"]

    # --------------------------------------------------
    # Required Indicator Codes
    # --------------------------------------------------

    def get_required_indicators(self):

        return [

            indicator

            for indicator, metadata in self.indicators.items()

            if metadata.get(
                "required",
                False
            )

        ]

    # --------------------------------------------------
    # All Indicator Codes
    # --------------------------------------------------

    def get_all_indicators(self):

        return list(

            self.indicators.keys()

        )