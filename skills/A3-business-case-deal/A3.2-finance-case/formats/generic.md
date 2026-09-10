# A3.2 — Finance Case

> **EaaS E2E Operating Model** · Group: A3 · Business Case & Deal · Role: Finance Director
> Version: 1.24.0 · License: Apache-2.0 · Author: Luis Prato

**Summary:** Structure the financing model for EaaS asset deployment — evaluating balance sheet, off-balance sheet, and third-party financing options against the contract economics.

**Key Outcomes:**
- Financing structure options analysis
- Cost of capital and WACC impact assessment
- Debt covenants and lender requirements review
- Recommended financing structure with rationale

---

## What This Skill Covers

The Finance Case models the financial structure of the EaaS arrangement — covering asset financing, accounting treatment (IFRS 16 / lease classification), cash flow profile, and the customer's financial perspective. It bridges commercial design and financial execution.

---

## Why It Matters in EaaS

EaaS involves significant capital deployed over long periods. How this capital is financed — and how the contract is classified for accounting purposes — determines whether the deal works for both parties. An EaaS contract misclassified as a finance lease can undermine the customer's motivation and complicate the provider's balance sheet.

---

## Finance Case Components

### 1. Asset Financing Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **Internal financing** | Provider funds asset from own balance sheet | Full control; no third-party terms | Capital-intensive; limits deal volume |
| **Asset-backed lending** | Bank loan secured against equipment | Leverages balance sheet | Covenant risk; lender approval |
| **Operating lease** | Provider leases asset from lessor; sub-leases as EaaS | Off-balance-sheet for customer; capital-light for provider | Requires lessor; margin sharing |
| **Sale & leaseback** | Sell asset to financial institution; lease it back | Immediate liquidity | Complexity; residual value exposure |
| **Captive finance company** | Dedicated SPV to hold and finance assets | Tax efficiency; balance sheet isolation | Regulatory overhead |

### 2. IFRS 16 / Lease Classification Analysis

EaaS contracts must be assessed against lease classification criteria:

**Finance lease indicators** (avoid if targeting operating lease treatment for customer):
- Ownership transfers at end of contract
- Customer has purchase option at significant discount to fair value
- Contract term covers major part of economic life
- PV of minimum payments ≈ fair value of asset

**Operating lease characteristics** (preferred for EaaS):
- Provider retains substantive residual value risk
- Multiple customers could use the same asset type
- Short-to-medium term relative to economic life
- No guaranteed purchase option

### 3. Cash Flow Profile

| Period | Provider Cash Outflow | Provider Cash Inflow | Net |
|--------|----------------------|---------------------|-----|
| Year 0 | Asset purchase; installation | — | (CapEx) |
| Years 1–N | Financing cost; service delivery cost | Monthly outcome fee | +/– |
| End of contract | Refurbishment; removal | Residual value recovery or reinvestment | |

### 4. Customer Financial Perspective

- **CapEx avoidance**: EaaS converts equipment purchase to OpEx; frees capital for core business investment
- **Balance sheet impact**: Operating lease treatment keeps debt off balance sheet (subject to IFRS 16)
- **Cash flow predictability**: Fixed monthly fee vs. lumpy CapEx + unpredictable maintenance
- **Budget alignment**: OpEx fits annual budget cycles; easier to approve than CapEx

---

## Key Outputs

- Financing Structure Recommendation
- Lease Classification Analysis (IFRS 16 checklist)
- Cash Flow Model (provider and customer perspectives)
- Treasury / CFO Briefing Note (for internal approval)
- Term Sheet inputs for financing arrangement

---

## Related Skills

- A3.1 Business Case — commercial companion; this skill focuses on financing and accounting
- A4.4 Revenue Recognition & IFRS Compliance — ongoing accounting treatment post-signing
- A4.3 Insurance & Residual Value Management — manages residual value risk in the financing model
- A3.5 Digital Contracting Platform — manages the contract documentation for financing arrangements

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*

---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · A3.2 Finance Case · v1.24.0*
