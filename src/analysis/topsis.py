import pandas as pd
import numpy as np


class TOPSISModel:

    def __init__(
        self,
        df
    ):

        self.df = df.copy()

    # -------------------------
    # Prepare Decision Matrix
    # -------------------------

    def create_matrix(self):

        matrix = (

            self.df

            .pivot(

                index=[
                    "country",
                    "country_name"
                ],

                columns="dimension",

                values="weighted_score"

            )

            .fillna(0)

        )

        return matrix

    # -------------------------
    # Normalize Decision Matrix
    # -------------------------

    def normalize_matrix(

        self,

        matrix

    ):

        denominator = np.sqrt(

            (matrix ** 2).sum(axis=0)

        )

        denominator = denominator.replace(

            0,

            1

        )

        normalized = (

            matrix

            /

            denominator

        )

        return normalized

    # -------------------------
    # Ideal Solutions
    # -------------------------

    def calculate_ideal_solution(

        self,

        normalized_matrix

    ):

        ideal_best = normalized_matrix.max()

        ideal_worst = normalized_matrix.min()

        return (

            ideal_best,

            ideal_worst

        )

    # -------------------------
    # Distance Calculation
    # -------------------------

    def calculate_distance(

        self,

        matrix,

        ideal

    ):

        distance = np.sqrt(

            (

                (matrix - ideal)

                ** 2

            )

            .sum(axis=1)

        )

        return distance

    # -------------------------
    # TOPSIS Score
    # -------------------------

    def calculate_score(

        self,

        normalized_matrix

    ):

        ideal_best, ideal_worst = (

            self.calculate_ideal_solution(

                normalized_matrix

            )

        )

        distance_best = (

            self.calculate_distance(

                normalized_matrix,

                ideal_best

            )

        )

        distance_worst = (

            self.calculate_distance(

                normalized_matrix,

                ideal_worst

            )

        )

        score = (

            distance_worst

            /

            (

                distance_best

                +

                distance_worst

            )

        )

        return score

    # -------------------------
    # Run TOPSIS
    # -------------------------

    def run(self):

        matrix = self.create_matrix()

        if len(matrix) < 2:

            raise ValueError(

                "TOPSIS requires at least two countries for ranking."

            )

        normalized_matrix = self.normalize_matrix(

            matrix

        )

        scores = self.calculate_score(

            normalized_matrix

        )

        result = scores.reset_index()

        result.columns = [

            "country",

            "country_name",

            "topsis_score"

        ]

        result["rank"] = (

            result["topsis_score"]

            .rank(

                ascending=False,

                method="dense"

            )

            .astype(int)

        )

        result = (

            result

            .sort_values(

                "rank"

            )

            .reset_index(

                drop=True

            )

        )

        return result