# A2.5 — Implementation Blueprint

**Group:** A2 · Solution Design  
**Stage:** Deliver  
**Layer:** Back Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

The Implementation Blueprint is the master plan for deploying the EaaS solution — from contract signing through to full operational handover. It sequences all activities, assigns responsibilities, defines milestones, and establishes the go-live acceptance criteria.

---

## Why It Matters in EaaS

EaaS contracts have long tails. A slow or messy implementation damages customer confidence before the provider has had a chance to demonstrate outcome delivery. The Implementation Blueprint ensures the transition from deal to delivery is structured, predictable, and builds trust.

---

## Implementation Phases

### Phase 0: Pre-Contract Preparation (before signing)
- Confirm technology readiness and data platform setup
- Validate spare parts inventory and supplier lead times
- Brief service team on contract terms and SLA commitments
- Set up monitoring and ticketing platforms
- Confirm insurance coverage is in place

### Phase 1: Mobilisation (weeks 1–4 post-signing)
- Internal project kick-off: assign dedicated implementation manager
- Customer kick-off meeting: introduce delivery team; align on implementation plan
- Site assessment and logistics planning
- Order equipment if not already in production

### Phase 2: Installation & Commissioning (weeks 4–12)
- Equipment delivery and physical installation
- System integration: IoT connectivity, telemetry validation, CMMS configuration
- Performance baseline measurement (if not completed pre-contract)
- Operator training delivery
- System acceptance testing (SAT) against agreed criteria

### Phase 3: Go-Live & Stabilisation (months 3–6)
- Formal go-live sign-off by customer
- Intensive monitoring period: daily KPI tracking, rapid response to issues
- Planned maintenance first cycle execution
- 30/60/90-day performance reviews
- SLA payment cycle confirmed and first invoice issued

### Phase 4: Steady State (month 6+)
- Transition to standard service rhythm
- Monthly performance reporting
- Quarterly business reviews
- Continuous improvement programme initiation

---

## Implementation RACI

| Activity | Provider PM | Field Service | Customer Ops | Customer IT | Finance |
|----------|-------------|--------------|--------------|-------------|---------|
| Installation | R/A | R | C | I | I |
| IoT integration | A | R | C | R | I |
| Operator training | R/A | R | R | I | I |
| SAT sign-off | A | R | A | I | I |
| First invoice | I | I | A | I | R/A |

R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Go-Live Acceptance Criteria (Template)

The customer formally accepts go-live when:

1. All equipment is installed and operational
2. IoT telemetry is live and validated against agreed KPIs
3. Operator training has been completed and signed off
4. Baseline KPIs have been measured and agreed
5. SLA measurement period has formally started
6. First maintenance window is scheduled
7. Customer success manager introduced and contact escalation path confirmed

---

## Key Outputs

- Implementation Master Plan (Gantt chart)
- RACI Matrix
- Go-Live Acceptance Criteria document
- Implementation Risk Register
- Post-implementation review report (90 days)

---

## Related Skills

- A4.1 Machine Delivery — executes the physical delivery component
- A4.2 Customer Onboarding — manages the customer-facing onboarding experience
- A3.7 SLA Design — defines the SLA measurement start date and conditions
- A5.3 Continuous Improvement — picks up from steady state

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
