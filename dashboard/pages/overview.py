import streamlit as st

from utils.loader import DataLoader
from utils.recommendation_badge import recommendation_badge

from components.metrics import DashboardMetrics
from components.charts import DashboardCharts
from components.tables import DashboardTables

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="SMIP Recommendation Overview",
    layout="wide"
)

with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

loader = DataLoader()

# --------------------------------------------------
# Load Data
# --------------------------------------------------
market_scores = loader.market_scores()
ranking = loader.topsis_ranking()
weighted = loader.weighted_data()
recommendation = loader.recommendation()
npv = loader.npv()
irr = loader.irr()
payback = loader.payback()

# --------------------------------------------------
# Executive Header
# --------------------------------------------------
st.title("Executive Overview")
st.caption("Executive summary of the market entry assessment combining MCDA market attractiveness and financial feasibility.")

# ==================================================
# 1. Executive Recommendation & Core KPI Block
# ==================================================
if recommendation.empty:
    st.warning("Recommendation data unavailable.")
else:
    top_market = recommendation.iloc[0]
    badge, _ = recommendation_badge(top_market["recommendation"])
    total_markets = len(recommendation)
    market_rank = int(top_market["rank"]) if "rank" in top_market else 1

    executive_summary = (
        f"{top_market['country_name']} ranks "
        f"#{market_rank} among {total_markets} evaluated markets "
        f"and achieved the highest overall investment score "
        f"({top_market['investment_score']:.3f}). "
        f"The recommendation is supported by "
        f"an estimated NPV of {top_market['npv']:,.0f} "
        f"with an IRR of {top_market['irr']:.2f}% "
        f"and an expected payback period of "
        f"{top_market['payback_period']:.2f} years."
    )

    strengths = []
    if top_market["market_score"] >= recommendation["market_score"].median():
        strengths.append("strong market attractiveness")
    if top_market["npv"] == recommendation["npv"].max():
        strengths.append("highest projected NPV")
    if top_market["irr"] == recommendation["irr"].max():
        strengths.append("highest projected IRR")
    if top_market["payback_period"] == recommendation["payback_period"].min():
        strengths.append("fastest capital recovery")

    if strengths:
        strengths_text = ", ".join(strengths[:-1]) + (f" and {strengths[-1]}" if len(strengths) > 1 else strengths[0])
    else:
        strengths_text = "balanced financial performance"

    total_unique_markets = recommendation["country"].nunique()
    priority_count = (recommendation["recommendation"] == "Priority Entry").sum()
    strong_count = (recommendation["recommendation"] == "Strong Candidate").sum()
    average_score = recommendation["investment_score"].mean()

    left_wall, right_wall = st.columns([1.2, 1])

    with left_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">PRIMARY SELECTION</div>', unsafe_allow_html=True)
        st.markdown(f"""
<div style="font-size: 3rem; font-weight: 900; color: #0f172a; letter-spacing: -0.04em; line-height: 1.1; margin-bottom: 0.5rem;">{top_market["country_name"]}</div>

**Recommendation Tier:** {top_market["recommendation"]}  
**Investment Score Baseline:** {top_market['investment_score']:.3f}

---

{executive_summary}

*Key structural strengths identified:* **{strengths_text}**.
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right_wall:
        st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
        
        st.markdown('<div class="institutional-header">Portfolio Summary Framework</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Priority Entry Markets</span><span class="corporate-value">{priority_count}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Strong Candidate Markets</span><span class="corporate-value">{strong_count}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Average Investment Score</span><span class="corporate-value">{average_score:.3f}</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="institutional-header" style="margin-top: 2rem !important; margin-bottom: 1.5rem !important;">Best Financial Performance Baseline</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Net Present Value (NPV)</span><span class="corporate-value">IDR {top_market["npv"]:,.0f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Internal Rate of Return (IRR)</span><span class="corporate-value">{top_market["irr"]:.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Expected Payback Period</span><span class="corporate-value">{top_market["payback_period"]:.2f} Years</span></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# 2. Evaluation Graph & Result Summary
# ==================================================
if not recommendation.empty:
    st.markdown('<div class="corporate-section-title">🔍 Executive Analysis & Evaluation</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Integration breakdown of final market investment selection ranking index</div>', unsafe_allow_html=True)
    
    DashboardCharts.horizontal_bar_chart(
        df=recommendation.sort_values("investment_score", ascending=False),
        x="investment_score",
        y="country_name",
        title="Overall Investment Score"
    )
    
    sub_col_left, sub_col_right = st.columns([1, 1.2])
    
    with sub_col_left:
        highest_market = recommendation.iloc[0]
        lowest_market = recommendation.iloc[-1]
        average_score = recommendation["investment_score"].mean()
        score_gap = highest_market["investment_score"] - lowest_market["investment_score"]
        positive_npv = (recommendation["npv"] > 0).sum()
        average_irr = recommendation["irr"].mean()
        average_payback = recommendation["payback_period"].mean()
        
        st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">📋 Executive Findings</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Overall Strategic Leader</span><span class="corporate-value">{highest_market["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Leader Investment Score</span><span class="corporate-value">{highest_market["investment_score"]:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average Score</span><span class="corporate-value">{average_score:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Score Gap (Leader vs Lowest)</span><span class="corporate-value">{score_gap:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Positive NPV Markets</span><span class="corporate-value">{positive_npv}/{len(recommendation)}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average IRR</span><span class="corporate-value">{average_irr:.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Portfolio Average Payback</span><span class="corporate-value">{average_payback:.2f} Years</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with sub_col_right:
        st.markdown('<div class="horizon-text-block">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
        leader = recommendation.iloc[0]
        runner_up = recommendation.iloc[1]
        last = recommendation.iloc[-1]
        
        st.markdown(f"""
The integrated investment model identifies **{leader['country_name']}** as the preferred market for entry, achieving the highest overall investment score of **{leader['investment_score']:.3f}**.

The difference between **{leader['country_name']}** and **{runner_up['country_name']}** demonstrates the advantage created by combining market attractiveness with financial feasibility instead of relying solely on MCDA rankings.

All evaluated countries currently generate positive Net Present Value under the base-case assumptions, indicating that each market is financially feasible. However, **{last['country_name']}** ranks lowest after integrating both strategic and financial criteria, suggesting comparatively weaker investment attractiveness.
""")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Key Findings</div>', unsafe_allow_html=True)
    st.markdown(f"""
• **{leader['country_name']}** is identified as the recommended market for entry with the highest integrated investment score (**{leader['investment_score']:.3f}**).
• **{runner_up['country_name']}** ranks as the strongest alternative investment opportunity based on combined strategic and financial performance.
• **{positive_npv} of {len(recommendation)}** evaluated markets generate positive Net Present Value under the base-case assumptions.
• The current portfolio contains **{priority_count} Priority Entry** market(s) and **{strong_count} Strong Candidate** market(s).
• Final recommendations are derived from the weighted integration of market attractiveness, NPV, IRR and payback period, providing a balanced assessment of strategic potential and investment feasibility.
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# 3. High-Level Financial & Strategic Baselines
# ==================================================
if not npv.empty and not irr.empty and not payback.empty:
    st.markdown('<div class="corporate-section-title">💵 Financial Performance Baseline</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Deep dive comparative assessment of baseline capital efficiency metrics</div>', unsafe_allow_html=True)
    
    financial = npv.merge(irr, on=["country", "country_name"]).merge(payback, on=["country", "country_name"])
    best_npv = financial.loc[financial["npv"].idxmax()]
    best_irr = financial.loc[financial["irr"].idxmax()]
    best_payback = financial.loc[financial["payback_period"].idxmin()]
    
    DashboardCharts.bar_chart(
        df=financial.sort_values("npv", ascending=False),
        x="country_name",
        y="npv",
        title="Net Present Value by Market"
    )
    
    fin_sub_left, fin_sub_right = st.columns([1, 1.2])
    
    with fin_sub_left:
        st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">💵 Financial Highlights</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest NPV Market</span><span class="corporate-value">{best_npv["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Projected Value Asset NPV</span><span class="corporate-value">IDR {best_npv["npv"]:,.0f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest IRR Market</span><span class="corporate-value">{best_irr["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Efficiency Internal Rate IRR</span><span class="corporate-value">{best_irr["irr"]:.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Fastest Capital Recovery Asset</span><span class="corporate-value">{best_payback["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Expected Payback Horizon</span><span class="corporate-value">{best_payback["payback_period"]:.2f} Years</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average NPV</span><span class="corporate-value">IDR {financial["npv"].mean():,.0f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Average IRR</span><span class="corporate-value">{financial["irr"].mean():.2f}%</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Portfolio Average Payback</span><span class="corporate-value">{financial["payback_period"].mean():.2f} Years</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with fin_sub_right:
        st.markdown('<div class="horizon-text-block">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Financial Interpretation</div>', unsafe_allow_html=True)
        positive_npv_count = (financial["npv"] > 0).sum()
        
        st.markdown(f"""
The financial assessment indicates that **{positive_npv_count} of {len(financial)}** evaluated markets generate a positive Net Present Value under the base-case assumptions.

Among all evaluated markets, **{best_npv['country_name']}** delivers the greatest shareholder value through the highest projected NPV. The same market also demonstrates strong investment efficiency, while **{best_payback['country_name']}** achieves the fastest capital recovery.

Overall, the portfolio exhibits attractive financial characteristics, supporting expansion into the highest-ranked markets identified by the integrated recommendation framework.
""")
        st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("View Detailed Financial Metrics"):DashboardTables.dataframe(financial)

# ==================================================
# 4. Market Priority (Chart 3 of 3)
# ==================================================
if not market_scores.empty:
    st.markdown('<div class="corporate-section-title">🎯 Strategic Market Priority Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Multi-criteria decision analysis summary across strategic weighting criteria</div>', unsafe_allow_html=True)
    
    DashboardCharts.horizontal_bar_chart(
        df=market_scores.sort_values("market_priority_score", ascending=False),
        x="market_priority_score",
        y="country_name",
        title="MCDA Market Priority Score"
    )
    
    market_sub_left, market_sub_right = st.columns([1, 1.2])
    
    with market_sub_left:
        highest_market = market_scores.loc[
            market_scores["market_priority_score"].idxmax()
        ]
        average_priority = market_scores["market_priority_score"].mean()
        
        st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
        st.markdown('<div class="institutional-header">🎯 Market Highlights</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest Priority Country</span><span class="corporate-value">{highest_market["country_name"]}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Highest Priority Score</span><span class="corporate-value">{highest_market["market_priority_score"]:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">Portfolio Strategic Average</span><span class="corporate-value">{average_priority:.3f}</span></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none; margin-bottom: 0px;"><span class="corporate-label">Total Markets Evaluated</span><span class="corporate-value">{len(market_scores)}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with market_sub_right:
        st.markdown('<div class="horizon-text-block">', unsafe_allow_html=True)
        st.markdown('<div class="narrative-title">Interpretation</div>', unsafe_allow_html=True)
        st.markdown(f"""
Market Priority Scores summarize the multi-criteria decision analysis by combining all weighted strategic indicators into a single attractiveness measure.

**{highest_market['country_name']}** achieved the highest overall strategic attractiveness before incorporating financial metrics. These scores represent the strategic foundation of the final investment recommendation model.
""")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No market score available.")

st.divider()

# ==================================================
# 5. Appendix
# ==================================================
with st.expander("Appendix: Weighted Indicator Dataset"):
    if not weighted.empty:
        summary = weighted[
            [
                "country_name",
                "indicator_name",
                "dimension",
                "normalized_score"
            ]
        ]

        DashboardTables.table_with_download(
            summary,
            filename="weighted_market_data.csv"
        )
    else:
        st.info("Dataset unavailable.")