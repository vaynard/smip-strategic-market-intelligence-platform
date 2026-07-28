import streamlit as st

from utils.loader import DataLoader
from components.metrics import DashboardMetrics
from components.charts import DashboardCharts
from components.tables import DashboardTables


with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="SMIP Financial analysis",
    layout="wide"
)
# --------------------------------------------------
# Load Data
# --------------------------------------------------
loader = DataLoader()
npv = loader.npv()
irr = loader.irr()
payback = loader.payback()
sensitivity = loader.sensitivity()
revenue = loader.revenue_projection()
cashflow = loader.cashflow()
recommendation = loader.recommendation()

# ==================================================
# Header
# ==================================================
st.title("Financial Analysis")
st.caption("Evaluate the financial feasibility of market entry using capital budgeting metrics, revenue projections, cash flow forecasts, and investment attractiveness.")

# ==================================================
# Executive Summary
# ==================================================
if not npv.empty and not irr.empty and not payback.empty:
    best_npv = npv.sort_values("npv", ascending=False).iloc[0]
    best_irr = irr.sort_values("irr", ascending=False).iloc[0]
    fastest_payback = payback.sort_values("payback_period").iloc[0]
    average_npv = npv["npv"].mean()
    average_irr = irr["irr"].mean()

    left_wall, right_wall = st.columns([1.2, 1])

    with left_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">FINANCIAL VALUATION LEADER</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div style="font-size: 3rem; font-weight: 900; color: #0f172a; letter-spacing: -0.04em; line-height: 1.1; margin-bottom: 0.5rem;">{best_npv["country_name"]}</div>

This financial assessment evaluates **{npv['country'].nunique()} candidate markets**
using standard capital budgeting techniques.

Among the evaluated markets,
**{best_npv['country_name']}** delivers the highest **Net Present Value (NPV)**,
while **{best_irr['country_name']}** achieves the highest **Internal Rate of Return (IRR)**.
The average investment generates an estimated **NPV of {average_npv:,.0f}**
with an average **IRR of {average_irr:.2f}%**, indicating the overall financial
attractiveness of the evaluated market portfolio.
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        
        st.markdown('<div class="institutional-header">Capital Budgeting Portfolio</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Markets Evaluated</span><span class="corporate-value">{npv["country"].nunique()}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average NPV</span><span class="corporate-value">IDR {average_npv:,.0f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average IRR</span><span class="corporate-value">{average_irr:.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest NPV ({best_npv["country_name"]})</span><span class="corporate-value">IDR {best_npv["npv"]:,.0f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest IRR ({best_irr["country_name"]})</span><span class="corporate-value">{best_irr["irr"]:.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Fastest Payback ({fastest_payback["country_name"]})</span><span class="corporate-value">{fastest_payback["payback_period"]:.2f} Years</span></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Financial analysis unavailable.")

st.divider()

# ==================================================
# Financial Performance Comparison
# ==================================================
if not npv.empty and not irr.empty and not payback.empty:
    st.markdown('<div class="corporate-section-title">📊 Capital Budgeting Comparison</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Cross-market analysis of Net Present Value, Internal Rate of Return, and capital recovery timelines</div>', unsafe_allow_html=True)

    financial = npv.merge(irr, on=["country", "country_name"]).merge(payback, on=["country", "country_name"])

    left, right = st.columns(2)
    with left:
        DashboardCharts.horizontal_bar_chart(
            df=financial.sort_values("npv", ascending=False),
            x="npv",
            y="country_name",
            title="Net Present Value"
        )
    with right:
        DashboardCharts.horizontal_bar_chart(
            df=financial.sort_values("irr", ascending=False),
            x="irr",
            y="country_name",
            title="Internal Rate of Return"
        )

    st.markdown('### Capital Recovery')
    
    DashboardCharts.horizontal_bar_chart(
        df=financial.sort_values("payback_period"),
        x="payback_period",
        y="country_name",
        title="Payback Period"
    )

    best_npv_loc = financial.loc[financial["npv"].idxmax()]
    best_irr_loc = financial.loc[financial["irr"].idxmax()]
    fastest_loc = financial.loc[financial["payback_period"].idxmin()]

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
**{best_npv_loc['country_name']}** generates the highest projected
**Net Present Value (NPV)** of **{best_npv_loc['npv']:,.0f}**, indicating the
greatest absolute value creation among the evaluated investments.

**{best_irr_loc['country_name']}** achieves the highest
**Internal Rate of Return (IRR)** at **{best_irr_loc['irr']:.2f}%**, reflecting
the strongest expected investment profitability.

The fastest capital recovery is observed in
**{fastest_loc['country_name']}**, with an estimated payback period of
**{fastest_loc['payback_period']:.2f} years**.

Together, these metrics provide complementary perspectives on financial
performance by measuring value creation, profitability, and investment
recovery speed.
""")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Financial comparison unavailable.")

st.divider()

# ==================================================
# Revenue & Cash Flow Forecast
# ==================================================
if not revenue.empty and not cashflow.empty:
    st.markdown('<div class="corporate-section-title">📈 Revenue & Cash Flow Forecast</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Long-term prospective modeling of gross revenue baselines and cumulative operating inflows</div>', unsafe_allow_html=True)

    selected_country = st.selectbox(
        "Select Market",
        sorted(revenue["country_name"].unique()),
        key="forecast_country"
    )

    revenue_country = revenue[revenue["country_name"] == selected_country]
    cashflow_country = cashflow[cashflow["country_name"] == selected_country]

    left_forecast, right_forecast = st.columns(2)
    
    with left_forecast:
        DashboardCharts.line_chart(
            df=revenue_country,
            x="year",
            y="projected_revenue",
            title="Projected Revenue"
        )

    with right_forecast:
        DashboardCharts.line_chart(
            df=cashflow_country,
            x="year",
            y="net_cash_flow",
            title="Projected Net Cash Flow"
        )

    revenue_growth = (
        revenue_country.iloc[-1]["projected_revenue"]
        -
        revenue_country.iloc[0]["projected_revenue"]
    )

    total_cashflow = cashflow_country["net_cash_flow"].sum()

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
For **{selected_country}**, projected revenue increases steadily over the
forecast horizon, with an estimated total growth of
**{revenue_growth:,.0f}** between the first and final projection year.

Projected cash flows remain positive throughout the investment horizon,
producing cumulative net cash inflows of
**{total_cashflow:,.0f}**.

Together, these projections illustrate the expected operating performance
that underpins the calculated NPV, IRR, and payback period presented in the
financial evaluation.
""")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Revenue forecast unavailable.")

st.divider()

# ==================================================
# Sensitivity Analysis
# ==================================================
if not sensitivity.empty:
    st.markdown('<div class="corporate-section-title">📊 NPV Sensitivity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Stress-testing valuation stability across varying required rates of return assumptions</div>', unsafe_allow_html=True)

    selected_country_sens = st.selectbox(
        "Select Market",
        sorted(sensitivity["country_name"].unique()),
        key="sensitivity_country"
    )

    sensitivity_country = sensitivity[
        sensitivity["country_name"] == selected_country_sens
    ].sort_values("discount_rate")

    DashboardCharts.line_chart(
        df=sensitivity_country,
        x="discount_rate",
        y="npv",
        title="NPV Sensitivity to Discount Rate"
    )

    base_case = sensitivity_country.loc[
        (sensitivity_country["discount_rate"] - 0.10).abs().idxmin()
    ]

    lowest_case = sensitivity_country.iloc[0]
    highest_case = sensitivity_country.iloc[-1]
    npv_change = highest_case["npv"] - lowest_case["npv"]

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
For **{selected_country_sens}**, the base-case financial evaluation assumes a
discount rate of **{base_case['discount_rate']:.0%}**, producing an estimated
NPV of **{base_case['npv']:,.0f}**.

As the discount rate increases, the present value of future cash flows
declines, resulting in lower project valuations. Across the evaluated
discount-rate range, the estimated NPV changes by approximately
**{abs(npv_change):,.0f}**.

This sensitivity analysis demonstrates how changes in the required rate of
return influence investment value and provides an indication of the project's
robustness under different financing assumptions.
""")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Sensitivity analysis unavailable.")

st.divider()

# ==================================================
# Investment Attractiveness
# ==================================================
if not recommendation.empty:
    st.markdown('<div class="corporate-section-title">🎯 Investment Attractiveness Model</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Consolidated prioritization score mapping absolute value creation, internal efficiency, and capital safety</div>', unsafe_allow_html=True)

    DashboardCharts.horizontal_bar_chart(
        df=recommendation.sort_values("investment_score", ascending=False),
        x="investment_score",
        y="country_name",
        title="Financial Investment Score"
    )

    attr_sub_left, attr_sub_right = st.columns([1, 1.2])

    with attr_sub_left:
        st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">📋 Investment Prioritization Ranking</div>', unsafe_allow_html=True)
        DashboardTables.ranking_table(
            recommendation[
                [
                    "country_name",
                    "investment_score",
                    "recommendation"
                ]
            ]
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with attr_sub_right:
        best_market = recommendation.sort_values("investment_score", ascending=False).iloc[0]
        average_score = recommendation["investment_score"].mean()
        recommendation_distribution = recommendation["recommendation"].value_counts()
        top_category = recommendation_distribution.index[0]
        top_category_count = recommendation_distribution.iloc[0]

        st.markdown('<div class="horizon-text-block">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
        st.markdown(f"""
The financial attractiveness model combines **Net Present Value (NPV)**,
**Internal Rate of Return (IRR)**, and **Payback Period** into a single
investment score to support investment prioritization.

**{best_market['country_name']}** achieves the highest overall investment
score of **{best_market['investment_score']:.3f}**, making it the strongest
financial opportunity among the evaluated markets.

Across all evaluated markets, the average investment score is
**{average_score:.3f}**. The most common recommendation category is
**{top_category}**, assigned to **{top_category_count}**
market(s).
""")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Investment recommendation unavailable.")

st.divider()

# ==================================================
# Key Findings
# ==================================================
if (
    not recommendation.empty
    and not npv.empty
    and not irr.empty
    and not payback.empty
):
    st.markdown('<div class="corporate-section-title">💡 Financial Key Findings & Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Consolidated analytical highlights separating portfolio indicators and core decision logic</div>', unsafe_allow_html=True)

    recommendation_sorted = recommendation.sort_values("investment_score", ascending=False)
    best_market = recommendation_sorted.iloc[0]
    worst_market = recommendation_sorted.iloc[-1]
    average_score = recommendation_sorted["investment_score"].mean()
    score_gap = best_market["investment_score"] - worst_market["investment_score"]
    
    above_average = recommendation_sorted[
        recommendation_sorted["investment_score"] > average_score
    ]
    
    recommendation_distribution = recommendation_sorted["recommendation"].value_counts()
    best_npv = npv.loc[npv["npv"].idxmax()]
    best_irr = irr.loc[irr["irr"].idxmax()]
    fastest_payback = payback.loc[payback["payback_period"].idxmin()]
    
    same_market = (
        best_market["country_name"]
        == best_npv["country_name"]
        == best_irr["country_name"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Portfolio Insights</div>', unsafe_allow_html=True)
        st.markdown(f"""
- **{len(above_average)} of {len(recommendation_sorted)}** evaluated markets outperform the portfolio average investment score.
- The investment score ranges from **{worst_market['investment_score']:.3f}** to **{best_market['investment_score']:.3f}**, representing a spread of **{score_gap:.3f}**.
- **{recommendation_distribution.index[0]}** is the most frequently assigned recommendation category, indicating the overall quality of the evaluated market portfolio.
- **{best_market['country_name']}** ranks first in the integrated financial evaluation.
""")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Decision Insights</div>', unsafe_allow_html=True)
        if same_market:
            st.markdown(f"""
- **{best_market['country_name']}** simultaneously delivers the highest investment score, highest NPV, and highest IRR, making it the strongest overall financial opportunity.
- Capital recovery is fastest in **{fastest_payback['country_name']}**, indicating earlier investment recovery.
- The financial evaluation consistently supports prioritizing **{best_market['country_name']}** for market entry.
""")
        else:
            st.markdown(f"""
- Financial leadership is distributed across different markets rather than concentrated in a single country.
- **{best_npv['country_name']}** maximizes value creation through the highest NPV.
- **{best_irr['country_name']}** provides the highest expected rate of return, while **{fastest_payback['country_name']}** minimizes capital recovery time.
- Decision makers should balance profitability, value creation, and recovery speed when selecting the preferred investment destination.
""")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Financial insights unavailable.")

st.divider()

# ==================================================
# Appendix
# ==================================================
with st.expander("Appendix"):
    st.markdown("### Net Present Value")
    DashboardTables.table_with_download(npv, filename="net_present_value.csv")

    st.markdown("### Internal Rate of Return")
    DashboardTables.table_with_download(irr, filename="internal_rate_return.csv")

    st.markdown("### Payback Period")
    DashboardTables.table_with_download(payback, filename="payback_period.csv")

    st.markdown("### Investment Recommendation")
    DashboardTables.table_with_download(recommendation, filename="investment_recommendation.csv")

    if not sensitivity.empty:
        st.markdown("### Sensitivity Analysis")
        DashboardTables.table_with_download(sensitivity, filename="sensitivity_analysis.csv")

    if not revenue.empty:
        st.markdown("### Revenue Projection")
        DashboardTables.table_with_download(revenue, filename="revenue_projection.csv")

    if not cashflow.empty:
        st.markdown("### Cash Flow Projection")
        DashboardTables.table_with_download(cashflow, filename="cashflow_projection.csv")