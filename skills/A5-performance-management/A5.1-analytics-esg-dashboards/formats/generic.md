# A5.1 — Analytics & ESG Dashboards

> **EaaS E2E Operating Model** · Group: A5 · Performance Management · Role: Data & Sustainability Lead
> Version: 1.24.0 · License: Apache-2.0 · Author: Luis Prato

**Summary:** Design and deploy the three-tier dashboard architecture that gives operations, customers, and leadership real-time visibility of performance, value, and ESG outcomes.

**Key Outcomes:**
- Operational, customer, and ESG dashboard specifications
- ESG measurement framework (energy, circular economy, social)
- Data pipeline and update frequency architecture
- Dashboard governance and access control model

---

## What This Skill Covers

Analytics & ESG Dashboards covers the design, deployment, and operation of the reporting infrastructure that makes EaaS performance visible — to the provider's operations team, to customers, and to sustainability stakeholders. It transforms raw IoT and operational data into insight, value evidence, and ESG reporting.

---

## Why It Matters in EaaS

Data is an EaaS asset. Providers who can demonstrate — in real time, with precision — that outcomes are being delivered, energy is being saved, and emissions are being reduced, have a structural advantage in retention, renewal, and expansion. Analytics and ESG dashboards are the mechanism that converts operational data into commercial value and competitive differentiation.

---

## Dashboard Architecture

### Tier 1: Operational Dashboard (Internal, Real-Time)
**Audience:** Operations, Field Service, Contract Managers  
**Purpose:** Monitor asset performance and SLA compliance in real time  
**Key metrics:**
- Live asset status (online / offline / fault)
- Current KPI performance vs. target (availability, uptime, energy index)
- Open work orders (planned, reactive, overdue)
- MTTR and first-time fix rate (rolling 30 days)
- SLA risk alerts (assets approaching penalty threshold)

### Tier 2: Customer Performance Dashboard (External, Shared)
**Audience:** Customer Operations Lead, Contract Manager  
**Purpose:** Transparent performance reporting; evidence of value delivery  
**Key metrics:**
- SLA KPI performance vs. contracted target (current period and historical)
- Uptime delivered vs. baseline (pre-EaaS or contract target)
- Maintenance activity log (PM visits, reactive calls, resolution times)
- Upcoming maintenance schedule
- Invoice status and payment history

### Tier 3: ESG & Sustainability Dashboard (External, Executive)
**Audience:** Customer Sustainability Team, CFO, ESG Reporting Team  
**Purpose:** Quantify and report the sustainability outcomes of the EaaS contract  
**Key metrics:**
- Energy consumption (kWh) — actual vs. baseline
- Energy savings (kWh and £/€/$)
- Carbon emissions (CO₂e) — actual vs. baseline reduction
- Circular economy contribution — asset refurbishment rate, end-of-life recovery
- ESG reporting data exports (aligned to GRI, TCFD, EU Taxonomy)

---

## ESG Measurement Framework

### Energy & Carbon
- Measure energy consumption at asset level (IoT-connected meters)
- Calculate baseline using pre-EaaS consumption data or industry benchmarks
- Report savings as: kWh saved, CO₂e avoided, and financial equivalent
- Apply appropriate emission factors (location-based, market-based per GHG Protocol)

### Circular Economy
- Track asset refurbishment rate (assets repaired vs. replaced)
- Report end-of-life asset recovery (recycled, resold, refurbished)
- Calculate avoided manufacturing emissions from refurbishment vs. new production

### Social Value
- Local workforce employment (field service jobs created in customer region)
- Training hours delivered to customer operators
- Supplier diversity in the MRO supply chain (where applicable)

---

## Data Pipeline

```
IoT Sensors → Telemetry Platform → Data Warehouse → Analytics Engine → Dashboards
                                        ↑
                             CMMS + ERP + Billing data
```

Key design principles:
- Real-time data for operational dashboards (< 5-minute latency)
- Daily aggregation for customer and ESG reporting
- Data lineage documented for audit purposes
- Customer data isolated in separate logical partition (data sovereignty)

---

## Key Outputs

- Operational Performance Dashboard (provider-internal, live)
- Customer Performance Report (monthly, per contract)
- ESG / Sustainability Report (annual, per customer)
- Portfolio Analytics Report (all contracts, provider executive view)
- Data Export Package (customer's raw data for their own reporting)

---

## Related Skills

- A5.4 Performance Monitoring — generates the underlying performance data
- A5.5 IoT & Smart Contracts — the telemetry infrastructure feeding these dashboards
- A4.3 Customer Success — uses dashboards for QBR delivery and value communication
- A1.1 Data Platform Readiness — ensures the data infrastructure can support these dashboards

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*

---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · A5.1 Analytics & ESG Dashboards · v1.24.0*
