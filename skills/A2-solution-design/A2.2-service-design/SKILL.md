# A2.2 — Service Design

**Group:** A2 · Solution Design  
**Stage:** Order  
**Layer:** Shared Platforms  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Service Design defines the full service experience the customer will receive throughout the EaaS contract — from installation and onboarding through daily operations, maintenance, and end-of-contract. It creates the service architecture that underpins the outcome commitments.

---

## Why It Matters in EaaS

In EaaS, the provider is responsible for outcomes, which means the provider must design and control the service processes that deliver those outcomes. Poor service design creates unplanned service costs that destroy contract economics, and poor customer experience that destroys relationships.

---

## EaaS Service Design Components

### 1. Service Scope Definition

Clearly define what is included and excluded:

| Service Element | Included | Excluded | Notes |
|-----------------|----------|----------|-------|
| Installation & commissioning | ☐ | ☐ | |
| Operator training | ☐ | ☐ | |
| Planned maintenance | ☐ | ☐ | |
| Unplanned repair | ☐ | ☐ | |
| Spare parts (wear parts) | ☐ | ☐ | |
| Spare parts (consumables) | ☐ | ☐ | |
| Remote monitoring | ☐ | ☐ | |
| Software updates (OTA) | ☐ | ☐ | |
| Performance reporting | ☐ | ☐ | |
| End-of-contract removal | ☐ | ☐ | |

### 2. Service Response Model

| Severity | Response Time | Resolution Time | Communication Channel |
|----------|---------------|-----------------|----------------------|
| Critical (production stopped) | ≤2 hours | ≤8 hours onsite | Dedicated hotline |
| Major (degraded performance) | ≤4 hours | ≤24 hours | Ticket + call |
| Minor (cosmetic, non-critical) | ≤24 hours | ≤72 hours | Ticket portal |

### 3. Planned Maintenance Programme

- Define maintenance intervals (hours, cycles, calendar)
- Schedule planned maintenance windows with customer
- Document spare parts consumption plan and buffer stock requirements

### 4. Remote Monitoring & Diagnostics

- Define monitoring KPIs and alert thresholds
- Establish escalation protocol: automated alert → technician triage → field dispatch
- Define data ownership and access rights for monitoring data

---

## Key Outputs

- Service Scope Document (included / excluded scope matrix)
- Service Response Model (SLA matrix)
- Planned Maintenance Programme
- Remote Monitoring Protocol
- Service Cost Model (internal: cost to deliver the designed service)

---

## Related Skills

- A2.3 Service Blueprint — visualises the service design as an experience map
- A3.7 SLA Design — translates service design into contractual commitments
- A4.1 Machine Delivery — executes the installation and commissioning phase
- A4.2 Customer Onboarding — onboards the customer into the service model
- A4.5 MRO Service — manages the ongoing maintenance execution

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
