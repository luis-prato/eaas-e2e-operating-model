---
description: "A4.5 Managing Contracts — Operate live EaaS contracts with rigour — tracking obligations, managing variations, processing invo..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A4.5 — Managing Contracts

**Group:** A4 · Operations & Capability  
**Stage:** Support  
**Layer:** Back Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Managing Contracts covers the active administration of live EaaS contracts — from obligation tracking and change management through invoicing, amendment processing, and performance dispute resolution. It is the operational backbone that keeps contracts compliant, commercial relationships clean, and obligations fulfilled on both sides.

---

## Why It Matters in EaaS

Long-term EaaS contracts generate a continuous stream of obligations, changes, and commercial events — maintenance schedules, indexation adjustments, asset additions, SLA reviews, and invoice cycles. Without disciplined contract management, obligations are missed, disputes accumulate, and the provider's margin erodes through unclaimed indexation, unprocessed change orders, or SLA credits issued without proper validation.

---

## Contract Management Operating Model

### Obligation Tracking
- Maintain a live obligation register for each contract (see A3.7 Digital Contracting Platform)
- Flag upcoming obligations 30, 14, and 7 days before due date
- Record fulfilment evidence for every obligation (maintenance reports, inspection certificates, calibration records)
- Escalate unfulfilled obligations immediately — delay compounds liability

### Change Management
Every change to a live EaaS contract must follow a formal process:

1. **Change request raised** — by provider or customer, in writing
2. **Impact assessment** — commercial, operational, and legal implications evaluated
3. **Pricing update** — change order value calculated and agreed
4. **Approval** — both parties sign the change order
5. **Contract update** — digital contracting platform updated with new version
6. **Implementation** — operational teams briefed on the change

Changes without signed change orders are the single most common source of EaaS contract disputes.

### Invoicing & Revenue Management
- Invoice on the schedule defined in the contract — never early, never late
- Include performance evidence with each invoice (SLA performance data for the period)
- Track payment against each invoice; escalate overdue payments at 30/45/60 days
- Apply indexation adjustments on the contracted anniversary; document the calculation
- Manage SLA credit notes accurately — issue only credits that are contractually due

### Performance Dispute Resolution
When the customer disputes SLA performance data:

1. **Receive dispute in writing** — acknowledge within agreed timeframe
2. **Review data** — pull raw telemetry; compare with customer's data
3. **Identify discrepancy source** — measurement methodology, data gap, sensor fault, or genuine underperformance
4. **Resolve or escalate** — agree correction or escalate to expert determination per contract clause
5. **Document outcome** — close with signed resolution record

---

## Contract Manager Toolkit

| Tool | Purpose |
|------|---------|
| Obligation Register | Live tracker of all contractual obligations and due dates |
| Change Order Log | Record of all amendments with approval status |
| Invoice Schedule | Forward-looking calendar of all invoice events |
| SLA Performance Tracker | Period-by-period KPI performance vs. target |
| Payment Tracker | Invoice status, payment dates, overdue flags |
| Dispute Log | Open and resolved disputes with resolution record |

---

## Indexation Management

Annual indexation is frequently unclaimed by providers who miss the contractual trigger:
- Set a calendar reminder 60 days before each indexation anniversary
- Calculate the adjustment using the contracted index (CPI, energy index, etc.)
- Notify the customer in writing before the effective date
- Update the billing system with the new fee level
- Confirm the indexed fee in the next invoice narrative

---

## Key Outputs

- Obligation Register (per contract, updated monthly)
- Change Order Log (with approval status and financial impact)
- Invoice Calendar and Payment Tracker
- Indexation Log (adjustment dates, index values, new fee levels)
- Dispute Resolution Record
- Contract Performance Summary (annual, for renewal positioning)

---

## Related Skills

- A3.7 Digital Contracting Platform — provides the system infrastructure for contract management
- A4.4 Contract Clause Bank — defines the contractual standards being managed here
- A4.3 Customer Success — commercial relationship that contract management supports
- A5.4 Performance Monitoring — supplies SLA data for invoicing and dispute resolution

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
