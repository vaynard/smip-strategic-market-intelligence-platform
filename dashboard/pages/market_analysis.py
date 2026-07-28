import streamlit as st

from utils.loader import DataLoader
from components.charts import DashboardCharts
from components.tables import DashboardTables

# --------------------------------------------------
# External CSS Loader
# --------------------------------------------------
# Membaca berkas stylesheet eksternal dari direktori assets Anda
with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="SMIP Market Analysis",
    layout="wide"
)
# --------------------------------------------------
# Load Data
# --------------------------------------------------
loader = DataLoader()
dimension_scores = loader.dimension_scores()
weighted = loader.weighted_data()
ranking = loader.topsis_ranking()

# ==================================================
# Header
# ==================================================
st.title("Market Analysis")
st.caption("Evaluate market attractiveness across candidate countries using Multi-Criteria Decision Analysis (MCDA) and TOPSIS.")

# ==================================================
# Executive Summary
# ==================================================
if not ranking.empty:
    best_market = ranking.sort_values("rank").iloc[0]
    average_score = ranking["topsis_score"].mean()
    strongest_dimension = dimension_scores.groupby("dimension")["weighted_score"].mean().idxmax()

    left_wall, right_wall = st.columns([1.2, 1])

    with left_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">PRIMARY SELECTION</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div style="font-size: 3rem; font-weight: 900; color: #0f172a; letter-spacing: -0.04em; line-height: 1.1; margin-bottom: 0.5rem;">{best_market["country_name"]}</div>

This analysis evaluates **{ranking['country'].nunique()} candidate markets** using the project's
Multi-Criteria Decision Analysis framework.

Based on the weighted evaluation, **{best_market['country_name']}**
achieves the highest overall market attractiveness score, indicating the
strongest strategic opportunity among the evaluated countries.
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        
        st.markdown('<div class="institutional-header">MCDA Strategic Framework</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Markets Evaluated</span><span class="corporate-value">{ranking["country"].nunique()}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Top Strategic Market</span><span class="corporate-value">{best_market["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Average TOPSIS Score</span><span class="corporate-value">{average_score:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Strongest Dimension</span><span class="corporate-value">{strongest_dimension}</span></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Market analysis unavailable.")

st.divider()

# ==================================================
# TOPSIS Analysis
# ==================================================
if not ranking.empty:
    st.markdown('<div class="corporate-section-title">🎯 Market Comparison Framework</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Relative closeness metric calculations to the ideal strategic solution profile</div>', unsafe_allow_html=True)

    DashboardCharts.horizontal_bar_chart(
        df=ranking.sort_values("topsis_score", ascending=False),
        x="topsis_score",
        y="country_name",
        title="Relative Closeness to Ideal Solution"
    )


    st.markdown('<div class="institutional-header">📋 TOPSIS Asset Ranking</div>', unsafe_allow_html=True)
    DashboardTables.ranking_table(ranking.sort_values("rank"))
    st.markdown('</div>', unsafe_allow_html=True)

    best = ranking.sort_values("rank").iloc[0]
    average_score = ranking["topsis_score"].mean()
    median_score = ranking["topsis_score"].median()
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
TOPSIS ranks candidate markets according to their relative closeness to the
ideal market profile constructed from all evaluation criteria.

**{best['country_name']}** achieves the highest TOPSIS score of
**{best['topsis_score']:.3f}**, indicating the strongest overall strategic
position among the evaluated countries.

The portfolio average TOPSIS score is **{average_score:.3f}**, while the
median score is **{median_score:.3f}**, providing a benchmark for comparing
individual market performance.

Higher TOPSIS scores indicate markets that more closely resemble the ideal
combination of economic potential, business environment, market opportunity,
and other strategic dimensions incorporated within the MCDA framework.
""")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("TOPSIS analysis unavailable.")

st.divider()
# ==================================================
# Dimension Performance
# ==================================================
st.markdown('<div class="corporate-section-title">📊 Dimension Performance Assessment</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Compare market performance profiles across the strategic dimensions used in the MCDA framework</div>', unsafe_allow_html=True)

comparison_countries = st.multiselect(
    "Compare Markets",
    sorted(dimension_scores["country_name"].unique()),
    default=ranking.sort_values("rank").head(5)["country_name"].tolist(),
    key="radar_compare"
)

comparison_scores = dimension_scores[
    dimension_scores["country_name"].isin(comparison_countries)
]

top_left, top_right = st.columns(2)

# --------------------------------------------------
# Radar Chart
# --------------------------------------------------
with top_left:
    radar = comparison_scores.pivot(
        index="dimension",
        columns="country_name",
        values="weighted_score"
    ).reset_index()

    DashboardCharts.radar_chart(
        radar,
        category="dimension",
        value="weighted_score",
        title="Dimension Comparison"
    )

# --------------------------------------------------
# Heatmap
# --------------------------------------------------
with top_right:
    heatmap = comparison_scores.pivot(
        index="country_name",
        columns="dimension",
        values="weighted_score"
    )

    DashboardCharts.heatmap(
        heatmap,
        title="Dimension Heatmap"
    )

# --------------------------------------------------
# Country Contribution (Redesign Horizon Stack)
# --------------------------------------------------

selected_country_dimension = st.selectbox(
    "Select Country",
    sorted(dimension_scores["country_name"].unique()),
    key="dimension_country"
)

country_dimension = dimension_scores[
    dimension_scores["country_name"] == selected_country_dimension
].sort_values("weighted_score", ascending=False)

DashboardCharts.horizontal_bar_chart(
    df=country_dimension,
    x="weighted_score",
    y="dimension",
    title=f"{selected_country_dimension} Dimension Contribution"
)

best_dimension = country_dimension.iloc[0]
worst_dimension = country_dimension.iloc[-1]

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
st.markdown(f"""
For **{selected_country_dimension}**, the strongest contribution to overall
market attractiveness comes from the **{best_dimension['dimension']}**
dimension, while **{worst_dimension['dimension']}** contributes the least.

The radar chart and heatmap compare the selected markets across the strategic
dimensions of the MCDA framework, while the contribution chart explains how
each dimension contributes to the selected country's overall market
attractiveness.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
# ==================================================
# Indicator Drill-down
# ==================================================
st.markdown('<div class="corporate-section-title">🔍 Indicator Drill-down Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Inspect the normalized indicator values supporting the foundational MCDA calculation framework</div>', unsafe_allow_html=True)

selected_country = st.selectbox(
    "Select Market",
    sorted(weighted["country_name"].unique()),
    key="indicator_country"
)

indicator_data = weighted[
    weighted["country_name"] == selected_country
].sort_values(["dimension", "indicator_name"])

dimension_filter = st.multiselect(
    "Filter Dimensions",
    sorted(indicator_data["dimension"].unique()),
    default=sorted(indicator_data["dimension"].unique())
)

indicator_data = indicator_data[
    indicator_data["dimension"].isin(dimension_filter)
]

indicator_summary = (
    indicator_data
    .groupby("dimension")
    .agg(
        indicators=("indicator_name", "count"),
        average_score=("normalized_score", "mean")
    )
    .reset_index()
)

DashboardCharts.horizontal_bar_chart(
    df=indicator_summary.sort_values("average_score", ascending=True),
    x="average_score",
    y="dimension",
    title="Average Normalized Score"
)

st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
st.markdown(f'<div class="institutional-header">📋 {selected_country} Detailed Indicator Dataset</div>', unsafe_allow_html=True)
DashboardTables.dataframe(
    indicator_data[
        [
            "dimension",
            "indicator_name",
            "value",
            "normalized_score"
        ]
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

DashboardTables.table_with_download(
    indicator_data,
    filename=f"{selected_country.lower()}_indicator_scores.csv"
)

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)

best_dimension = (
    indicator_summary
    .sort_values("average_score", ascending=False)
    .iloc[0]
)

st.markdown(f"""
For **{selected_country}**, the strongest overall indicator performance
is observed in the **{best_dimension['dimension']}** dimension.

The indicator table presents the original values alongside their normalized
scores used during MCDA processing, providing full traceability from raw
data to the final market attractiveness assessment.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
# ==================================================
# Key Findings
# ==================================================
if not ranking.empty and not dimension_scores.empty:
    st.markdown('<div class="corporate-section-title">💡 Institutional Key Findings & Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Consolidated analytical highlights separating market intelligence dimensions and strategic conclusions</div>', unsafe_allow_html=True)

    ranking = ranking.sort_values("rank")
    best_market = ranking.iloc[0]
    worst_market = ranking.iloc[-1]
    average_score = ranking["topsis_score"].mean()
    median_score = ranking["topsis_score"].median()
    score_gap = best_market["topsis_score"] - worst_market["topsis_score"]
    
    above_average = ranking[
        ranking["topsis_score"] > average_score
    ]["country_name"].tolist()

    dimension_average = (
        dimension_scores
        .groupby("dimension")["weighted_score"]
        .mean()
        .sort_values(ascending=False)
    )
    strongest_dimension = dimension_average.index[0]
    weakest_dimension = dimension_average.index[-1]

    top_country_dimension = (
        dimension_scores[
            dimension_scores["country_name"] == best_market["country_name"]
        ]
        .sort_values("weighted_score", ascending=False)
        .iloc[0]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Market Insights</div>', unsafe_allow_html=True)
        st.markdown(f"""
- **{best_market['country_name']}** ranks **#1** with a TOPSIS score of **{best_market['topsis_score']:.3f}**.
- The portfolio average TOPSIS score is **{average_score:.3f}**, while the median score is **{median_score:.3f}**.
- **{len(above_average)} of {len(ranking)}** evaluated markets perform above the portfolio average.
- The difference between the highest and lowest ranked markets is **{score_gap:.3f}**, indicating a meaningful separation in overall market attractiveness.
""")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Strategic Insights</div>', unsafe_allow_html=True)
        st.markdown(f"""
- **{strongest_dimension}** is the strongest-performing dimension across the evaluated markets.
- **{weakest_dimension}** represents the weakest average dimension and the largest opportunity for improvement.
- For **{best_market['country_name']}**, the largest contributor to its market attractiveness is **{top_country_dimension['dimension']}**.
- Overall market attractiveness is driven by different combinations of dimension performance rather than a single indicator, reinforcing the value of the MCDA framework.
""")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Key findings unavailable.")

st.divider()

# ==================================================
# Appendix
# ==================================================
with st.expander("Appendix"):
    st.markdown("### Dimension Scores")
    DashboardTables.table_with_download(
        dimension_scores,
        filename="mcda_dimension_scores.csv"
    )

    st.markdown("### Weighted Indicator Dataset")
    DashboardTables.table_with_download(
        weighted,
        filename="weighted_indicator_scores.csv"
    )

    st.markdown("### TOPSIS Ranking")
    DashboardTables.table_with_download(
        ranking,
        filename="topsis_ranking.csv"
    )