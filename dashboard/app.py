import streamlit as st
from utils.loader import DataLoader


pages = [
    st.Page("pages/home.py", title="Home", default=True),
    st.Page("pages/overview.py", title="Recommendation Overview"),
    st.Page("pages/market_analysis.py", title="Market Analysis"),
    st.Page("pages/financial_analysis.py", title="Financial Analysis"),
    st.Page("pages/methodology.py", title="Methodology"),
    st.Page("pages/assumption.py", title="Assumption"),
]

pg = st.navigation(pages)
pg.run()