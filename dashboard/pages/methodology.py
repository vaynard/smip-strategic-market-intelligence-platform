import streamlit as st

# --------------------------------------------------
# External CSS Loader
# --------------------------------------------------
with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="SMIP Methodology",
    layout="wide"
)
# ==================================================
# Header
# ==================================================
st.title("Methodology")
st.caption("Understand the analytical framework, data processing pipeline, and decision methodology used by the Strategic Market Intelligence Platform (SMIP).")

# ==================================================
# Executive Summary (Redesign to Regal Split Wall)
# ==================================================
left_wall, right_wall = st.columns([1.2, 1])

with left_wall:
    st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
    st.markdown('<div class="institutional-header">METHODOLOGY FRAMEWORK</div>', unsafe_allow_html=True)
    st.markdown("""
The **Strategic Market Intelligence Platform (SMIP)** is an end-to-end
decision-support framework designed to evaluate international market
entry opportunities using objective macroeconomic indicators,
multi-criteria decision analysis, and financial feasibility assessment.

Rather than relying on a single economic metric, SMIP integrates
multiple strategic dimensions into a transparent and repeatable
evaluation process. The framework combines data engineering,
decision analytics, and capital budgeting techniques to support
evidence-based market selection and investment prioritization.
""")
    st.markdown('</div>', unsafe_allow_html=True)

with right_wall:
    st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
    
    st.markdown('<div class="institutional-header">Methodological Components</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="corporate-data-strip"><span class="corporate-label">Total Evaluation Indicators</span><span class="corporate-value">25</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-data-strip"><span class="corporate-label">Strategic Dimensions</span><span class="corporate-value">5</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-data-strip"><span class="corporate-label">Analytical Pipeline Stages</span><span class="corporate-value">9</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">Core Decision Methods</span><span class="corporate-value">MCDA + TOPSIS</span></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
# ==================================================
# End-to-End Analytical Workflow
# ==================================================
st.markdown('<div class="corporate-section-title">End-to-End Analytical Workflow</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">SMIP Workflow and data processing framework and methodology</div>', unsafe_allow_html=True)

col_stage1, col_stage2 = st.columns(2)

with col_stage1:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">1. Data Collection</div>', unsafe_allow_html=True)
    st.markdown("""
Economic indicators are collected directly from the **World Bank Open Data API**
covering multiple countries, indicators, and historical observations.

**Purpose**
- Acquire reliable macroeconomic data
- Ensure standardized international coverage
- Maintain reproducible data acquisition
""")
    st.markdown('</div>', unsafe_allow_html=True)

with col_stage2:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">2. Data Enrichment</div>', unsafe_allow_html=True)
    st.markdown("""
Each indicator is enriched using a metadata configuration that defines
its analytical role within the evaluation framework.

Metadata includes:
- Business dimension
- Indicator description
- Benefit or Cost classification
- Aggregation strategy
- Normalization strategy
- Data source

This standardization enables consistent downstream processing.
""")
    st.markdown('</div>', unsafe_allow_html=True)

col_stage3, col_stage4 = st.columns(2)

with col_stage3:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">3. Data Quality Validation</div>', unsafe_allow_html=True)
    st.markdown("""
The platform validates collected data before analysis to improve
data reliability and consistency.

Validation includes:
- Missing value detection
- Duplicate record detection
- Numeric validation
- Business rule verification
- Source completeness checks
""")
    st.markdown('</div>', unsafe_allow_html=True)

with col_stage4:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">4. Historical Aggregation</div>', unsafe_allow_html=True)
    st.markdown("""
Historical observations are transformed into representative business
metrics according to indicator-specific aggregation rules.

Examples include:
- GDP Growth → Five-year average
- Inflation → Five-year average
- GDP per Capita → Latest available value
- Population → Latest available value
- Internet Usage → Latest available value

This ensures each indicator reflects an appropriate business perspective.
""")
    st.markdown('</div>', unsafe_allow_html=True)


col_stage5, col_stage6 = st.columns(2)

with col_stage5:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">5. Indicator Normalization</div>', unsafe_allow_html=True)
    st.markdown("""
Indicators use different measurement units and scales. To enable
meaningful comparison, values are transformed onto a common scale using
**Min-Max normalization**.

The framework supports:
- Benefit indicators (higher values preferred)
- Cost indicators (lower values preferred)

Normalization preserves the relative performance of each country while
making heterogeneous indicators directly comparable.
""")
    st.markdown('</div>', unsafe_allow_html=True)

with col_stage6:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">6. Weighted Scoring</div>', unsafe_allow_html=True)
    st.markdown("""
Normalized indicators are multiplied by configurable weights that
represent their strategic importance.

The weighting process occurs at two levels:
- Indicator weights
- Business dimension weights

This allows the framework to reflect different strategic priorities
while maintaining transparency.
""")
    st.markdown('</div>', unsafe_allow_html=True)

col_stage7, col_stage8 = st.columns(2)

with col_stage7:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">7. Market Evaluation</div>', unsafe_allow_html=True)
    st.markdown("""
Weighted indicators are aggregated into business dimensions before
being combined into an overall Market Priority Score.

Outputs include:
- Indicator Scores
- Dimension Scores
- Market Priority Scores
""")
    st.markdown('</div>', unsafe_allow_html=True)

with col_stage8:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">8. Market Ranking</div>', unsafe_allow_html=True)
    st.markdown("""
The Technique for Order Preference by Similarity to Ideal Solution
(TOPSIS) ranks candidate markets according to their relative closeness
to an ideal market profile.

Rather than evaluating a single indicator, TOPSIS simultaneously
considers every weighted criterion to produce an overall ranking.
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title" style="color:#0f172a;">9. Financial Evaluation</div>', unsafe_allow_html=True)
st.markdown("""
Financial feasibility complements market attractiveness through
capital budgeting techniques.

The framework evaluates:
- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period
- Sensitivity Analysis

These metrics are integrated with the market evaluation to produce the
final investment recommendation.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Evaluation Framework
# ==================================================
st.markdown('<div class="corporate-section-title">🎯 Strategic Evaluation Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Multidimensional screening matrix evaluating international asset prioritization nodes</div>', unsafe_allow_html=True)

framework = """

| Strategic Dimension | Business Objective | Example Indicators |
|----------------------|-------------------|--------------------|
| **Market Opportunity** | Measure market size and long-term growth potential. | GDP, GDP Growth, Population |
| **Economic Stability** | Assess macroeconomic resilience and investment risk. | Inflation, Unemployment, Exchange Stability |
| **Business Environment** | Evaluate the ease of operating and expanding within the market. | Ease of Doing Business, Regulatory Quality |
| **Infrastructure & Digital Readiness** | Measure the country's physical and digital capabilities supporting business operations. | Internet Usage, Mobile Subscriptions, Logistics |
| **Market Accessibility** | Evaluate how easily foreign firms can enter and compete within the market. | Trade Openness, FDI, Market Access Indicators |
"""

st.markdown(framework)

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
st.markdown("""
Rather than relying on a single economic indicator, SMIP evaluates
markets from multiple strategic perspectives.

Each dimension captures a different component of market attractiveness,
allowing the framework to balance growth potential, economic stability,
operational conditions, infrastructure readiness, and accessibility.

This multidimensional approach reduces the risk of selecting markets
based solely on one strong indicator while overlooking weaknesses in
other strategically important areas.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Why This Framework?
# ==================================================
st.markdown('<div class="corporate-section-title">💡 System Architecture Rationale</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Core investment philosophy tracking quantitative reproducibility and data-driven risk management</div>', unsafe_allow_html=True)

st.markdown("""
The Strategic Market Intelligence Platform (SMIP) integrates
macroeconomic analysis, multi-criteria decision analysis, and financial
evaluation into a unified decision-support framework for international
market entry.

Rather than relying on subjective judgement or isolated economic
indicators, the framework evaluates candidate markets using a transparent,
repeatable, and data-driven methodology. Every recommendation can be
traced from the final investment score back through financial metrics,
market rankings, business dimensions, normalized indicators, and the
original economic data sources.

By combining **market attractiveness** with **financial feasibility**,
SMIP enables decision-makers to compare international markets
consistently while reducing analytical bias and improving confidence in
strategic investment decisions.
""")
