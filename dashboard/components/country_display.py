import streamlit as st

from utils.country import get_country_flag



def display_country(

    country_code,

    country_name

):

    flag = get_country_flag(
        country_code
    )


    col1, col2 = st.columns(
        [0.15, 0.85]
    )


    with col1:

        if flag:

            st.image(

                flag,

                width=35

            )


    with col2:

        st.write(

            f"**{country_name}**"

        )