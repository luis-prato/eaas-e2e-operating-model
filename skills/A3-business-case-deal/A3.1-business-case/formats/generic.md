# A3.1 — Business Case

> **EaaS E2E Operating Model** · Group: A3 · Business Case & Deal · Role: Commercial Director
> Version: 1.24.0 · License: Apache-2.0 · Author: Luis Prato

**Summary:** Build the full EaaS business case — P&L model, cash flow, residual value assumptions, and scenario analysis — to support internal investment approval and customer commercial negotiation.

**Key Outcomes:**
- EaaS contract P&L model
- Cash flow and working capital analysis
- Residual value and asset recovery model
- Scenario analysis (base / upside / downside)

---

## What This Skill Covers

The EaaS Business Case quantifies the provider's commercial rationale for offering an EaaS contract — modelling revenues, costs, risks, and returns across the full contract term. It is the internal financial gate that determines whether a specific EaaS opportunity is commercially viable.

---

## Why It Matters in EaaS

EaaS deals look attractive in year 1 but fail in years 3–7 when hidden service costs, underperforming assets, or pricing errors accumulate. A rigorous Business Case forces the financial consequences of outcome commitments to be modelled before signing — not discovered after.

---

## Business Case Structure

### 1. Revenue Model

| Revenue Stream | Description | Year 1 | Year 3 | Year 5 |
|----------------|-------------|--------|--------|--------|
| Base outcome fee | Fixed monthly fee for baseline performance | | | |
| Performance bonus | Variable fee for outperformance | | | |
| Indexation | Annual price adjustment (CPI/energy index) | | | |
| **Total Revenue** | | | | |

### 2. Cost Model

| Cost Category | Description | Year 1 | Year 3 | Year 5 |
|---------------|-------------|--------|--------|--------|
| Asset cost (depreciation) | Equipment cost amortised over contract | | | |
| Financing cost | Interest on asset financing | | | |
| Planned maintenance | Labour, parts, scheduled maintenance | | | |
| Unplanned repair | Estimated failure cost (probability × cost) | | | |
| Remote monitoring | Technology platform and team costs | | | |
| Field service | Travel, overtime, escalations | | | |
| Insurance | Asset insurance, liability | | | |
| Overhead allocation | G&A, contract management | | | |
| **Total Cost** | | | | |

### 3. Financial Metrics

- **Gross Margin %** per year and cumulative
- **NPV** of the contract at agreed discount rate
- **IRR** of the EaaS investment
- **Payback period** (months to recover asset investment)
- **Break-even uptime** (minimum uptime to maintain positive margin)

### 4. Scenario Analysis

Model three scenarios:
- **Base case**: KPIs met at baseline; no major unexpected costs
- **Downside**: 3–5 unplanned failures per year; performance at 80% of target
- **Upside**: Outperformance; bonus payments received; no major failures

---

## Red Lines: When to Walk Away

The business case should define minimum acceptable thresholds:
- Gross margin < 15% in base case → renegotiate or walk away
- NPV negative in base case → contract is value-destroying
- IRR < WACC + 5% → returns do not justify risk
- Break-even uptime > 95% → insufficient headroom for real-world variability

---

## Key Outputs

- Provider Business Case Model (Excel or financial model)
- Scenario Analysis (base / downside / upside)
- Go / No-Go recommendation with financial rationale
- Pricing input to contract negotiation team

---

## Related Skills

- A3.2 Finance Case — companion skill: models the customer's financial perspective and EaaS financing
- A3.3 Tendering Procedure — uses business case to define bidding strategy
- A4.6 Risk Assessment — feeds risk cost estimates into the business case cost model
- A1.6 Product Assessment — validates the product performance assumptions in the model

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*

---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · A3.1 Business Case · v1.24.0*
