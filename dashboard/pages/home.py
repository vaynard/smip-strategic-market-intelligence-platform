import streamlit as st
import os
from utils.loader import DataLoader

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Strategic Market Intelligence Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("dashboard/assets/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


loader = DataLoader()
ranking = loader.topsis_ranking()
weighted = loader.weighted_data()
dimension_scores = loader.dimension_scores()

# ==================================================
# Header
# ==================================================
st.title("🌍 Strategic Market Intelligence Platform")
st.subheader("Strategic Market Entry Decision Support Dashboard")

st.markdown(
    """
The **Strategic Market Intelligence Platform (SMIP)** is an end-to-end
decision support system that evaluates international market entry
opportunities by integrating economic indicators, multi-criteria
decision analysis (MCDA), TOPSIS ranking, and financial feasibility
analysis into a unified analytical workflow.

The platform transforms raw macroeconomic data into transparent,
reproducible investment recommendations for strategic market
prioritization.
"""
)
st.divider()

# ==================================================
# Project Statistics
# ==================================================
st.markdown('<div class="corporate-section-title">📊 Project Overview & Operational Scale</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Key architectural indicators mapping the scale of the decision support dataset</div>', unsafe_allow_html=True)

# 4-Column Grid layout untuk penempatan st.metric bawaan yang sudah dihias CSS
metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("Candidate Markets", ranking["country_name"].nunique())
metric2.metric("Strategic Indicators", weighted["indicator_name"].nunique())
metric3.metric("Evaluation Dimensions", dimension_scores["dimension"].nunique())
metric4.metric("Dashboard Pages", 6)

st.divider()

# ==================================================
# Core Capabilities
# ==================================================
st.markdown('<div class="corporate-section-title">🛡️ Core System Capabilities</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Dual-track division architecture separating advanced data analytics from capital budgeting models</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">📊 Decision Analytics</div>', unsafe_allow_html=True)
    st.markdown("""
- Automated World Bank data collection
- Data quality validation
- Historical indicator aggregation
- MCDA weighted market evaluation
- TOPSIS market ranking
- Executive reporting
""")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">💰 Financial Evaluation</div>', unsafe_allow_html=True)
    st.markdown("""
- Revenue projection model
- Dynamic market multipliers
- Cash flow forecasting
- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period & Sensitivity Analysis
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Dashboard Navigation (Redesign to Corporate Strips)
# ==================================================
st.markdown('<div class="corporate-section-title">📑 Dashboard Modules Reference</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Direct systemic layout mapping page scopes and functional evaluation purposes</div>', unsafe_allow_html=True)

st.markdown('<div class="luxury-text-box">', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">🏠 Home</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">Project overview and navigation</span></div>', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">📈 Executive Overview</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">Executive KPIs and investment summary</span></div>', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">🌍 Market Analysis</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">MCDA evaluation and TOPSIS market ranking</span></div>', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">💰 Financial Analysis</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">Financial feasibility and investment evaluation</span></div>', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip"><span class="corporate-label">⚙️ Methodology</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">Analytical framework and processing pipeline</span></div>', unsafe_allow_html=True)
st.markdown(f'<div class="corporate-data-strip" style="border-bottom: none;"><span class="corporate-label">📑 Assumptions</span><span class="corporate-value" style="font-size:0.95rem; font-weight:500; color:#475569;">Model assumptions and configuration</span></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Analytical Workflow (Redesign to Uniform Connected Steps)
# ==================================================
st.markdown('<div class="corporate-section-title">🔄 End-to-End Analytical Workflow</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Linear sequence pipeline translating raw macroeconomic data strings into core executive metrics</div>', unsafe_allow_html=True)

# Diagram alur interaktif dengan struktur ukuran kotak yang seragam 100%
st.markdown("""
<div class="workflow-grid-wrapper">
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 01</span>
            <span class="workflow-step-text">World Bank Data Collection</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 02</span>
            <span class="workflow-step-text">Data Enrichment</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 03</span>
            <span class="workflow-step-text">Data Quality Validation</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 04</span>
            <span class="workflow-step-text">Historical Aggregation</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 05</span>
            <span class="workflow-step-text">Indicator Normalization</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 06</span>
            <span class="workflow-step-text">MCDA Weighted Scoring</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 07</span>
            <span class="workflow-step-text">TOPSIS Market Ranking</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule">
        <div>
            <span class="workflow-phase-badge">STAGE 08</span>
            <span class="workflow-step-text">Financial Modeling</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>
    <div class="workflow-uniform-capsule final-stage">
        <div>
            <span class="workflow-phase-badge final-badge">OUTPUT RESOLUTION</span>
            <span class="workflow-step-text">Executive Decision Support Dashboard</span>
        </div>
        <span class="workflow-arrow-indicator">→</span>
    </div>

</div>
""", unsafe_allow_html=True)

st.divider()
# ==================================================
# Technology Stack
# ==================================================
st.markdown('<div class="corporate-section-title">🛠️ System Technology Stack</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">Core baseline software stacks and frameworks driving calculation pipeline validation</div>', unsafe_allow_html=True)

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Data Engineering</div>', unsafe_allow_html=True)
    st.markdown("""
- Python
- Pandas
- NumPy
- Requests
- YAML
""")
    st.markdown('</div>', unsafe_allow_html=True)

with tech2:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Decision Analytics</div>', unsafe_allow_html=True)
    st.markdown("""
- MCDA
- TOPSIS
- NumPy Financial
- Financial Modeling
""")
    st.markdown('</div>', unsafe_allow_html=True)

with tech3:
    st.markdown('<div class="corporate-narrative-box" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="narrative-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown("""
- Streamlit
- Plotly
- Interactive Visualization
- Executive Reporting
""")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==================================================
# Project Resources
# ==================================================
st.markdown('<div class="corporate-section-title">📂 Infrastructure Project Resources</div>', unsafe_allow_html=True)
st.markdown('<div class="corporate-section-subtitle">External integration gateways for system documents, version controls, and profiles</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("💻 GitHub Repository", "https://google.com")
with col2:
    st.link_button("💼 LinkedIn", "https://google.com")
with col3:
    st.link_button("📄 Project Documentation", "https://google.com")

st.caption("Replace the placeholder links with your GitHub repository, LinkedIn profile, and project documentation.")
st.divider()