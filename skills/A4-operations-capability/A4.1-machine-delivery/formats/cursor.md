---
description: "A4.1 Machine Delivery & Installation — Manage the full asset delivery lifecycle — from pre-delivery planning through transport, installatio..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A4.1 — Machine Delivery

**Group:** A4 · Operations & Capability  
**Stage:** Deliver  
**Layer:** Front Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Machine Delivery covers the physical deployment of EaaS assets — from logistics planning and site preparation through equipment installation, commissioning, and formal handover to operations. It is the moment the EaaS promise becomes a physical reality at the customer site.

---

## Why It Matters in EaaS

Unlike a product sale where delivery ends at the loading dock, EaaS delivery ends when the asset is producing outcomes. A slow, disorganised, or technically flawed installation delays SLA commencement, damages customer confidence, and incurs cost overruns that erode the contract margin before a single invoice is issued.

---

## Machine Delivery Process

### Phase 1: Pre-Delivery Planning
- Confirm site readiness against pre-installation checklist (power, space, access, interfaces)
- Coordinate logistics: transport, lifting equipment, specialist contractors
- Confirm equipment build and factory acceptance test (FAT) completion
- Brief installation team on site-specific requirements and safety protocols

### Phase 2: Transport & Site Logistics
- Equipment transport with appropriate handling (vibration, temperature, secure load)
- Site access coordination with customer (permits, escorts, time windows)
- Equipment receiving inspection: visual check, serial numbers, completeness vs. packing list

### Phase 3: Installation
- Physical positioning and mechanical installation
- Electrical and utility connections per approved drawings
- Integration with existing customer systems (network, SCADA, ERP)
- IoT sensor installation and telemetry wiring

### Phase 4: Commissioning & Testing
- System power-up and functional checks against commissioning protocol
- Performance validation: run equipment at rated conditions; capture baseline readings
- IoT telemetry validation: confirm data is flowing correctly to monitoring platform
- Safety system testing: alarms, interlocks, emergency stops

### Phase 5: Operator Training & Handover
- Operator training: safe use, routine checks, escalation procedure
- Handover documentation package delivered to customer (manuals, as-built drawings, certificates)
- Go-live acceptance signed by customer (refer to A2.5 Implementation Blueprint)
- SLA measurement period formally commenced

---

## Site Readiness Checklist

| Item | Customer Responsibility | Provider Responsibility |
|------|------------------------|------------------------|
| Power supply (spec confirmed) | ✓ | Verify |
| Floor load capacity | ✓ | Verify |
| Space clearances | ✓ | Verify |
| Network/data connection | ✓ | Specify |
| Safety risk assessment | Joint | Joint |
| Lifting equipment (if required) | | ✓ |
| Installation crew | | ✓ |
| Commissioning protocol | | ✓ |

---

## Factory Acceptance Test (FAT) Criteria

Before shipping, equipment must pass FAT:
- All specified functions demonstrated under load
- Safety systems tested and signed off
- Serial numbers and asset data recorded
- IoT hardware installed and bench-tested
- Documentation pack complete (certificates, calibration records)

---

## Key Outputs

- Delivery & Installation Plan (logistics, timeline, crew)
- Site Readiness Certificate (signed by customer pre-delivery)
- Commissioning Report (test results, baseline readings)
- Go-Live Acceptance Certificate (signed by customer)
- Asset Record (serial number, installation date, location, IoT device IDs)

---

## Related Skills

- A2.5 Implementation Blueprint — master plan for the implementation phase
- A4.2 Customer Onboarding — runs in parallel with machine delivery
- A4.6 MRO Service — takes ownership of the asset post-handover
- A5.5 IoT & Smart Contracts — requires telemetry commissioning completed here

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
