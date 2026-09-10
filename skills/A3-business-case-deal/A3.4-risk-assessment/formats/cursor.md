---
description: "A3.4 Risk Assessment — Identify, score, and allocate the full risk register for an EaaS contract — covering technical, comm..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A3.4 — Risk Assessment

**Group:** A3 · Business Case & Deal  
**Stage:** Order  
**Layer:** Middle Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

The EaaS Risk Assessment identifies, quantifies, and allocates the risks inherent in an outcome-based service contract — from asset failure and performance shortfall to customer-side risks and macro-economic exposures. It feeds the Business Case, the contract design, and the bid strategy.

---

## Why It Matters in EaaS

EaaS providers carry risks that product sellers never touched: machine reliability, energy price volatility, workforce availability, and the customer's operational context. Underestimating any one of these can turn a profitable contract into a liability. The Risk Assessment makes risk visible before it becomes expensive.

---

## EaaS Risk Taxonomy

### 1. Technical Risk
- Asset reliability below forecast MTBF
- Spare parts unavailability or excessive lead times
- Technology obsolescence during contract term
- IoT/telemetry data gaps or failures

### 2. Performance Risk
- KPI miss due to factors within provider control (maintenance quality, response time)
- KPI miss due to factors partially within provider control (asset wear, consumables)
- KPI miss due to customer-side factors (misuse, site conditions, refusal of access)

### 3. Commercial & Financial Risk
- Pricing model underestimating total service cost
- Energy or commodity cost inflation beyond indexed adjustments
- Currency risk in multi-country contracts
- Customer credit risk / insolvency

### 4. Contractual & Legal Risk
- SLA ambiguity leading to disputed measurement
- Liability cap inadequate relative to potential SLA penalties
- Regulatory change affecting product use or safety compliance
- Intellectual property ownership disputes

### 5. Operational Risk
- Field service workforce shortage
- Subcontractor performance failure
- Site access denied by customer
- Health & safety incidents during service delivery

### 6. Strategic Risk
- Customer early termination (with or without penalty)
- Competitor disruption during long contract term
- Reputational damage from high-profile SLA miss

---

## Risk Scoring Matrix

For each identified risk, score:

| Dimension | Scale | Description |
|-----------|-------|-------------|
| **Likelihood** | 1–5 | 1 = Rare, 5 = Almost certain |
| **Impact** | 1–5 | 1 = Negligible, 5 = Contract-threatening |
| **Risk Score** | L × I | 1–25; escalate anything ≥ 12 |

---

## Risk Allocation Framework

Not all risks should sit with the provider. Allocate each risk to the party best placed to manage it:

| Risk | Provider | Shared | Customer |
|------|----------|--------|----------|
| Asset failure (within MTBF) | ✓ | | |
| Asset failure (due to misuse) | | ✓ | |
| Site readiness | | | ✓ |
| Energy cost inflation | | ✓ (index) | |
| Regulatory change | | ✓ | |
| Customer process change affecting KPI | | | ✓ |

---

## Risk Mitigation Options

| Mitigation | Applicable Risks |
|------------|-----------------|
| Maintenance regime upgrade | Technical, Performance |
| Spare parts buffer stock | Technical |
| Force majeure clause | Operational, Strategic |
| SLA carve-outs for customer-caused downtime | Performance |
| Price indexation clause | Commercial/Financial |
| Insurance (asset, liability, business interruption) | Technical, Operational |
| Performance bond from subcontractors | Operational |
| Early termination fee | Strategic |

---

## Key Outputs

- Risk Register (full taxonomy, scores, ownership, mitigations)
- Risk Summary for Business Case (cost of risk provisioning)
- Contract Risk Schedule (risks to be addressed in SLA and T&Cs)
- Bid Risk Sign-Off (internal approval that risk is acceptable)

---

## Related Skills

- A3.1 Business Case — incorporates risk cost provisioning into the financial model
- A3.3 Tendering Procedure — uses risk assessment to define bid red lines
- A3.7 Digital Contracting Platform — embeds risk schedule into contract
- A4.5 Managing Contracts — monitors realised risks during delivery

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
