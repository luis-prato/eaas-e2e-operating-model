# A1.1 — Data Platform Readiness ★ NEW v1.23

**Group:** A1 · Strategy & Discovery  
**Stage:** Discover  
**Layer:** Shared Platforms  
**Version:** v1.23 (new)  
**License:** Apache 2.0

---

## What This Skill Covers

Data Platform Readiness assesses whether an organisation's data infrastructure can support the continuous measurement, monitoring, and reporting required for an EaaS / outcome-based contract. Without reliable data, SLA targets cannot be verified and outcome-based pricing cannot be enforced.

---

## Why It Matters in EaaS

EaaS contracts pay for outcomes (uptime, throughput, energy efficiency) — not for equipment. This means measurement is contractual, not optional. A weak data platform creates disputes, billing errors, and SLA failures that erode trust and destroy contract economics.

---

## Key Activities

1. **Baseline data audit** — Inventory all existing data sources: PLC tags, SCADA historians, MES systems, ERP outputs, sensor feeds
2. **Measurement gap analysis** — Map required KPIs (uptime, throughput, quality, energy) against current data availability
3. **Data quality assessment** — Check completeness, latency, accuracy, and retention of existing data streams
4. **Architecture readiness review** — Evaluate whether current infrastructure can handle real-time telemetry at EaaS scale
5. **Integration pathway design** — Define the integration roadmap: APIs, edge gateways, cloud connectors, historian bridges
6. **Data governance framework** — Establish ownership, access rights, and audit trail requirements for contractual data

---

## Key Outputs

- Data Readiness Assessment Report
- KPI-to-Data-Source Mapping Matrix
- Integration Architecture Diagram
- Data Quality Scorecard (per KPI)
- Gap Remediation Roadmap with cost and timeline

---

## Common Failure Modes

| Failure | Consequence |
|---------|-------------|
| KPIs defined without confirming data exists | SLA targets cannot be verified at contract start |
| Data siloed across departments | Disputes over which system is "the truth" |
| No agreed measurement window | Gaming of uptime calculations |
| High data latency (daily batch instead of real-time) | Slow detection of SLA breaches; delayed remediation |

---

## Skill Inputs

- Asset inventory and technical specifications
- Current SCADA / MES / ERP architecture
- Draft SLA KPI list (from A3.7 — SLA Design)
- IT/OT integration constraints

---

## Related Skills

- A1.2 Technology Stack Assessment — evaluates the broader tech platform
- A3.7 EaaS SLA Design — defines the KPIs this data platform must measure
- A5.1 Analytics & ESG Dashboards — consumes data platform outputs
- A5.4 Performance Monitoring — ongoing use of this infrastructure

---

## Practitioner Notes

> "In every EaaS deal where measurement was disputed post-signing, we found the same root cause: the data readiness conversation happened after the contract was signed, not before. Data readiness is a pre-contract gate, not a post-contract problem."
> — Luis Prato, EaaS Operating Model v1.24.0

**Rule of thumb:** If you cannot measure a KPI today, you cannot put it in an outcome-based contract today. Either fix the data infrastructure first, or exclude that KPI until measurement is verified.

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
