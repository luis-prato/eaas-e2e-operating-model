# A4.6 — MRO Service

**Group:** A4 · Operations & Capability  
**Stage:** Deliver  
**Layer:** Middle Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

MRO (Maintenance, Repair & Overhaul) Service covers the technical service delivery that keeps EaaS assets performing at contracted levels — including planned preventive maintenance, reactive repair, spare parts management, field service dispatch, and mean time to repair (MTTR) optimisation.

---

## Why It Matters in EaaS

In a product sale, after-sale service is optional revenue. In EaaS, MRO is contractual performance delivery. Every unplanned failure that exceeds the contracted response time is a KPI miss. Every avoidable failure that predictive maintenance should have caught is margin erosion. MRO in EaaS is not a cost centre — it is the operational mechanism that converts the SLA promise into reality.

---

## MRO Service Framework

### 1. Preventive Maintenance (PM)
**Purpose:** Prevent failures through scheduled intervention.

- PM schedule derived from OEM recommendations, asset usage data, and contract requirements
- PM visits logged in CMMS (Computerised Maintenance Management System)
- PM completion confirmed by field engineer report + customer sign-off
- PM scope includes: lubrication, filter changes, calibration, wear part replacement, firmware updates

**Best practice:** Predictive maintenance overlays condition data (vibration, temperature, energy consumption) to optimise PM intervals — reducing unnecessary visits while preventing failures.

### 2. Reactive Maintenance (RM)
**Purpose:** Restore asset performance after an unplanned failure.

| Priority | Response Target | Typical Trigger |
|----------|----------------|-----------------|
| P1 — Critical | 4 hours on-site | Production-stopping failure |
| P2 — High | Next business day | Performance degraded; workaround available |
| P3 — Standard | Within 5 business days | Minor fault; no production impact |

Response time SLAs are contracted and measured from fault notification to field engineer on-site.

### 3. Spare Parts Management
- Maintain a stocked spare parts inventory sized to meet contracted response times
- Classify parts by criticality: A (production-critical, hold on-site), B (hold at regional depot), C (order on demand)
- Monitor stock levels against consumption; trigger reorder at minimum stock threshold
- Manage supplier lead times; dual-source critical parts where feasible
- Track parts to asset (serialised tracking for warranty and wear analysis)

### 4. Field Service Dispatch
- Integrate CMMS with IoT monitoring: alerts trigger automatic work orders for threshold breaches
- Dispatch field engineers based on proximity, skill match, and parts availability
- Mobile field service app: work order, asset history, parts lookup, customer sign-off
- Travel time and first-time fix rate are key efficiency KPIs

---

## MRO Performance KPIs

| KPI | Definition | Target |
|-----|-----------|--------|
| **MTTR** (Mean Time to Repair) | Average time from failure notification to asset restored | < 4 hours (P1) |
| **MTBF** (Mean Time Between Failures) | Average operating time between unplanned failures | Asset-class specific |
| **PM Completion Rate** | Planned maintenance visits completed on schedule | ≥ 98% |
| **First-Time Fix Rate** | Reactive calls resolved without return visit | ≥ 85% |
| **Parts Availability** | Critical parts in stock at time of need | ≥ 95% |
| **SLA Compliance** | Response time targets met across all priority levels | ≥ 99% |

---

## Technology Stack for MRO

| System | Role |
|--------|------|
| **CMMS** | Work order management, PM scheduling, asset history |
| **IoT Platform** | Real-time asset condition monitoring; predictive alerts |
| **Parts Management System** | Inventory, reorder, supplier management |
| **Mobile Field App** | Field engineer work order execution and reporting |
| **Routing & Dispatch** | Field engineer scheduling and route optimisation |

---

## Key Outputs

- PM Schedule (per asset, per contract)
- Work Order Log (planned and reactive, all contracts)
- MTTR / MTBF Performance Report (monthly)
- Spare Parts Inventory Report (stock levels, consumption, reorder status)
- Field Service Performance Dashboard (SLA compliance, first-time fix, engineer utilisation)
- Failure Mode Log (recurring failures flagged for root cause analysis)

---

## Related Skills

- A4.1 Machine Delivery — installs the assets this skill maintains
- A5.4 Performance Monitoring — provides the KPI data that MRO must maintain
- A5.5 IoT & Smart Contracts — generates the alerts that trigger reactive maintenance
- A5.2 Continuous Improvement — uses failure mode data to improve MRO processes

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
