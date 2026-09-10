# A2.3 — Service Blueprint

> **EaaS E2E Operating Model** · Group: A2 · Solution Design · Role: Operations Designer
> Version: 1.24.0 · License: Apache-2.0 · Author: Luis Prato

**Summary:** Map the full operational model behind the EaaS promise — the frontstage customer interactions, backstage processes, and supporting systems that deliver the contracted outcome.

**Key Outcomes:**
- Full service blueprint with swim lanes
- Backstage process specifications
- Technology and system integration map
- Failure point and recovery protocol register

---

## What This Skill Covers

The Service Blueprint is a visual and structured map of the entire EaaS service experience — showing front-stage customer interactions, back-stage provider actions, and supporting processes — across the full contract lifecycle. It is the operational specification that enables consistent, repeatable service delivery.

---

## Why It Matters in EaaS

EaaS is a long-term relationship (typically 5–10 years). A well-designed service blueprint ensures that every team member — sales, delivery, field service, customer success, finance — knows their role at every stage. It prevents the service from degrading as the initial enthusiasm of a new contract fades.

---

## Service Blueprint Structure

The service blueprint maps four lanes across the contract lifecycle:

### Contract Lifecycle Stages
`Onboard → Operate → Maintain → Improve → Renew/Exit`

### Blueprint Lanes

```
CUSTOMER ACTIONS
  └─ What the customer does, sees, and experiences at each stage

FRONT-STAGE PROVIDER ACTIONS (Visible to customer)
  └─ What the provider does that the customer can observe

BACK-STAGE PROVIDER ACTIONS (Invisible to customer)
  └─ Internal processes that support the customer experience

SUPPORTING PROCESSES & SYSTEMS
  └─ Technology, tools, and platforms that enable delivery
```

---

## Service Blueprint: EaaS Standard Template

| Stage | Customer | Front-Stage | Back-Stage | Systems |
|-------|----------|------------|------------|---------|
| **Onboard** | Receives equipment; attends training; accepts system | Installation; training delivery; go-live sign-off | Logistics; configuration; quality check | CMMS; training platform |
| **Operate (Normal)** | Uses equipment; receives performance reports | Monthly reporting; proactive check-ins | Remote monitoring; alert management | IoT platform; BI dashboard |
| **Maintain (Planned)** | Receives maintenance notification; approves window | Technician visit; maintenance execution | Parts ordering; scheduling; post-maintenance test | ERP; CMMS; parts system |
| **Maintain (Unplanned)** | Reports issue or receives alert; tracks resolution | Incident response; repair; communication | Root cause analysis; escalation management | Ticketing system; helpdesk |
| **Improve** | Reviews improvement recommendations; co-designs targets | Quarterly business review; improvement proposals | Analytics; benchmarking; roadmap planning | Analytics platform |
| **Renew / Exit** | Negotiates renewal or exit; returns equipment | Renewal proposal; transition planning | Asset refurbishment; remarketing; removal logistics | CRM; asset management |

---

## Key Outputs

- Service Blueprint diagram (visual, full lifecycle)
- Swim-lane responsibility matrix (RACI per stage)
- Critical moments identification (moments where failure has highest customer impact)
- Fail-point analysis (where service most commonly breaks down)
- Blueprint implementation guide for operations teams

---

## Related Skills

- A2.2 Service Design — provides the service scope and response model input
- A2.4 Capability Strategy — identifies capability gaps in delivering this blueprint
- A3.7 SLA Design — contractualises the front-stage commitments in this blueprint
- A4.2 Customer Onboarding — executes the Onboard stage

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*

---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · A2.3 Service Blueprint · v1.24.0*
