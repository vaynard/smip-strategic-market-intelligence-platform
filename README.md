# 🌍 Strategic Market Intelligence Platform (SMIP)

> An end-to-end decision support system for evaluating and prioritizing international market entry opportunities using Multi-Criteria Decision Analysis (MCDA), TOPSIS, and financial feasibility analysis.

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)](#)
[![World%20Bank](https://img.shields.io/badge/Data-World%20Bank-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</p>

<p align="center">

🌐 **Live Demo:** www.google.com

👤 **LinkedIn:** https://www.linkedin.com/in/roiki-then/

</p>

---

## Overview

The **Strategic Market Intelligence Platform (SMIP)** is an end-to-end analytics platform designed to support international market entry decisions through a transparent, data-driven evaluation framework.

Rather than relying on subjective judgement or isolated economic indicators, SMIP integrates external macroeconomic data, multi-criteria decision analysis, and financial feasibility assessment into a unified decision-support workflow.

The platform automatically retrieves public economic indicators from the **World Bank Open Data API**, validates and transforms the data, evaluates market attractiveness using **Multi-Criteria Decision Analysis (MCDA)** and **TOPSIS**, and estimates investment feasibility through capital budgeting techniques including **Net Present Value (NPV)**, **Internal Rate of Return (IRR)**, **Payback Period**, and **Sensitivity Analysis**.

The result is an interactive executive dashboard that enables decision makers to compare international markets using consistent assumptions, transparent scoring methodologies, and configurable business rules.

---

## Key Features

- 🌍 Automated multi-country data collection from the World Bank Open Data API
- ✅ Configurable data validation and quality assessment pipeline
- 📊 Multi-Criteria Decision Analysis (MCDA) for market evaluation
- 🏆 TOPSIS-based market prioritization and ranking
- 💰 Financial feasibility analysis using NPV, IRR, Payback Period, and Sensitivity Analysis
- 📈 Five-year revenue and cash flow forecasting
- ⚙️ YAML-driven configuration for indicators, weights, financial assumptions, and recommendation models
- 📑 Interactive executive dashboard built with Streamlit
- 📥 Downloadable datasets and analytical outputs for transparency and auditability

---

## Dashboard

The platform is organized into six modules designed for both executive decision makers and analysts.

| Module | Purpose |
|---------|---------|
| 🏠 Home | Project overview, workflow, architecture, and navigation |
| 📈 Executive Summary | High-level strategic insights and investment highlights |
| 🌍 Market Analysis | MCDA evaluation, TOPSIS ranking, and market comparison |
| 💰 Financial Analysis | Capital budgeting, forecasting, and investment attractiveness |
| 📚 Methodology | Complete analytical framework and evaluation process |
| ⚙️ Assumptions | Business rules, weighting schemes, financial assumptions, and configuration transparency |

---

# Dashboard Preview

The dashboard provides an end-to-end decision-support workflow, from strategic market evaluation to investment feasibility analysis.

> Replace the placeholders below with screenshots from your application.

## 🏠 Home

<p align="center">
<img src="docs/images/home.png" width="900">
</p>

Provides an overview of the platform, project objectives, analytical workflow, dashboard modules, and repository links.

---

## 📈 Executive Summary

<p align="center">
<img src="docs/images/executive_summary.png" width="900">
</p>

Summarizes the overall market evaluation using executive KPIs, market rankings, financial highlights, and strategic recommendations.

---

## 🌍 Market Analysis

<p align="center">
<img src="docs/images/market_analysis.png" width="900">
</p>

Interactive market evaluation including:

- MCDA Dimension Performance
- TOPSIS Ranking
- Market Comparison
- Indicator Drill-down
- Strategic Insights

---

## 💰 Financial Analysis

<p align="center">
<img src="docs/images/financial_analysis.png" width="900">
</p>

Financial feasibility assessment including:

- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period
- Revenue Projection
- Cash Flow Forecast
- Sensitivity Analysis
- Investment Recommendation

---

## 📚 Methodology

<p align="center">
<img src="docs/images/methodology.png" width="900">
</p>

Documents the complete analytical framework, including the data pipeline, MCDA methodology, TOPSIS ranking process, and financial modeling workflow.

---

## ⚙️ Assumptions

<p align="center">
<img src="docs/images/assumptions.png" width="900">
</p>

Provides full transparency of configurable business assumptions, indicator definitions, weighting schemes, financial parameters, recommendation criteria, and evaluation rules used throughout the platform.

---

# System Architecture

The platform follows a modular analytics architecture where each stage produces validated outputs for the next stage of the workflow.

```text
                  World Bank Open Data API
                             │
                             ▼
                   Data Collection Pipeline
                             │
                             ▼
                    Data Enrichment Layer
                             │
                             ▼
                   Data Quality Validation
                             │
                             ▼
                  Historical Aggregation
                             │
                             ▼
                     Data Normalization
                             │
                             ▼
          Multi-Criteria Decision Analysis (MCDA)
                             │
                             ▼
                    TOPSIS Market Ranking
                             │
                             ▼
                 Financial Feasibility Model
                             │
                             ▼
              Interactive Streamlit Dashboard
```
---


# Analytics Workflow

SMIP follows a reproducible analytics pipeline that transforms raw macroeconomic data into actionable market entry recommendations.

```text
World Bank API
      │
      ▼
Data Collection
      │
      ▼
Data Enrichment
      │
      ▼
Data Validation
      │
      ▼
Historical Aggregation
      │
      ▼
Normalization
      │
      ▼
Weighted Scoring (MCDA)
      │
      ▼
TOPSIS Market Ranking
      │
      ▼
Financial Modeling
      │
      ▼
Interactive Dashboard
```

Each stage produces validated outputs consumed by the next stage, ensuring transparency and reproducibility throughout the decision-making process.

---

# Decision Analytics

## Multi-Criteria Decision Analysis (MCDA)

The platform evaluates candidate markets using a weighted Multi-Criteria Decision Analysis framework.

The current implementation evaluates markets across five strategic dimensions.

| Dimension | Weight | Purpose |
|------------|------:|---------|
| Market Opportunity | 30% | Market size, purchasing power, and growth potential |
| Economic Stability | 25% | Inflation, unemployment, and fiscal sustainability |
| Business Environment | 20% | Business financing and regulatory efficiency |
| Infrastructure & Digital Readiness | 15% | Digital connectivity and operational capability |
| Market Accessibility | 10% | Trade openness and investment accessibility |

Each indicator is:

- Retrieved from the World Bank API
- Validated against configurable business rules
- Aggregated using indicator-specific strategies
- Normalized to a common scale
- Weighted according to configurable YAML definitions
- Aggregated into dimension scores

This approach enables objective comparison across markets while maintaining full transparency of the evaluation methodology.

---

## TOPSIS Market Ranking

After calculating weighted dimension scores, SMIP applies the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)** to prioritize candidate markets.

Rather than selecting markets based on a single indicator, TOPSIS evaluates each country according to its distance from:

- ✅ The ideal market profile
- ❌ The least desirable market profile

The resulting **TOPSIS score** represents each country's relative closeness to the ideal solution.

Higher scores indicate markets that provide a more balanced combination of economic opportunity, stability, business environment, infrastructure, and accessibility.

---

# Financial Modeling

Strategic attractiveness alone does not determine investment decisions.

SMIP therefore complements market evaluation with a financial feasibility model that estimates the expected commercial performance of entering each market.

The financial workflow includes:

### Revenue Projection

Revenue projections combine:

- Market attractiveness (TOPSIS score)
- Population size
- GDP per capita
- GDP growth adjustment

to estimate market-specific revenue potential over a five-year planning horizon.

---

### Cash Flow Projection

Projected revenue is transformed into annual operating cash flow using configurable assumptions for:

- Operating margin
- Corporate tax rate
- Investment horizon

---

### Capital Budgeting

The projected cash flows are evaluated using standard investment metrics.

| Metric | Purpose |
|---------|---------|
| Net Present Value (NPV) | Measures expected value creation |
| Internal Rate of Return (IRR) | Measures investment profitability |
| Payback Period | Measures capital recovery speed |

---

### Sensitivity Analysis

The financial model evaluates how changes in discount rates affect project valuation.

This provides decision makers with insight into the robustness of each investment under different financing assumptions.

---

# Configuration-Driven Design

One of the core design principles of SMIP is **configuration over hard-coded logic**.

Business rules are maintained through YAML configuration files rather than embedded directly in source code.

| Configuration | Purpose |
|--------------|---------|
| indicators.yaml | Indicator metadata and validation rules |
| weights.yaml | Strategic dimension weights |
| financial.yaml | Financial assumptions and forecasting parameters |
| recommendation.yaml | Investment scoring methodology |

This design allows the evaluation framework to evolve without requiring modifications to the analytical pipeline.

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| Financial Modeling | NumPy Financial |
| Configuration | YAML |
| Decision Analytics | MCDA, TOPSIS |
| Data Source | World Bank Open Data API |

The modular architecture separates data engineering, analytics, financial modeling, visualization, and configuration into independent components, making the platform easier to maintain and extend.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/market-entry-project.git

cd market-entry-project
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```
---

## Run Main Script

```bash
python main.py
```
---

## Run Dashboard

```bash
cd dashboard

streamlit run app.py
```

The application will launch in your default web browser.

---

# Dashboard Outputs

The platform generates multiple analytical outputs throughout the evaluation workflow.

## Executive Outputs

- Executive dashboard
- Market attractiveness ranking
- Investment attractiveness ranking
- Strategic recommendations

---

## Analytical Outputs

- MCDA dimension scores
- TOPSIS ranking
- Weighted indicator scores
- Data quality assessment

---

## Financial Outputs

- Revenue projections
- Cash flow forecasts
- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period
- Sensitivity Analysis

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# Acknowledgements

Data used in this project is sourced from publicly available datasets provided by the **World Bank Open Data API**.

This project was developed for educational and portfolio purposes to demonstrate end-to-end analytics engineering, decision-support system design, and financial modeling techniques.