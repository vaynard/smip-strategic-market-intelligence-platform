import streamlit as st
import yaml
from pathlib import Path
from components.tables import DashboardTables

with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="SMIP Assumptions",
    layout="wide"
)
# ==================================================
# Load Configuration
# ==================================================
CONFIG = Path("config")

with open(CONFIG / "countries.yaml", "r") as f:
    countries = yaml.safe_load(f)

with open(CONFIG / "weights.yaml", "r") as f:
    weights = yaml.safe_load(f)

with open(CONFIG / "financial.yaml", "r") as f:
    financial = yaml.safe_load(f)

with open(CONFIG / "recommendation.yaml", "r") as f:
    recommendation = yaml.safe_load(f)

with open(CONFIG / "indicators.yaml", "r") as f:
    indicators = yaml.safe_load(f)

# ==================================================
# Header
# ==================================================
st.title("Model Assumptions")
st.caption("Review the assumptions, configuration parameters, weighting framework, and financial inputs used throughout the Strategic Market Intelligence Platform (SMIP).")
st.divider()

# ==================================================
# Executive Summary
# ==================================================
st.markdown('<div class="corporate-section-title">🏆 Configuration Baseline Summary</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">High-level model parameter thresholds and operational scope limits loaded from system variables</div>', unsafe_allow_html=True)

# 4-Column Grid layout untuk penempatan st.metric bawaan yang sudah dihias CSS
metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("Countries", len(countries["countries"]))
metric2.metric("Indicators", len(indicators["indicators"]))
metric3.metric("Dimensions", len(weights["dimensions"]))
metric4.metric("Forecast Horizon", f"{financial['project_years']} Years")

st.markdown(f"""
This page documents the assumptions and configuration parameters that
drive the Strategic Market Intelligence Platform (SMIP).

The framework currently evaluates **{len(countries['countries'])} candidate markets**
using **{len(indicators['indicators'])} economic indicators**
grouped into **{len(weights['dimensions'])} strategic dimensions**.

All market rankings, financial projections, and investment
recommendations presented throughout the dashboard are generated using
the assumptions documented on this page with the intent to ensuring transparency,
reproducibility, and interpretability of the analytical results.
""")

st.divider()

# ==================================================
# Market Evaluation Assumptions
# ==================================================
if "dimensions" in weights:
    st.markdown('<div class="corporate-section-title">📊 Market Evaluation Assumptions</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Configurable strategic business dimensions and their associated weights allocation mapping</div>', unsafe_allow_html=True)

    dimension_rows = []
    for dimension, config in weights["dimensions"].items():
        dimension_rows.append(
            {
                "Strategic Dimension": dimension.replace("_", " ").title(),
                "Weight": f"{config['weight']:.0%}",
                "Business Objective": config["rationale"]
            }
        )

    st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
    st.markdown('<div class="institutional-header">📋 Strategic Dimension Weights Framework</div>', unsafe_allow_html=True)
    DashboardTables.dataframe(dimension_rows)
    st.markdown('</div>', unsafe_allow_html=True)

    total_weight = sum(
        config["weight"]
        for config in weights["dimensions"].values()
    )

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
The market evaluation framework applies **Multi-Criteria Decision
Analysis (MCDA)** to combine multiple strategic dimensions into a single
market attractiveness score.

Each business dimension is assigned a configurable importance weight,
reflecting its relative contribution to the overall market evaluation.
The current framework allocates a total weight of **{total_weight:.0%}**
across all strategic dimensions.

The golas of using this configurable weights is to enable the evaluation model to remain
transparent and adaptable while ensuring that every market is assessed
consistently under the same decision criteria.
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Indicator Processing Assumptions
# ==================================================
if "indicators" in indicators:
    st.markdown('<div class="corporate-section-title">📊 Indicator Processing Assumptions</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Predefined business rules mapping aggregation, normalization, and optimization direction for foundational economic variables</div>', unsafe_allow_html=True)

    indicator_rows = []
    for indicator_code, config in indicators["indicators"].items():
        indicator_rows.append(
            {
                "Indicator": config["name"],
                "Dimension": config["dimension"],
                "Aggregation": config["aggregation"].title(),
                "Optimization": config["direction"].title(),
                "Normalization": config["normalization"].replace("_", " ").title()
            }
        )

    st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
    st.markdown('<div class="institutional-header">📋 Preprocessing and Normalization Pipeline Mapping</div>', unsafe_allow_html=True)
    DashboardTables.dataframe(indicator_rows)
    st.markdown('</div>', unsafe_allow_html=True)

    aggregation_summary = {}
    direction_summary = {"Benefit": 0, "Cost": 0}

    for _, config in indicators["indicators"].items():
        aggregation_summary[config["aggregation"]] = aggregation_summary.get(config["aggregation"], 0) + 1
        direction_summary[config["direction"].title()] += 1

    aggregation_text = ", ".join(
        [f"**{count}** using *{method.replace('_',' ').title()}*" for method, count in aggregation_summary.items()]
    )

    st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
    st.markdown(f"""
Before market evaluation, every indicator is processed using
predefined business rules to ensure consistency across countries.

The current framework applies **Min-Max normalization** to transform
heterogeneous indicators onto a comparable scale while preserving
relative performance.

Historical observations are aggregated according to indicator-specific
business logic, with {aggregation_text}.

Among the evaluated indicators,
**{direction_summary['Benefit']}** are treated as **Benefit**
criteria (higher values preferred), while
**{direction_summary['Cost']}** are treated as **Cost**
criteria (lower values preferred).

""")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Financial Modeling Assumptions
# ==================================================
if "project_years" in financial:
    st.markdown('<div class="corporate-section-title">💵 Financial Modeling Assumptions</div>', unsafe_allow_html=True)
    st.markdown('<div class="corporate-section-subtitle">Deep dive overview of configurable baseline investment inputs, margins, and horizon parameters</div>', unsafe_allow_html=True)

    financial_rows = [
        {"Parameter": "Currency", "Value": financial["currency"]},
        {"Parameter": "Forecast Horizon", "Value": f"{financial['project_years']} Years"},
        {"Parameter": "Initial Investment", "Value": f"{financial['initial_investment']:,.0f}"},
        {"Parameter": "Discount Rate", "Value": f"{financial['discount_rate']:.0%}"},
        {"Parameter": "Base Revenue", "Value": f"{financial['base_revenue']:,.0f}"},
        {"Parameter": "Base Revenue Growth", "Value": f"{financial['base_growth_rate']:.0%}"},
        {"Parameter": "Operating Margin", "Value": f"{financial['operating_margin']:.0%}"},
        {"Parameter": "Tax Rate", "Value": f"{financial['tax_rate']:.0%}"}
    ]

    st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
    st.markdown('<div class="institutional-header">📋 Capital Budgeting Baseline Assumptions</div>', unsafe_allow_html=True)
    DashboardTables.dataframe(financial_rows)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Revenue Model
# ==================================================
st.markdown('<div class="corporate-section-title">📈 Revenue Forecasting Architecture</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Market-responsive forecasting multipliers combining strategic attractiveness indices and purchasing power</div>', unsafe_allow_html=True)

revenue_model = [
    {"Model Component": "Base Revenue", "Configuration": f"{financial['base_revenue']:,.0f}"},
    {"Model Component": "Revenue Score", "Configuration": "Weighted Composite Score"},
    {"Model Component": "TOPSIS Weight", "Configuration": f"{financial['revenue_score_weights']['topsis']:.0%}"},
    {"Model Component": "Population Weight", "Configuration": f"{financial['revenue_score_weights']['population']:.0%}"},
    {"Model Component": "Income Weight", "Configuration": f"{financial['revenue_score_weights']['income']:.0%}"},
    {"Model Component": "Market Multiplier", "Configuration": f"{financial['market_multiplier']['minimum']:.2f}x – {financial['market_multiplier']['maximum']:.2f}x"},
    {"Model Component": "Base Growth", "Configuration": f"{financial['base_growth_rate']:.0%}"},
    {"Model Component": "GDP Growth Adjustment", "Configuration": f"{financial['growth_adjustment']['gdp_growth_weight']:.0%}"}
]

st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
st.markdown('<div class="institutional-header">📋 Revenue Model Component Rules</div>', unsafe_allow_html=True)
DashboardTables.dataframe(revenue_model)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
st.markdown("""
Projected revenue is generated using a market-responsive forecasting
model rather than a fixed annual growth assumption.

Each candidate market receives a **Revenue Score**, calculated as a
weighted combination of:
- Market attractiveness (TOPSIS)
- Population potential
- Purchasing power (GDP per capita)

Population and GDP per capita are first transformed using logarithmic
scaling before Min-Max normalization to reduce the influence of extreme
values while preserving relative differences between markets.

The resulting Revenue Score determines a market multiplier ranging from
**0.80× to 1.20×**, which adjusts the baseline revenue according to the
relative attractiveness of each market.

Annual revenue growth is then projected dynamically by combining the
configured base growth rate with country-specific GDP growth through the
GDP growth adjustment factor.

This methodology produces revenue forecasts that reflect both structural
market characteristics and expected macroeconomic performance, providing
a more realistic basis for subsequent NPV, IRR, and Payback Period
calculations.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Investment Decision Model
# ==================================================
st.markdown('<div class="corporate-section-title">⚖️ Investment Decision Model</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Integrated priority weighting matrix balancing strategic market screening and capital feasibility thresholds</div>', unsafe_allow_html=True)

criteria_rows = []
for criterion, config in recommendation["criteria"].items():
    criteria_rows.append(
        {
            "Evaluation Criterion": criterion,
            "Weight": f"{config['weight']:.0%}",
            "Business Rationale": config["rationale"]
        }
    )

st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
st.markdown('<div class="institutional-header">📋 Consolidated Prioritization Scoring Framework</div>', unsafe_allow_html=True)
DashboardTables.dataframe(criteria_rows)
st.markdown('</div>', unsafe_allow_html=True)

total_weight = sum(
    config["weight"]
    for config in recommendation["criteria"].values()
)
framework_name = recommendation["framework"]["name"]
methodology = recommendation["framework"]["methodology"]

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
st.markdown(f"""
The **{framework_name}** applies the
**{methodology}** methodology to combine market attractiveness and
financial performance into a single investment score.

The model allocates a total weight of **{total_weight:.0%}** across four
decision criteria:
- Market Attractiveness
- Value Creation
- Return Profile
- Capital Recovery

Each criterion contributes according to its configured importance,
ensuring that investment recommendations balance strategic opportunity,
expected profitability, and investment risk using a transparent and
reproducible scoring framework.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Configuration Summary
# ==================================================
st.subheader("Configuration Summary")
st.caption("All analytical parameters are externalized through YAML configuration files, enabling transparent, reproducible, and easily maintainable model configuration.")

configuration = [
    {"Configuration File": "countries.yaml", "Purpose": "Defines candidate markets included in the evaluation."},
    {"Configuration File": "indicators.yaml", "Purpose": "Defines indicators, dimensions, aggregation rules, normalization, and optimization direction."},
    {"Configuration File": "weights.yaml", "Purpose": "Stores strategic dimension weights used in the MCDA evaluation."},
    {"Configuration File": "financial.yaml", "Purpose": "Contains financial modeling assumptions, projection parameters, and market multipliers."},
    {"Configuration File": "recommendation.yaml", "Purpose": "Defines the investment score calculation and recommendation thresholds."}
]

st.markdown('<div class="horizon-data-block">', unsafe_allow_html=True)
st.markdown('<div class="institutional-header">📋 File Architecture External Registry</div>', unsafe_allow_html=True)
DashboardTables.dataframe(configuration)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="corporate-narrative-box">', unsafe_allow_html=True)
st.markdown('<div class="narrative-title">Result Summary</div>', unsafe_allow_html=True)
st.markdown("""
SMIP separates analytical logic from business configuration by storing
all evaluation parameters in external YAML configuration files.

This configuration-driven architecture provides several advantages:
- Transparent business assumptions
- Easy adjustment without source code modification
- Consistent evaluation across all candidate markets
- Improved reproducibility of analytical results
- Simplified maintenance and future framework expansion

This approach allows decision-makers to update strategic priorities,
financial assumptions, and evaluation criteria while preserving the
integrity of the analytical pipeline.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Why These Assumptions?
# ==================================================
st.markdown('<div class="corporate-section-title">💡 Standardized Validation Rationale</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Objective structural baseline boundaries minimizing individual interpretation bias</div>', unsafe_allow_html=True)

st.markdown("""
The assumptions documented throughout this page provide a standardized
foundation for evaluating every candidate market under identical
conditions.

Using common assumptions ensures that differences in market rankings
and investment recommendations are driven by underlying economic and
financial performance rather than inconsistent analytical settings.

All these assumptions can be modified to reflect different strategic priorities
or investment scenarios while maintaining a consistent and scalable configuration during
evaluations with the intent to help user to produce objective, comparable, and reproducible
results.
""")