---
description: "A5.2 Continuous Improvement — Run a structured PDCA improvement programme that prevents margin erosion, reduces reactive maintenan..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A5.2 — Continuous Improvement ★ NEW v1.24

**Group:** A5 · Performance Management  
**Stage:** Improve  
**Layer:** Middle Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Continuous Improvement in EaaS is the structured process of analysing contract performance data, identifying patterns, and implementing operational or commercial changes that improve reliability, reduce cost, and increase the margin contribution of the EaaS portfolio over time.

---

## Why It Matters in EaaS

Year 1 performance does not equal Year 5 performance. Assets degrade, operational patterns evolve, and service costs compound. EaaS providers who operate without a formal improvement process find their margins eroding silently — more reactive calls, longer MTTRs, growing parts consumption — until a contract that looked profitable at signing is loss-making by Year 4. Continuous Improvement reverses that trajectory.

---

## Improvement Framework

### PDCA Cycle for EaaS

**Plan** — Identify the improvement opportunity:
- Which assets are generating disproportionate maintenance cost?
- Which failure modes are recurring?
- Which SLA metrics are consistently at risk?
- Which service processes have the highest variation?

**Do** — Implement the change:
- Modify the PM schedule (frequency, scope, technique)
- Change parts (higher-quality component, extended service life)
- Retrain field engineers (technique, tool, sequence)
- Update the monitoring alert threshold
- Redesign the dispatch or parts logistics process

**Check** — Measure the outcome:
- Compare KPIs before and after the change (at least 90-day window)
- Confirm cost savings are materialising in the financial model
- Check for unintended consequences (other metrics affected)

**Act** — Standardise or iterate:
- Roll successful changes across the fleet
- Update the playbook, training materials, and PM specification
- Document the improvement in the contract continuous improvement log

---

## Improvement Input Sources

| Source | Data Provided | Frequency |
|--------|--------------|-----------|
| **Failure Mode Analysis** | Recurring failure patterns by asset type and age | Monthly |
| **MTTR Trend** | Is response and repair getting faster or slower? | Monthly |
| **SLA Near-Miss Log** | Incidents that almost triggered a penalty | Monthly |
| **Customer Feedback** | Service quality perception vs. operational data | Quarterly |
| **Technician Feedback** | Process friction; parts quality; tool gaps | Quarterly |
| **Cost Variance Report** | Where is actual cost exceeding plan? | Monthly |
| **Benchmarking** | How does fleet MTBF compare to industry norms? | Annual |

---

## Improvement Governance

### Continuous Improvement Review (Monthly)
- **Participants:** Operations Manager, Contract Managers, Field Service Lead
- **Agenda:** Performance variance analysis; open improvement actions; new opportunities identified
- **Output:** Improvement action register (updated)

### Portfolio Improvement Forum (Quarterly)
- **Participants:** Operations Director, Technology Lead, Finance, Customer Success
- **Agenda:** Portfolio-level trend analysis; investment decisions on systemic improvements; technology or process upgrades
- **Output:** Portfolio improvement roadmap; capital investment proposals

---

## Technology-Enabled Improvement

Predictive analytics unlocks a more proactive improvement model:

- **Remaining useful life (RUL) modelling** — predict when a component will fail, based on condition data; replace before failure at optimal cost point
- **Anomaly detection** — identify unusual operating patterns that precede failure
- **Cross-fleet learning** — apply failure patterns from one site to prevent failures at comparable sites
- **Digital twin** — simulate the impact of PM schedule or component changes before implementation

---

## Key Outputs

- Continuous Improvement Action Register (open and closed actions, owners, deadlines)
- Monthly Performance Variance Report
- Improvement ROI Tracker (cost savings and margin impact per improvement implemented)
- Fleet Reliability Trend Report (MTBF, MTTR, SLA compliance over time)
- Technology Improvement Roadmap (data-driven upgrades to MRO and monitoring)

---

## Related Skills

- A5.4 Performance Monitoring — primary data source for improvement analysis
- A4.6 MRO Service — the operational function where most improvements are implemented
- A5.3 Customer Feedback — external perspective on where improvement is most needed
- A1.1 Data Platform Readiness — the infrastructure that enables predictive improvement analytics

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
