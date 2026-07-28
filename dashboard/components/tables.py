import streamlit as st
import pandas as pd


class DashboardTables:


    # --------------------------------------------------
    # Standard Data Table
    # --------------------------------------------------

    @staticmethod
    def dataframe(

        df,

        use_container_width=True,

        hide_index=True

    ):

        st.dataframe(

            df,

            use_container_width=use_container_width,

            hide_index=hide_index

        )



    # --------------------------------------------------
    # Ranking Table
    # --------------------------------------------------

    @staticmethod
    def ranking_table(

        df

    ):

        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True

        )



    # --------------------------------------------------
    # Styled Table
    # --------------------------------------------------

    @staticmethod
    def styled_table(

        df,

        precision=2

    ):

        styled = (

            df.style

            .format(

                precision=precision

            )

        )

        st.dataframe(

            styled,

            use_container_width=True,

            hide_index=True

        )



    # --------------------------------------------------
    # Download Button
    # --------------------------------------------------

    @staticmethod
    def download_csv(

        df,

        filename,

        label="Download CSV"

    ):

        csv = df.to_csv(

            index=False

        )

        st.download_button(

            label=label,

            data=csv,

            file_name=filename,

            mime="text/csv"

        )



    # --------------------------------------------------
    # Show Table + Download
    # --------------------------------------------------

    @staticmethod
    def table_with_download(

        df,

        filename

    ):

        DashboardTables.dataframe(

            df

        )

        DashboardTables.download_csv(

            df,

            filename

        )