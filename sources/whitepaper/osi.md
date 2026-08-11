---
title: "Open Semantic Interchange (OSI)"
type: source
kind: whitepaper
authority: informational
subtype: emerging-standard
aliases: ["OSI", "Open Semantic Interchange"]
publisher: Snowflake
url: https://www.snowflake.com/en/blog/open-semantic-interchange-ai-standard/
version: "announced 2025; spec finalized"
published: 2025-09
effective_from: 2025-09
effective_to: ongoing
status: current
tags: [semantic-layer]
updated: 2026-08-10
---

# Open Semantic Interchange (OSI)

## Scope & purpose
Open Semantic Interchange (OSI) is a collaborative, open-source industry initiative, announced by Snowflake on Sep 23, 2025, to define a vendor-neutral open standard (specification) for exchanging semantic-layer models — the business definitions of metrics, dimensions, and relationships — consistently across data analytics, AI, and BI tools. Its stated purpose is to give data definitions a single, consistent source of truth as they move between AI agents, BI platforms, catalog/governance products, and agentic applications, eliminating the inconsistency caused by definitions locked in proprietary silos. These pages are Snowflake's corporate blog posts (an informational vendor source), so claims reflect the initiative's own framing rather than an independently ratified standard.

## Structure
Two Snowflake blog posts are the ingested source: the Sep 23, 2025 announcement (the OSI vision, member charter principles, targeted outcomes, and core proposal) and the Jan 27, 2026 update (the first spec version going live under Apache 2, an expanded working group, a project website launch, and a planned move to foundation-led governance). The OSI program itself is scoped around an OSI model (semantic metadata in a standardized YAML format) plus participant-specific mapping and read/write code modules.

## Key points
- OSI is a collaborative, open-source initiative to standardize and streamline semantic model exchange across the data analytics, AI, and BI ecosystem. ⟨osi: announce §A Common Semantic Standard⟩
- Snowflake framed OSI as solving a foundational AI challenge — the lack of a common semantic standard — with the industry "coming together, not competing." ⟨osi: announce §intro / Kleinerman quote⟩
- The shared vision is a common, vendor-agnostic semantic model specification and query API acting as a single, consistent source of truth for data definitions across AI agents, BI platforms, and other tools. ⟨osi: announce §A Common Semantic Standard⟩
- The OSI member charter rests on five principles: Standardization, Interoperability, Extensibility, Open Source, and Domain-Specific Models. ⟨osi: announce §Key Principles⟩
- Targeted outcomes are Improved AI/BI Adoption, Streamlined Data Operations, and Vendor Neutrality (independence from any specific data platform, AI tool, or BI vendor). ⟨osi: announce §Transformative Outcomes⟩
- The core deliverable is an OSI model specifying semantic metadata in a standardized YAML format, plus participant-specific mapping and read/write code modules delivered as an Apache open-source project. ⟨osi: announce §Core Proposal⟩
- Founding ecosystem partners included Alation, Atlan, BlackRock, Blue Yonder, Cube, dbt Labs, Elementum AI, Hex, Honeydew, Mistral AI, Omni, RelationalAI, Salesforce, Select Star, Sigma, and ThoughtSpot. ⟨osi: announce §intro⟩
- The problem OSI targets: business logic and definitions such as churn rate or net margin have been locked inside proprietary silos, forcing teams to rebuild the same semantic context repeatedly. ⟨osi: specs §intro⟩
- On Jan 27, 2026, the first version of the OSI specification went live in an Apache 2 licensed Git repository at github.com/open-semantic-interchange/OSI. ⟨osi: specs §The OSI specification is live⟩
- The spec defines a vendor-neutral, extensible model for semantic-layer constructs — data sets, metrics, dimensions, relationships, and contexts — interpretable across tools, platforms, and agentic applications, and is described as a starting point shaped by community contribution. ⟨osi: specs §The OSI specification is live⟩
- New working group members added since launch: AtScale, Coalesce, Collate, Credible, Databricks, JetBrains, Lightdash, and Qlik, joining an expanded roster that also includes Collibra, DataHub, Domo, Firebolt, Informatica, Instacart, Preset, and Starburst Data and Strategy. ⟨osi: specs §A powerhouse ecosystem⟩
- A dedicated project website launched at open-semantic-interchange.org, hosting the spec, a working group member directory, and community updates. ⟨osi: specs §Launch of the OSI website⟩
- OSI states it will transition to a neutral, foundation-led governance model as the initiative matures. ⟨osi: specs §Looking ahead⟩
- These claims come from Snowflake's corporate blog (an informational vendor source) and include forward-looking statements that are explicitly not commitments to deliver any product. ⟨osi: specs §Forward-looking statements⟩

## Concepts & entities covered
Concepts: [[semantic-layer]] · [[semantic-interoperability]] · [[metric-definition]]
Entities: [[osi-spec]] · [[org-snowflake]]
