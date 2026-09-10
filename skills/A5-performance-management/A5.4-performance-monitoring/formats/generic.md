# A5.4 — Performance Monitoring

> **EaaS E2E Operating Model** · Group: A5 · Performance Management · Role: Contract Manager
> Version: 1.24.0 · License: Apache-2.0 · Author: Luis Prato

**Summary:** Measure EaaS asset and service KPIs with precision — from IoT data collection through SLA compliance determination and the monthly performance certificate.

**Key Outcomes:**
- KPI measurement protocols (availability, output, efficiency)
- SLA compliance determination process
- Dispute-proofing monitoring framework
- Monthly SLA compliance certificate

---

## What This Skill Covers

Performance Monitoring covers the real-time and periodic measurement of EaaS asset and service KPIs — from data collection through calculation, validation, reporting, and SLA compliance determination. It is the measurement engine that makes outcome accountability operational.

---

## Why It Matters in EaaS

You cannot manage what you cannot measure. Performance Monitoring is the operational heartbeat of every EaaS contract — it determines whether the provider is meeting its SLA commitments, triggers invoicing and credit calculations, and generates the evidence that makes the customer relationship transparent and trustworthy. Gaps or inconsistencies in monitoring create disputed invoices, SLA arguments, and legal exposure.

---

## Performance Monitoring Architecture

### Data Collection Layer
- **IoT sensors** on each asset: availability signals, energy meters, production counters, condition sensors
- **CMMS integration:** maintenance activity, downtime events, parts consumption
- **Customer-side data:** production schedules, operator logs, site conditions
- **Telemetry latency target:** < 5 minutes for real-time KPIs; < 24 hours for daily aggregates

### Calculation Layer
- Raw telemetry is cleaned, validated, and aggregated against the KPI formulas defined in the contract
- SLA carve-outs applied automatically (force majeure, customer-caused downtime, planned maintenance windows)
- Anomaly detection flags suspicious readings (sensor failure, data gap) for manual review before the KPI is locked

### Reporting Layer
- Operational dashboard: real-time (provider internal)
- Customer dashboard: updated daily (see A5.1 Analytics & ESG Dashboards)
- Monthly SLA report: period-end KPI summary used to determine invoice / credit

---

## KPI Measurement Protocols

### Availability / Uptime
```
Availability (%) = (Contracted Operating Hours − Unplanned Downtime Hours) ÷ Contracted Operating Hours × 100
```
- Contracted Operating Hours defined in the contract schedule
- Unplanned Downtime: time from fault notification to asset restored, excluding carve-out events
- Measurement period: calendar month (or as contracted)

### Performance Index (Output-Based)
```
Performance Index (%) = Actual Output ÷ Target Output × 100
```
- Target Output: contracted baseline (units, cycles, litres, tonnes, etc.)
- Actual Output: measured at asset level via production counter or flow meter
- Normalised for planned downtime and customer-instructed stops

### Energy Efficiency
```
Energy Efficiency (kWh/unit) = Total Energy Consumed ÷ Total Units Produced
```
- Measured at asset level; compared to contracted baseline efficiency
- Indexed to ambient conditions where relevant (cooling loads, temperature-dependent processes)

---

## SLA Compliance Determination

At the end of each measurement period:

1. Lock KPI data (freeze the dataset for the period)
2. Apply all SLA carve-outs with documented evidence
3. Compare final KPI to contracted target
4. Determine: at/above target → standard invoice; below target → SLA credit calculation
5. Generate SLA compliance certificate (signed by Contract Manager)
6. Issue invoice or credit note as appropriate
7. Share SLA report with customer

---

## Dispute-Proofing Monitoring

- Document the measurement methodology in the contract with worked examples
- Use independent, tamper-evident data sources (customer-side meter + provider IoT as dual record)
- Agree data validation rules in advance (what constitutes a valid reading; how gaps are handled)
- Provide customer read access to raw telemetry (transparency eliminates most disputes)
- Maintain a dispute log with resolution records for pattern analysis

---

## Key Outputs

- Real-Time Asset Performance Dashboard (provider internal)
- Monthly SLA Compliance Certificate (per contract)
- SLA Performance Data Package (sent to customer with each invoice)
- Anomaly & Data Quality Log (sensor faults, gaps, corrections)
- Portfolio Performance Report (all contracts; SLA compliance rate; at-risk assets)

---

## Related Skills

- A5.5 IoT & Smart Contracts — the IoT infrastructure that generates the monitoring data
- A5.1 Analytics & ESG Dashboards — visualises the monitoring data for customers and leadership
- A4.5 Managing Contracts — uses SLA compliance data for invoicing and dispute resolution
- A4.6 MRO Service — receives performance alerts and triggers maintenance response

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*

---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · A5.4 Performance Monitoring · v1.24.0*
