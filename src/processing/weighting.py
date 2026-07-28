import yaml


class WeightAssigner:

    def __init__(
        self,
        df,
        config_path
    ):

        self.df = df.copy()

        with open(config_path, "r") as file:

            self.config = yaml.safe_load(file)

        self.dimensions = self.config["dimensions"]

        required_columns = [
            "dimension",
            "normalized_score"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in self.df.columns
        ]

        if missing_columns:

            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

    # -------------------------
    # Get Dimension Weight
    # -------------------------

    def get_dimension_weight(
        self,
        dimension
    ):

        metadata = self.dimensions.get(
            dimension
        )

        if metadata is None:

            raise ValueError(
                f"Dimension '{dimension}' not found in weights configuration."
            )

        return metadata["weight"]

    # -------------------------
    # Apply Weights
    # -------------------------

    def apply_weights(self):

        weighted = self.df.copy()

        weighted["dimension_weight"] = (

            weighted["dimension"]

            .apply(
                self.get_dimension_weight
            )

        )

        return weighted