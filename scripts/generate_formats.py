#!/usr/bin/env python3
"""
generate_formats.py
-------------------
Reads all SKILL.md files in the EaaS E2E Operating Model repository and generates:
  - skill.json          (machine-readable metadata per skill)
  - formats/openai.json (OpenAI Agents SDK tool definition)
  - formats/gemini.json (Google Gemini function calling format)
  - formats/cursor.md   (Cursor Rules / .cursor/skills format — identical to SKILL.md)
  - formats/generic.md  (clean markdown for any platform)
  - manifest.json       (root index of all 32 skills)

Usage:
  python scripts/generate_formats.py

Run from repo root. Safe to re-run — overwrites existing format files.
"""

import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Skill master data
# ---------------------------------------------------------------------------
# Structured data for all 32 skills. Outcomes and summaries are derived from
# the SKILL.md content and kept in sync here for programmatic generation.

SKILLS = [
    # A1 · Strategy & Discovery
    {
        "code": "A1.1", "slug": "e2e-data-platform-readiness",
        "name": "Data Platform Readiness", "new": True,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.1-data-platform-readiness.md",
        "stage": "Discover", "layer": "Shared Platforms", "role": "Technology Lead",
        "tags": ["data", "infrastructure", "iot", "esg", "readiness"],
        "summary": "Assess whether your data infrastructure can support real-time asset monitoring, automated SLA calculation, and ESG reporting before an EaaS contract goes live.",
        "outcomes": [
            "Data readiness audit across six dimensions",
            "Gap remediation roadmap with cost estimates",
            "Go/no-go recommendation for EaaS deployment",
            "Data governance framework for IoT and operational data"
        ],
        "parameters": {
            "asset_type": "Type of industrial asset to be monitored (e.g. compressor, HVAC, conveyor)",
            "data_sources": "Existing data sources and systems (SCADA, ERP, CMMS, etc.)",
            "sla_requirements": "Performance KPIs and SLA targets the contract must measure"
        }
    },
    {
        "code": "A1.2", "slug": "e2e-technology-stack-assessment",
        "name": "Technology Stack Assessment", "new": True,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.2-technology-stack-assessment.md",
        "stage": "Discover", "layer": "Shared Platforms", "role": "Technology Lead",
        "tags": ["technology", "systems", "iot", "cmms", "erp", "assessment"],
        "summary": "Evaluate your current technology systems against EaaS requirements and build a roadmap to close capability gaps before your first contract.",
        "outcomes": [
            "Technology capability gap analysis",
            "Build vs buy vs integrate decision framework",
            "Stack integration architecture",
            "Technology investment roadmap"
        ],
        "parameters": {
            "current_systems": "List of current technology systems in use",
            "eaas_requirements": "Specific EaaS capabilities required (IoT, billing, CMMS, etc.)",
            "budget_constraints": "Investment budget available for technology upgrades"
        }
    },
    {
        "code": "A1.3", "slug": "e2e-discovery-blueprint",
        "name": "Discovery Blueprint", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.3-discovery-blueprint.md",
        "stage": "Discover", "layer": "Front Office", "role": "Strategy Lead",
        "tags": ["discovery", "customer", "research", "opportunity"],
        "summary": "Structure the initial customer discovery phase to understand operational context, pain points, and outcome ambitions before any solution is proposed.",
        "outcomes": [
            "Customer discovery interview guide",
            "Operational baseline documentation",
            "Pain point and opportunity register",
            "Discovery-to-design handover pack"
        ],
        "parameters": {
            "customer_name": "Customer organisation name and industry",
            "asset_category": "Category of assets under discussion",
            "discovery_scope": "Scope of discovery — single site, division, or enterprise"
        }
    },
    {
        "code": "A1.4", "slug": "e2e-design-blueprint",
        "name": "Design Blueprint", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.4-design-blueprint.md",
        "stage": "Discover", "layer": "Front Office", "role": "Solution Designer",
        "tags": ["solution", "design", "sla", "outcome-model"],
        "summary": "Translate discovery findings into a structured EaaS solution concept — defining the outcome model, asset scope, SLA framework, and service wrapper before commercial development begins.",
        "outcomes": [
            "EaaS solution concept document",
            "Outcome model definition",
            "Asset scope and SLA framework",
            "Design-to-deal handover pack"
        ],
        "parameters": {
            "discovery_findings": "Summary of discovery phase findings and customer pain points",
            "asset_scope": "Assets to be included in the EaaS solution",
            "outcome_targets": "Customer-desired outcomes and measurable KPIs"
        }
    },
    {
        "code": "A1.5", "slug": "e2e-stakeholder-alignment",
        "name": "Stakeholder Alignment", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.5-stakeholder-alignment.md",
        "stage": "Discover", "layer": "Front Office", "role": "Account Executive",
        "tags": ["stakeholders", "sales", "champion", "approval", "decision-making"],
        "summary": "Map the customer decision-making unit, understand each stakeholder's priorities, and build the internal coalition needed to approve and sustain an EaaS contract.",
        "outcomes": [
            "Stakeholder map and influence analysis",
            "Champion identification and engagement plan",
            "Objection register with response playbook",
            "Internal approval pathway documentation"
        ],
        "parameters": {
            "customer_organisation": "Customer organisation and deal context",
            "known_stakeholders": "Names and roles of known stakeholders",
            "deal_size": "Approximate contract value and term"
        }
    },
    {
        "code": "A1.6", "slug": "e2e-product-assessment",
        "name": "EaaS Product Assessment", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.6-product-assessment.md",
        "stage": "Discover", "layer": "Back Office", "role": "Product Manager",
        "tags": ["product", "portfolio", "suitability", "assessment", "scoring"],
        "summary": "Evaluate which products in your portfolio are structurally suited to EaaS — and which are not — using a scoring model across seven dimensions.",
        "outcomes": [
            "Product EaaS suitability scorecard",
            "Portfolio prioritisation for EaaS conversion",
            "Product readiness gap analysis",
            "Recommended pilot product selection"
        ],
        "parameters": {
            "product_list": "Products or product lines to assess",
            "market_context": "Target market and customer segments",
            "strategic_priorities": "Business priorities driving EaaS transition"
        }
    },
    {
        "code": "A1.7", "slug": "e2e-challenge-prioritisation",
        "name": "Challenge Prioritisation", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.7-challenge-prioritisation.md",
        "stage": "Discover", "layer": "Back Office", "role": "Strategy Lead",
        "tags": ["barriers", "challenges", "prioritisation", "transformation"],
        "summary": "Identify and rank the internal and external barriers to EaaS transition so leadership can allocate resources to the challenges that matter most.",
        "outcomes": [
            "EaaS barrier register with severity ratings",
            "Prioritised challenge roadmap",
            "Resource allocation recommendations",
            "Executive challenge briefing"
        ],
        "parameters": {
            "organisation_context": "Organisation size, industry, and current business model",
            "eaas_ambition": "Target EaaS scale — pilot, division, or full portfolio",
            "known_blockers": "Any known blockers or constraints already identified"
        }
    },
    {
        "code": "A1.8", "slug": "e2e-customer-segmentation",
        "name": "Customer Segmentation", "new": False,
        "group": "A1 · Strategy & Discovery", "group_folder": "A1-strategy-discovery",
        "file": "A1.8-customer-segmentation.md",
        "stage": "Discover", "layer": "Front Office", "role": "Commercial Director",
        "tags": ["segmentation", "icp", "targeting", "commercial", "gtm"],
        "summary": "Identify which customer segments are the best candidates for EaaS — based on operational maturity, contract appetite, and outcome alignment — to focus sales effort where conversion is highest.",
        "outcomes": [
            "EaaS customer segmentation model",
            "Ideal Customer Profile for EaaS",
            "Segment-specific value proposition",
            "Target account list and prioritisation"
        ],
        "parameters": {
            "current_customer_base": "Description of existing customers and market",
            "product_focus": "Products or asset categories to lead with",
            "sales_capacity": "Available sales headcount and territory coverage"
        }
    },
    # A2 · Solution Design
    {
        "code": "A2.1", "slug": "e2e-baseline-journey-mapping",
        "name": "Baseline Journey Mapping", "new": False,
        "group": "A2 · Solution Design", "group_folder": "A2-solution-design",
        "file": "A2.1-baseline-journey-mapping.md",
        "stage": "Order", "layer": "Front Office", "role": "Service Designer",
        "tags": ["journey-mapping", "baseline", "customer-experience", "as-is"],
        "summary": "Document the customer's current asset ownership experience — from procurement through operation and disposal — to establish the baseline your EaaS model must improve on.",
        "outcomes": [
            "As-is customer journey map",
            "Pain point and cost hotspot analysis",
            "Value gap identification",
            "Baseline metrics for EaaS comparison"
        ],
        "parameters": {
            "customer_context": "Customer industry, asset types, and operational model",
            "journey_scope": "Scope of the journey to map (single asset, fleet, site, etc.)",
            "focus_pain_points": "Known pain points or cost areas to investigate"
        }
    },
    {
        "code": "A2.2", "slug": "e2e-service-design",
        "name": "EaaS Service Design", "new": False,
        "group": "A2 · Solution Design", "group_folder": "A2-solution-design",
        "file": "A2.2-service-design.md",
        "stage": "Order", "layer": "Middle Office", "role": "Service Designer",
        "tags": ["service-design", "outcome-model", "sla", "customer-experience"],
        "summary": "Design the complete EaaS service model — the outcome promise, service components, SLA structure, and customer experience — before commercial documentation begins.",
        "outcomes": [
            "EaaS service model canvas",
            "Outcome and SLA definition framework",
            "Service component architecture",
            "Customer experience specification"
        ],
        "parameters": {
            "asset_type": "Asset type and operational context",
            "outcome_targets": "Customer outcome ambitions and measurable KPIs",
            "service_wrapper": "Support, maintenance, and service components to include"
        }
    },
    {
        "code": "A2.3", "slug": "e2e-service-blueprint",
        "name": "Service Blueprint", "new": False,
        "group": "A2 · Solution Design", "group_folder": "A2-solution-design",
        "file": "A2.3-service-blueprint.md",
        "stage": "Order", "layer": "Middle Office", "role": "Operations Designer",
        "tags": ["service-blueprint", "operations", "process", "swimlane"],
        "summary": "Map the full operational model behind the EaaS promise — the frontstage customer interactions, backstage processes, and supporting systems that deliver the contracted outcome.",
        "outcomes": [
            "Full service blueprint with swim lanes",
            "Backstage process specifications",
            "Technology and system integration map",
            "Failure point and recovery protocol register"
        ],
        "parameters": {
            "service_model": "Summary of the EaaS service model to blueprint",
            "asset_type": "Asset type and deployment context",
            "operational_constraints": "Known operational constraints or non-negotiables"
        }
    },
    {
        "code": "A2.4", "slug": "e2e-capability-strategy",
        "name": "Capability Strategy", "new": False,
        "group": "A2 · Solution Design", "group_folder": "A2-solution-design",
        "file": "A2.4-capability-strategy.md",
        "stage": "Order", "layer": "Back Office", "role": "Operations Director",
        "tags": ["capability", "build-buy-partner", "operations", "scaling"],
        "summary": "Define the operational capabilities your organisation must build, buy, or partner for to deliver EaaS at scale — and sequence the capability build in line with contract pipeline.",
        "outcomes": [
            "EaaS capability maturity assessment",
            "Build/buy/partner decision framework",
            "Capability development roadmap",
            "Partner and supplier strategy"
        ],
        "parameters": {
            "current_capabilities": "Existing operational capabilities and gaps",
            "target_scale": "Target number of contracts and asset types",
            "timeline": "Timeline to first contract and scale targets"
        }
    },
    {
        "code": "A2.5", "slug": "e2e-implementation-blueprint",
        "name": "Implementation Blueprint", "new": False,
        "group": "A2 · Solution Design", "group_folder": "A2-solution-design",
        "file": "A2.5-implementation-blueprint.md",
        "stage": "Order", "layer": "Back Office", "role": "Programme Manager",
        "tags": ["implementation", "programme", "roadmap", "go-live", "change-management"],
        "summary": "Build the master programme plan for EaaS transition — covering technology, operations, commercial, and change management workstreams from design through to first contract go-live.",
        "outcomes": [
            "EaaS transition programme plan",
            "Workstream structure and ownership",
            "Milestone and dependency map",
            "Go-live readiness criteria"
        ],
        "parameters": {
            "organisation_context": "Organisation size, industry, and current state",
            "first_contract_target": "Target date and scope for first EaaS contract",
            "constraints": "Budget, headcount, and technology constraints"
        }
    },
    # A3 · Business Case & Deal
    {
        "code": "A3.1", "slug": "e2e-business-case",
        "name": "Business Case", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.1-business-case.md",
        "stage": "Order", "layer": "Back Office", "role": "Commercial Director",
        "tags": ["business-case", "financial-model", "pl", "residual-value", "scenario"],
        "summary": "Build the full EaaS business case — P&L model, cash flow, residual value assumptions, and scenario analysis — to support internal investment approval and customer commercial negotiation.",
        "outcomes": [
            "EaaS contract P&L model",
            "Cash flow and working capital analysis",
            "Residual value and asset recovery model",
            "Scenario analysis (base / upside / downside)"
        ],
        "parameters": {
            "contract_value": "Estimated annual contract value and term",
            "asset_cost": "Asset acquisition or manufacturing cost",
            "service_cost_assumptions": "Expected maintenance, parts, and labour costs",
            "residual_value_assumption": "Expected asset residual value at contract end"
        }
    },
    {
        "code": "A3.2", "slug": "e2e-finance-case",
        "name": "Finance Case", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.2-finance-case.md",
        "stage": "Order", "layer": "Back Office", "role": "Finance Director",
        "tags": ["financing", "balance-sheet", "debt", "wacc", "capital-structure"],
        "summary": "Structure the financing model for EaaS asset deployment — evaluating balance sheet, off-balance sheet, and third-party financing options against the contract economics.",
        "outcomes": [
            "Financing structure options analysis",
            "Cost of capital and WACC impact assessment",
            "Debt covenants and lender requirements review",
            "Recommended financing structure with rationale"
        ],
        "parameters": {
            "asset_investment": "Total asset investment required for the contract portfolio",
            "contract_cashflows": "Expected monthly/annual cashflow profile",
            "balance_sheet_constraints": "Any balance sheet or leverage constraints",
            "financing_preferences": "Preference for on or off balance sheet treatment"
        }
    },
    {
        "code": "A3.3", "slug": "e2e-tendering-procedure",
        "name": "Tendering Procedure", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.3-tendering-procedure.md",
        "stage": "Order", "layer": "Front Office", "role": "Commercial Manager",
        "tags": ["tendering", "rfp", "bid", "procurement", "qualification"],
        "summary": "Manage the EaaS tendering process — from RFI/RFP response through to preferred bidder selection — with qualification criteria, scoring models, and negotiation strategy.",
        "outcomes": [
            "Tender qualification and bid/no-bid framework",
            "RFP response structure and content guide",
            "Evaluation scoring model",
            "Preferred bidder negotiation playbook"
        ],
        "parameters": {
            "tender_type": "Type of tender (RFI, RFP, ITT, competitive dialogue)",
            "customer_requirements": "Customer's stated requirements and evaluation criteria",
            "competitive_context": "Known competitors and competitive dynamics"
        }
    },
    {
        "code": "A3.4", "slug": "e2e-risk-assessment",
        "name": "Risk Assessment", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.4-risk-assessment.md",
        "stage": "Order", "layer": "Back Office", "role": "Risk Manager",
        "tags": ["risk", "contracts", "mitigation", "allocation", "scoring"],
        "summary": "Identify, score, and allocate the full risk register for an EaaS contract — covering technical, commercial, operational, and strategic risks — with mitigation strategies for each.",
        "outcomes": [
            "EaaS risk register with scoring matrix",
            "Risk allocation framework (provider vs customer)",
            "Mitigation strategy per risk category",
            "Residual risk acceptance criteria"
        ],
        "parameters": {
            "contract_context": "EaaS contract description, asset type, and customer",
            "contract_term": "Contract duration and scale",
            "risk_appetite": "Organisation's risk appetite and any known exposure limits"
        }
    },
    {
        "code": "A3.5", "slug": "e2e-internal-organisation",
        "name": "Internal Organisation", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.5-internal-organisation.md",
        "stage": "Order", "layer": "Back Office", "role": "Operations Director",
        "tags": ["governance", "organisation", "raci", "team-design", "centre-of-excellence"],
        "summary": "Design the governance structure, team composition, and decision-making cadences required to operate EaaS contracts reliably at scale.",
        "outcomes": [
            "EaaS organisational model and RACI",
            "Governance cadence and escalation framework",
            "Headcount and capability requirements by scale",
            "EaaS Centre of Excellence blueprint"
        ],
        "parameters": {
            "portfolio_size": "Current and target number of EaaS contracts",
            "existing_structure": "Current organisational structure and teams",
            "geographic_scope": "Single country or multi-country operation"
        }
    },
    {
        "code": "A3.6", "slug": "e2e-bid-preparation",
        "name": "Bid Preparation", "new": False,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.6-bid-preparation.md",
        "stage": "Order", "layer": "Front Office", "role": "Bid Manager",
        "tags": ["bid", "proposal", "win-themes", "differentiators", "review-gate"],
        "summary": "Produce a winning EaaS bid — structuring the technical, commercial, and legal response to maximise clarity, differentiation, and evaluator confidence.",
        "outcomes": [
            "Bid production process and ownership map",
            "Proposal structure and quality checklist",
            "Win theme and differentiator framework",
            "Review and approval gate process"
        ],
        "parameters": {
            "tender_requirements": "Customer's tender requirements and evaluation criteria",
            "win_themes": "Key differentiators and win themes to emphasise",
            "submission_deadline": "Bid submission deadline and page limits"
        }
    },
    {
        "code": "A3.7", "slug": "e2e-digital-contracting-platform",
        "name": "Digital Contracting Platform", "new": True,
        "group": "A3 · Business Case & Deal", "group_folder": "A3-business-case-deal",
        "file": "A3.7-digital-contracting-platform.md",
        "stage": "Order", "layer": "Shared Platforms", "role": "Technology Lead",
        "tags": ["digital-contracting", "platform", "automation", "iot", "billing"],
        "summary": "Specify and implement the digital contracting platform that manages EaaS contract data, automates obligation tracking, and integrates with IoT, CMMS, and billing systems.",
        "outcomes": [
            "Digital contracting platform specification",
            "EaaS contract data model",
            "System integration architecture",
            "Platform selection and implementation roadmap"
        ],
        "parameters": {
            "contract_portfolio": "Number and complexity of contracts to manage",
            "existing_systems": "Current CMMS, ERP, IoT, and billing systems",
            "automation_priorities": "Key automation priorities (billing, SLA, obligations)"
        }
    },
    # A4 · Operations & Capability
    {
        "code": "A4.1", "slug": "e2e-machine-delivery",
        "name": "Machine Delivery & Installation", "new": False,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.1-machine-delivery.md",
        "stage": "Deliver", "layer": "Back Office", "role": "Operations Manager",
        "tags": ["delivery", "installation", "commissioning", "fat", "go-live"],
        "summary": "Manage the full asset delivery lifecycle — from pre-delivery planning through transport, installation, commissioning, and operator training — with SLA clock starting at go-live.",
        "outcomes": [
            "Delivery and installation project plan",
            "Site readiness checklist and acceptance criteria",
            "Commissioning and FAT protocol",
            "Operator training completion sign-off"
        ],
        "parameters": {
            "asset_type": "Asset type and technical specifications",
            "site_context": "Customer site characteristics and access constraints",
            "go_live_date": "Target go-live date and SLA start"
        }
    },
    {
        "code": "A4.2", "slug": "e2e-customer-onboarding",
        "name": "Customer Onboarding", "new": True,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.2-customer-onboarding.md",
        "stage": "Deliver", "layer": "Front Office", "role": "Customer Success Manager",
        "tags": ["onboarding", "customer-success", "training", "90-day", "go-live"],
        "summary": "Deliver a structured 90-day onboarding programme that establishes the people, processes, and systems needed for a successful EaaS contract from day one.",
        "outcomes": [
            "Onboarding programme plan (Week 1 through Month 3)",
            "Stakeholder engagement and training schedule",
            "Systems access and integration checklist",
            "90-day onboarding completion assessment"
        ],
        "parameters": {
            "customer_context": "Customer organisation, site, and key contacts",
            "asset_scope": "Assets being onboarded and operational context",
            "go_live_date": "Contract go-live date"
        }
    },
    {
        "code": "A4.3", "slug": "e2e-customer-success",
        "name": "Customer Success", "new": False,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.3-customer-success.md",
        "stage": "Support", "layer": "Front Office", "role": "Customer Success Manager",
        "tags": ["customer-success", "renewal", "nps", "account-health", "churn"],
        "summary": "Manage the ongoing customer relationship to maximise satisfaction, prevent churn, and build the commercial conditions for contract renewal and expansion.",
        "outcomes": [
            "Account health scoring framework",
            "Customer engagement cadence (monthly/quarterly/annual)",
            "Value communication and reporting toolkit",
            "Renewal playbook with 18-month timeline"
        ],
        "parameters": {
            "account_name": "Customer account name and contract details",
            "account_health": "Current account health indicators (NPS, CSAT, SLA performance)",
            "renewal_date": "Contract renewal date"
        }
    },
    {
        "code": "A4.4", "slug": "e2e-contract-clause-bank",
        "name": "Contract Clause Bank", "new": False,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.4-contract-clause-bank.md",
        "stage": "Order", "layer": "Back Office", "role": "Legal Counsel",
        "tags": ["contract", "clauses", "legal", "sla", "liability", "termination"],
        "summary": "Access a structured library of EaaS-specific contract clauses covering SLA, asset ownership, liability, data, force majeure, and termination — with guidance on risk allocation.",
        "outcomes": [
            "EaaS clause library across 7 modules",
            "Clause risk rating and negotiation guidance",
            "Customer-friendly vs provider-protective variants",
            "Contract review and gap analysis checklist"
        ],
        "parameters": {
            "contract_type": "Type of EaaS contract and jurisdiction",
            "negotiation_context": "Negotiation stage and counterparty position",
            "risk_allocation": "Provider vs customer risk allocation preferences"
        }
    },
    {
        "code": "A4.5", "slug": "e2e-managing-contracts",
        "name": "Managing Contracts", "new": False,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.5-managing-contracts.md",
        "stage": "Support", "layer": "Middle Office", "role": "Contract Manager",
        "tags": ["contract-management", "obligations", "invoicing", "variations", "disputes"],
        "summary": "Operate live EaaS contracts with rigour — tracking obligations, managing variations, processing invoices, resolving disputes, and maintaining audit-ready records.",
        "outcomes": [
            "Contract obligation tracker and alert system",
            "Change management process (5-step)",
            "Invoice and credit note workflow",
            "Dispute resolution and escalation protocol"
        ],
        "parameters": {
            "contract_reference": "Contract reference and key terms",
            "management_challenge": "Specific contract management challenge or task",
            "period": "Reporting or management period"
        }
    },
    {
        "code": "A4.6", "slug": "e2e-mro-service",
        "name": "MRO Service", "new": False,
        "group": "A4 · Operations & Capability", "group_folder": "A4-operations-capability",
        "file": "A4.6-mro-service.md",
        "stage": "Support", "layer": "Back Office", "role": "Field Service Manager",
        "tags": ["mro", "maintenance", "field-service", "mttr", "mtbf", "spare-parts"],
        "summary": "Deliver preventive and reactive maintenance operations that protect SLA performance and residual asset value — with KPI-driven field service and parts management.",
        "outcomes": [
            "PM and reactive maintenance playbook",
            "MRO KPI framework (MTTR, MTBF, First-Time Fix)",
            "Spare parts strategy and inventory model",
            "Field service dispatch and routing process"
        ],
        "parameters": {
            "asset_type": "Asset type and failure mode profile",
            "fleet_size": "Number of assets under maintenance",
            "sla_requirements": "SLA uptime and response time requirements"
        }
    },
    # A5 · Performance Management
    {
        "code": "A5.1", "slug": "e2e-analytics-esg-dashboards",
        "name": "Analytics & ESG Dashboards", "new": True,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.1-analytics-esg-dashboards.md",
        "stage": "Support", "layer": "Shared Platforms", "role": "Data & Sustainability Lead",
        "tags": ["analytics", "esg", "dashboards", "reporting", "sustainability", "kpi"],
        "summary": "Design and deploy the three-tier dashboard architecture that gives operations, customers, and leadership real-time visibility of performance, value, and ESG outcomes.",
        "outcomes": [
            "Operational, customer, and ESG dashboard specifications",
            "ESG measurement framework (energy, circular economy, social)",
            "Data pipeline and update frequency architecture",
            "Dashboard governance and access control model"
        ],
        "parameters": {
            "audience": "Primary dashboard audience (operations, customers, leadership, investors)",
            "asset_type": "Asset type and performance KPIs to display",
            "esg_scope": "ESG reporting scope (energy, emissions, circular economy, social)"
        }
    },
    {
        "code": "A5.2", "slug": "e2e-continuous-improvement",
        "name": "Continuous Improvement", "new": True,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.2-continuous-improvement.md",
        "stage": "Improve", "layer": "Middle Office", "role": "Operations Manager",
        "tags": ["continuous-improvement", "pdca", "reliability", "margin", "analytics"],
        "summary": "Run a structured PDCA improvement programme that prevents margin erosion, reduces reactive maintenance, and compounds reliability gains across the EaaS portfolio over time.",
        "outcomes": [
            "Continuous improvement action register",
            "Monthly performance variance analysis process",
            "Improvement ROI tracker",
            "Technology improvement roadmap (predictive analytics)"
        ],
        "parameters": {
            "portfolio_context": "Contract portfolio size and asset types",
            "performance_data": "Current KPI performance vs targets",
            "improvement_focus": "Priority improvement areas (cost, reliability, SLA)"
        }
    },
    {
        "code": "A5.3", "slug": "e2e-customer-feedback",
        "name": "Customer Feedback", "new": False,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.3-customer-feedback.md",
        "stage": "Improve", "layer": "Front Office", "role": "Customer Success Manager",
        "tags": ["feedback", "nps", "csat", "ces", "renewal-intent", "voice-of-customer"],
        "summary": "Collect, analyse, and act on customer sentiment across transactional, relationship, and unsolicited channels — with NPS, CSAT, and renewal intent as the core metrics.",
        "outcomes": [
            "Transactional and relationship feedback framework",
            "NPS and CSAT measurement programme",
            "Close-the-loop process (acknowledge → act → confirm)",
            "Renewal risk flag report"
        ],
        "parameters": {
            "account_portfolio": "Accounts to include in feedback programme",
            "feedback_trigger": "Specific feedback trigger or programme design request",
            "current_metrics": "Current NPS, CSAT, or satisfaction data if available"
        }
    },
    {
        "code": "A5.4", "slug": "e2e-performance-monitoring",
        "name": "Performance Monitoring", "new": False,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.4-performance-monitoring.md",
        "stage": "Support", "layer": "Middle Office", "role": "Contract Manager",
        "tags": ["performance", "monitoring", "sla", "kpi", "compliance", "telemetry"],
        "summary": "Measure EaaS asset and service KPIs with precision — from IoT data collection through SLA compliance determination and the monthly performance certificate.",
        "outcomes": [
            "KPI measurement protocols (availability, output, efficiency)",
            "SLA compliance determination process",
            "Dispute-proofing monitoring framework",
            "Monthly SLA compliance certificate"
        ],
        "parameters": {
            "contract_kpis": "KPIs and SLA targets defined in the contract",
            "measurement_period": "Measurement period (month, quarter)",
            "data_sources": "IoT, CMMS, and other data sources available"
        }
    },
    {
        "code": "A5.5", "slug": "e2e-iot-smart-contracts",
        "name": "IoT & Smart Contracts", "new": True,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.5-iot-smart-contracts.md",
        "stage": "Support", "layer": "Shared Platforms", "role": "Technology Lead",
        "tags": ["iot", "smart-contracts", "automation", "telemetry", "billing", "sensors"],
        "summary": "Integrate real-time asset telemetry with automated contract execution — so performance data triggers SLA validation, payment calculation, and operational alerts without manual intervention.",
        "outcomes": [
            "IoT architecture specification (sensor, connectivity, platform)",
            "Smart contract trigger logic rules",
            "Automated payment run process",
            "IoT security audit framework"
        ],
        "parameters": {
            "asset_type": "Asset type and performance KPIs to instrument",
            "existing_iot": "Existing IoT infrastructure and connectivity",
            "automation_scope": "Automation scope (billing, alerts, work orders, all)"
        }
    },
    {
        "code": "A5.6", "slug": "e2e-return-refurbishment",
        "name": "Return & Refurbishment", "new": False,
        "group": "A5 · Performance Management", "group_folder": "A5-performance-management",
        "file": "A5.6-return-refurbishment.md",
        "stage": "Improve", "layer": "Back Office", "role": "Asset Manager",
        "tags": ["return", "refurbishment", "residual-value", "circular-economy", "esg", "asset-lifecycle"],
        "summary": "Manage end-of-contract asset return, condition assessment, refurbishment, and residual value realisation to close the circular economy loop of every EaaS contract.",
        "outcomes": [
            "End-of-contract asset disposition plan",
            "Condition assessment and grading protocol (Grade A–D)",
            "Refurbishment scope by condition grade",
            "Circular economy ESG impact report"
        ],
        "parameters": {
            "asset_type": "Asset type and age at contract end",
            "condition_data": "Available condition and maintenance history data",
            "disposition_options": "Available disposition routes (redeploy, sell, dismantle)"
        }
    },
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
VERSION = "1.24.0"
AUTHOR = "Luis Prato"
LICENSE = "Apache-2.0"


def skill_path(skill: dict) -> Path:
    """Return the directory path for a skill."""
    folder = skill["file"].replace(".md", "")
    return SKILLS_ROOT / skill["group_folder"] / folder


def fn_name(skill: dict) -> str:
    """Safe function name for OpenAI/Gemini tool definitions."""
    return skill["slug"].replace("-", "_")


def build_skill_json(skill: dict) -> dict:
    return {
        "schema": "eaas-skill/1.0",
        "code": skill["code"],
        "slug": skill["slug"],
        "name": skill["name"],
        "fullName": f"{skill['code']} {skill['name']}",
        "group": skill["group"],
        "category": "EaaS E2E Operating Model",
        "version": VERSION,
        "new": skill["new"],
        "stage": skill["stage"],
        "layer": skill["layer"],
        "role": skill["role"],
        "tags": skill["tags"],
        "summary": skill["summary"],
        "outcomes": skill["outcomes"],
        "author": AUTHOR,
        "license": LICENSE,
        "formats": {
            "skill_md": "SKILL.md",
            "openai": "formats/openai.json",
            "gemini": "formats/gemini.json",
            "cursor": "formats/cursor.md",
            "generic": "formats/generic.md"
        }
    }


def build_openai_json(skill: dict) -> dict:
    """OpenAI Agents SDK / function calling tool definition."""
    props = {k: {"type": "string", "description": v} for k, v in skill["parameters"].items()}
    props["output_format"] = {
        "type": "string",
        "enum": ["structured_deliverable", "executive_summary", "action_register", "detailed_report"],
        "description": "Desired output format",
        "default": "structured_deliverable"
    }
    return {
        "type": "function",
        "function": {
            "name": fn_name(skill),
            "description": (
                f"[EaaS E2E Operating Model — {skill['code']} {skill['name']}] "
                f"{skill['summary']} "
                f"Outputs: {'; '.join(skill['outcomes'])}."
            ),
            "parameters": {
                "type": "object",
                "properties": props,
                "required": list(skill["parameters"].keys())[:1]
            }
        },
        "metadata": {
            "skill_version": VERSION,
            "group": skill["group"],
            "role": skill["role"],
            "tags": skill["tags"],
            "source": f"https://github.com/luis-prato/eaas-skills/tree/main/skills/{skill['group_folder']}/{skill['file'].replace('.md', '')}"
        }
    }


def build_gemini_json(skill: dict) -> dict:
    """Google Gemini function calling / Extensions format."""
    props = {}
    for k, v in skill["parameters"].items():
        props[k] = {"type": "STRING", "description": v}
    props["output_format"] = {
        "type": "STRING",
        "description": "Desired output: structured_deliverable | executive_summary | action_register | detailed_report",
    }
    return {
        "name": fn_name(skill),
        "description": (
            f"EaaS E2E Operating Model — {skill['code']} {skill['name']}. "
            f"{skill['summary']}"
        ),
        "parameters": {
            "type": "OBJECT",
            "properties": props,
            "required": list(skill["parameters"].keys())[:1]
        },
        "metadata": {
            "skill_code": skill["code"],
            "skill_group": skill["group"],
            "skill_role": skill["role"],
            "skill_version": VERSION,
            "skill_tags": skill["tags"]
        }
    }


def build_generic_md(skill: dict, skill_md_content: str) -> str:
    """Clean markdown for any platform — strips EaaS-specific header, adds install note."""
    header = f"""# {skill['code']} — {skill['name']}

> **EaaS E2E Operating Model** · Group: {skill['group']} · Role: {skill['role']}
> Version: {VERSION} · License: {LICENSE} · Author: {AUTHOR}

**Summary:** {skill['summary']}

**Key Outcomes:**
{chr(10).join(f'- {o}' for o in skill['outcomes'])}

---

"""
    # Strip the original header lines (everything up to the first ## heading)
    body_lines = skill_md_content.split("\n")
    body_start = 0
    for i, line in enumerate(body_lines):
        if line.startswith("## "):
            body_start = i
            break
    body = "\n".join(body_lines[body_start:])

    footer = f"""
---

*Source: [EaaS Skills Library](https://github.com/luis-prato/eaas-skills) · {skill['code']} {skill['name']} · v{VERSION}*
"""
    return header + body + footer


def build_cursor_md(skill_md_content: str, skill: dict) -> str:
    """Cursor rules format — SKILL.md content with a Cursor-specific frontmatter block."""
    frontmatter = f"""---
description: "{skill['code']} {skill['name']} — {skill['summary'][:100]}..."
globs: ["**/*.ts", "**/*.py", "**/*.js", "**/*.md"]
alwaysApply: false
---

"""
    return frontmatter + skill_md_content


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------

def generate_all():
    manifest_skills = []
    total_generated = 0

    for skill in SKILLS:
        skill_dir = skill_path(skill)
        skill_dir.mkdir(parents=True, exist_ok=True)

        # Read SKILL.md
        skill_md_path = SKILLS_ROOT / skill["group_folder"] / skill["file"]
        if not skill_md_path.exists():
            print(f"  ⚠  SKILL.md missing: {skill_md_path}")
            continue

        skill_md_content = skill_md_path.read_text(encoding="utf-8")

        # Move SKILL.md into skill directory if not already there
        dest_skill_md = skill_dir / "SKILL.md"
        if not dest_skill_md.exists():
            dest_skill_md.write_text(skill_md_content, encoding="utf-8")

        # skill.json
        skill_json_path = skill_dir / "skill.json"
        skill_json_path.write_text(
            json.dumps(build_skill_json(skill), indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # formats/ directory
        formats_dir = skill_dir / "formats"
        formats_dir.mkdir(exist_ok=True)

        # formats/openai.json
        (formats_dir / "openai.json").write_text(
            json.dumps(build_openai_json(skill), indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # formats/gemini.json
        (formats_dir / "gemini.json").write_text(
            json.dumps(build_gemini_json(skill), indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # formats/cursor.md
        (formats_dir / "cursor.md").write_text(
            build_cursor_md(skill_md_content, skill),
            encoding="utf-8"
        )

        # formats/generic.md
        (formats_dir / "generic.md").write_text(
            build_generic_md(skill, skill_md_content),
            encoding="utf-8"
        )

        manifest_skills.append({
            "code": skill["code"],
            "slug": skill["slug"],
            "name": skill["name"],
            "group": skill["group"],
            "role": skill["role"],
            "new": skill["new"],
            "path": f"skills/{skill['group_folder']}/{skill['file'].replace('.md', '')}",
            "formats": ["SKILL.md", "skill.json", "formats/openai.json", "formats/gemini.json", "formats/cursor.md", "formats/generic.md"]
        })

        total_generated += 1
        print(f"  ✓  {skill['code']} {skill['name']}")

    # Root manifest.json
    manifest = {
        "schema": "eaas-skill-manifest/1.0",
        "name": "EaaS E2E Operating Model",
        "description": "32 skills covering the complete Equipment-as-a-Service end-to-end operating model — from strategy and discovery through performance management and asset return.",
        "version": VERSION,
        "author": AUTHOR,
        "license": LICENSE,
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repository": "https://github.com/luis-prato/eaas-skills",
        "total_skills": len(manifest_skills),
        "groups": [
            "A1 · Strategy & Discovery",
            "A2 · Solution Design",
            "A3 · Business Case & Deal",
            "A4 · Operations & Capability",
            "A5 · Performance Management"
        ],
        "platforms": {
            "claude_code": "SKILL.md",
            "cursor": "formats/cursor.md",
            "openai_agents": "formats/openai.json",
            "gemini": "formats/gemini.json",
            "generic": "formats/generic.md"
        },
        "skills": manifest_skills
    }

    manifest_path = REPO_ROOT / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\n✅  Generated {total_generated} skills + manifest.json")
    print(f"    Files per skill: SKILL.md · skill.json · formats/ (openai · gemini · cursor · generic)")


if __name__ == "__main__":
    print("EaaS Skills — Format Generator\n")
    generate_all()
