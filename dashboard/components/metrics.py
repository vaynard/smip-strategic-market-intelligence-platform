import streamlit as st


class DashboardMetrics:


    # --------------------------------------------------
    # Standard KPI Card
    # --------------------------------------------------

    @staticmethod
    def metric(

        label,

        value,

        delta=None,

        help_text=None

    ):

        st.metric(

            label=label,

            value=value,

            delta=delta,

            help=help_text

        )



    # --------------------------------------------------
    # Row of Metrics
    # --------------------------------------------------

    @staticmethod
    def metric_row(metrics):

        columns = st.columns(

            len(metrics)

        )

        for column, metric in zip(columns, metrics):

            with column:

                st.metric(

                    label=metric["label"],

                    value=metric["value"],

                    delta=metric.get("delta"),

                    help=metric.get("help")

                )



    # --------------------------------------------------
    # Success Metric
    # --------------------------------------------------

    @staticmethod
    def success(

        label,

        value

    ):

        st.success(

            f"**{label}:** {value}"

        )



    # --------------------------------------------------
    # Warning Metric
    # --------------------------------------------------

    @staticmethod
    def warning(

        label,

        value

    ):

        st.warning(

            f"**{label}:** {value}"

        )



    # --------------------------------------------------
    # Error Metric
    # --------------------------------------------------

    @staticmethod
    def error(

        label,

        value

    ):

        st.error(

            f"**{label}:** {value}"

        )



    # --------------------------------------------------
    # Info Metric
    # --------------------------------------------------

    @staticmethod
    def info(

        label,

        value

    ):

        st.info(

            f"**{label}:** {value}"

        )