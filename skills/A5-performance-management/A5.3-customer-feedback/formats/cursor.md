---
description: "A5.3 Customer Feedback — Collect, analyse, and act on customer sentiment across transactional, relationship, and unsolicited ..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

# A5.3 — Customer Feedback

**Group:** A5 · Performance Management  
**Stage:** Improve  
**Layer:** Front Office  
**Version:** v1.0  
**License:** Apache 2.0

---

## What This Skill Covers

Customer Feedback covers the structured collection, analysis, and actioning of customer sentiment across the EaaS contract lifecycle — from onboarding through steady-state delivery and renewal. It provides the voice-of-customer input that operational data alone cannot supply.

---

## Why It Matters in EaaS

SLA performance data tells the provider what happened operationally. Customer feedback tells the provider what the customer experienced — and there is a persistent gap between the two. A provider can hit every KPI and still lose the renewal because the customer felt unheard, undervalued, or surprised. Customer feedback closes that gap and gives the provider the intelligence to intervene before dissatisfaction becomes defection.

---

## Feedback Collection Framework

### 1. Transactional Feedback (Event-Triggered)
Collected after specific service interactions:

| Trigger Event | Method | Timing | Key Question |
|---------------|--------|--------|-------------|
| Reactive maintenance resolution | Email survey (3 questions) | Within 24h of close | Was your issue resolved satisfactorily? |
| Planned maintenance visit | Field engineer tablet survey | At site, post-visit | How would you rate today's service? |
| QBR / Business Review | Structured feedback form | End of meeting | Are we meeting your expectations? |
| Onboarding completion | Interview or survey | 90 days post go-live | How smooth was the transition? |

### 2. Relationship Feedback (Periodic)
Collected on a scheduled cadence regardless of specific events:

- **Annual NPS (Net Promoter Score):** Single question survey to all customer stakeholders; tracks relationship health at account level
- **Annual Voice of Customer Interview:** 30-minute structured interview with the senior customer sponsor; covers strategic satisfaction, unmet needs, renewal intent

### 3. Unsolicited Feedback
- Monitor escalation calls, complaint emails, and support tickets for sentiment
- Track LinkedIn, trade press, and industry event commentary for public feedback
- Log informal feedback from QBRs and relationship calls into the feedback system

---

## Feedback Metrics

| Metric | Description | Frequency |
|--------|------------|-----------|
| **NPS** | Net Promoter Score (Promoters – Detractors / Total) | Annual |
| **CSAT** | Customer Satisfaction Score (transactional, 1–5) | Per event |
| **CES** | Customer Effort Score (ease of doing business) | Quarterly |
| **Renewal Intent** | Likelihood to renew (1–10); tracked in CRM | Quarterly |
| **Issue Resolution Satisfaction** | Satisfaction with reactive call resolution | Per incident |

---

## Closing the Loop

Collecting feedback without acting on it damages trust more than not collecting it at all. Every feedback mechanism must have a close-the-loop process:

1. **Acknowledge** — Confirm receipt within 24 hours
2. **Review** — Route to the accountable owner (CSM, Operations, etc.)
3. **Respond** — Share what action will be taken (or why no action is planned)
4. **Act** — Implement the change; update the improvement action register
5. **Confirm** — Follow up with the customer that the change was made

---

## Red Flag Signals

Prioritise immediate action when feedback indicates:
- NPS Detractor score from the senior customer sponsor
- Complaint about invoice accuracy or billing disputes
- Sentiment that the provider "doesn't listen" or "is hard to reach"
- Mention of a competitor evaluation or RFP being issued
- Frustration with SLA definition or measurement methodology

---

## Key Outputs

- NPS Score (per account, per year)
- CSAT Score (per service interaction)
- Feedback Summary Report (quarterly, for leadership)
- Customer Feedback Action Register (open and closed items)
- Renewal Risk Flag Report (accounts with declining NPS or renewal intent)

---

## Related Skills

- A4.3 Customer Success — primary consumer and owner of customer feedback
- A5.2 Continuous Improvement — uses feedback as an improvement input source
- A4.2 Customer Onboarding — onboarding feedback informs programme improvement
- A3.5 Internal Organisation — feedback informs governance and staffing decisions

---

*EaaS End-to-End Operating Model · v1.24.0 · © Luis Prato · Apache 2.0 · luisprato.com/resources*
