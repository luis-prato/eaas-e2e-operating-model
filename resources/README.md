# EaaS E2E Operating Model — Resources

Practitioner artifacts that accompany the 32-skill EaaS E2E Operating Model library. These are human-facing tools (calculators, templates, SOPs) — not AI agent skills.

---

## Interactive Tools (`tools/`)

Web-based decision and assessment tools. Open in any browser — no installation required.

| File | Purpose |
|------|---------|
| `eaas-financing-mode-matrix.html` | Financing Mode Fit Matrix — ADL benchmark scoring across Purchase / Financing / Leasing / Outsourcing / AaaS |
| `eaas-go-no-go.html` | Go/No-Go Decision Framework — 5-dimension RAG rating (Strategic Fit, Risk, Capability, Financial, Alignment) |
| `eaas-obc-sla-design.html` | OBC SLA Design Table — 6 standard objective rows; editable and printable |
| `eaas-product-suitability-assessment.html` | Product Suitability Assessment — Customer Lens + Provider Lens, combined score /48 |
| `eaas-risk-register-provider.html` | Risk Register Provider — 19 pre-filled risks (PR-01–PR-19) with Probability × Impact scoring |

---

## Excel Calculators (`calculators/`)

Quantitative models for financial analysis and risk management.

| File | Purpose |
|------|---------|
| `EaaS-Business-Case-Calculator.xlsx` | Full business case model — revenue, cost, margin, payback |
| `EaaS-Customer-TCO-Calculator.xlsx` | Total Cost of Ownership comparison (buy vs. EaaS) |
| `EaaS-Finance-Deal-Structuring-Calculator.xlsx` | Deal structuring — AaaS refinancing, balance sheet impact |
| `EaaS-Finance-Risk-Assessment.xlsx` | Finance-side risk scoring and sensitivity analysis |
| `EaaS-Risk-Action-Plan.xlsx` | Risk action planning with owner and timeline tracking |
| `EaaS-Risk-Register.xlsx` | Full risk register template |
| `EaaS-Riskiest-Assumptions.xlsx` | Riskiest Assumptions Ranking Tool |
| `EaaS-Tendering-Procedure-Toolkit.xlsx` | Tendering and procurement procedure toolkit |

---

## Documents (`docs/`)

Legal and contractual reference documents.

| File | Purpose |
|------|---------|
| `EaaS-Clause-Bank.docx` | Clause bank — standardised contract clauses for EaaS agreements |

---

## Standard Operating Procedures (`sops/`)

Operational SOPs organized by business process (BP) and stage:

- **BP001** — Tender Process & Risk Assessment
- **BP003** — Business Case & Deal (Market Analysis, Competitor Analysis, Contract Review, Legal Compliance, Approval & Signing, ERP Setup)
- **BP004** — Operations / Delivery (Onboarding, Logistics, Startup, Training, Operational Support, Documentation)
- **BP005** — Maintenance & Service (Scheduled Maintenance, Service Requests, Onsite/Remote Support, Spare Parts, Training, Performance Monitoring)
- **BP006** — End-of-Life (Renewal, Financial Analysis, Condition Assessment, Refurbishment, Disposal & Compliance)
- **SP001** — Finance & Accounting Order-to-Cash (O2C)
- **SOP** — Control Tower Documentation, Onboarding Process

---

## Plugin (`plugin/`)

| File | Purpose |
|------|---------|
| `plugin.json` | EaaS Strategy Workshop plugin manifest v1.6.0 — 13-skill workshop series for Claude Code |

---

## Mapping to Skills

Each resource maps to one or more skills in the `skills/` directory. The skills define how an AI agent assists with the corresponding process; the resources are the human-operated counterparts.

| Resource type | Corresponding skill group |
|---------------|--------------------------|
| Financing Mode Matrix | A3.5 Finance Case Design |
| Go/No-Go Framework | A3.2 Go/No-Go Assessment |
| Product Suitability Assessment | A1.2 Technology Stack Assessment, A2.2 Product Assessment |
| Risk Register | A3.4 Risk Assessment |
| Business Case Calculator | A3.1 Business Case Development |
| Customer TCO Calculator | A3.3 TCO Analysis |
| Clause Bank | A3.7 Digital Contracting Platform |
| SOPs (BP001–BP006, SP001) | A4.x Operations & Capability, A5.x Performance Management |
