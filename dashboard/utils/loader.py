from pathlib import Path

import pandas as pd
import streamlit as st


# --------------------------------------------------
# Cached CSV Loader
# --------------------------------------------------

@st.cache_data(show_spinner=False)
def load_csv(path):

    path = Path(path)

    if not path.exists():

        raise FileNotFoundError(

            f"Dataset not found: {path}"

        )

    return pd.read_csv(path)



class DataLoader:


    def __init__(

        self,

        base_path="data"

    ):

        self.base_path = Path(base_path)



    # --------------------------------------------------
    # Raw Data
    # --------------------------------------------------

    def raw_data(self):

        return load_csv(

            self.base_path / "raw/worldbank_data.csv"

        )



    # --------------------------------------------------
    # Enriched Data
    # --------------------------------------------------

    def enriched_data(self):

        return load_csv(

            self.base_path / "enriched/market_indicators.csv"

        )



    # --------------------------------------------------
    # Processed Data
    # --------------------------------------------------

    def aggregated_data(self):

        return load_csv(

            self.base_path / "processed/aggregated.csv"

        )



    def normalized_data(self):

        return load_csv(

            self.base_path / "processed/normalized.csv"

        )



    def weighted_data(self):

        return load_csv(

            self.base_path / "processed/weighted.csv"

        )



    # --------------------------------------------------
    # MCDA Analysis
    # --------------------------------------------------

    def dimension_scores(self):

        return load_csv(

            self.base_path / "analysis/mcda_dimension_scores.csv"

        )



    def market_scores(self):

        return load_csv(

            self.base_path / "analysis/mcda_market_scores.csv"

        )



    # --------------------------------------------------
    # TOPSIS
    # --------------------------------------------------

    def topsis_ranking(self):

        return load_csv(

            self.base_path / "analysis/topsis_ranking.csv"

        )



    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------

    def recommendation(self):

        return load_csv(

            self.base_path / "analysis/investment_recommendation.csv"

        )



    # --------------------------------------------------
    # Finance
    # --------------------------------------------------

    def npv(self):

        return load_csv(

            self.base_path / "finance/npv.csv"

        )



    def irr(self):

        return load_csv(

            self.base_path / "finance/irr.csv"

        )



    def payback(self):

        return load_csv(

            self.base_path / "finance/payback.csv"

        )



    def sensitivity(self):

        return load_csv(

            self.base_path / "finance/sensitivity.csv"

        )



    def revenue_projection(self):

        return load_csv(

            self.base_path / "finance/revenue_projection.csv"

        )



    def cashflow(self):

        return load_csv(

            self.base_path / "finance/cashflow.csv"

        )