---
description: "A2.1 Baseline Journey Mapping — Document the customer's current asset ownership experience — from procurement through operation and ..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A2.1 — Baseline Journey Mapping

**Group:** A2 · Solution Design  
**Stage:** Order  
**Layer:** Shared Platforms  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Baseline Journey Mapping documents the customer's current end-to-end process — from equipment acquisition through operation, maintenance, and disposal — to establish the performance baseline that an EaaS solution will be measured against. It is the foundation for all outcome commitments.

---

## Why It Matters in EaaS

"Baseline first" is the first rule of EaaS SLA design. You cannot commit to improving uptime from X% to Y% unless you have measured X%. Baseline Journey Mapping creates the validated, agreed-upon starting point that makes outcome commitments credible and disputes avoidable.

---

## Journey Mapping Dimensions

### Operational Journey (Current State)

Map the customer's current process across five dimensions:

1. **Asset acquisition** — How does equipment arrive, get installed, and enter production?
2. **Normal operations** — How is the asset used day-to-day? Shifts, throughput targets, quality checks?
3. **Maintenance cycle** — Planned vs. unplanned maintenance: frequency, duration, cost, who does it?
4. **Performance monitoring** — What KPIs are tracked today? How? How often? By whom?
5. **End of life** — What happens when equipment fails beyond repair or becomes obsolete?

### Performance Baseline Data (Minimum Required)

| KPI | Measurement Period | Data Source | Agreed? |
|-----|-------------------|-------------|---------|
| Asset uptime (%) | Last 12 months | SCADA / maintenance log | ☐ |
| MTBF (hours) | Last 12 months | CMMS | ☐ |
| MTTR (hours) | Last 12 months | Ticketing system | ☐ |
| Throughput (units/hour) | Last 3 months | MES / line counter | ☐ |
| Energy consumption (kWh/unit) | Last 12 months | Smart meter / ERP | ☐ |
| Maintenance cost (€/month) | Last 12 months | ERP / finance | ☐ |

---

## Key Activities

1. **Documentation review** — Collect existing process documentation, maintenance logs, performance reports
2. **Observation sessions** — Where possible, observe the asset in operation; identify undocumented practices
3. **Data extraction** — Pull KPI data from source systems; validate completeness and accuracy
4. **Joint validation workshop** — Present baseline findings to customer stakeholders; agree on baseline values
5. **Baseline freeze** — Formally agree and sign off on the baseline data before contract design continues
6. **Gap documentation** — Where baseline data is missing, document the gap and agree on a measurement methodology before contract signing

---

## Key Outputs

- Current-State Journey Map (visual and narrative)
- Baseline KPI Dataset (agreed and signed off)
- Data Quality Assessment (confidence level per KPI)
- Baseline Gap Register (where data is missing or unreliable)
- Agreed Measurement Methodology for each KPI

---

## Common Baseline Disputes (and How to Prevent Them)

| Dispute | Prevention |
|---------|-----------|
| "The baseline was unusually bad that year" | Use rolling 24-month average; exclude documented force majeure events |
| "Different systems show different numbers" | Agree on a single system of record per KPI before signing |
| "We didn't know maintenance cost was that high" | Require finance-approved maintenance cost data |
| "Seasonal variation wasn't accounted for" | Specify seasonal adjustment methodology in the contract |

---

## Related Skills

- A1.3 Discovery Blueprint — initiates baseline data collection
- A3.7 SLA Design — uses baseline as the starting point for KPI targets
- A5.4 Performance Monitoring — ongoing measurement against this baseline

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
