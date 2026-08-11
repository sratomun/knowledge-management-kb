---
title: "Compliance checking"
type: concept
subtype: use-case-profile
aliases: []
tags: [knowledge-processing]
related: ["[[obligation-extraction]]", "[[regulatory-gap-detection]]", "[[rules-as-code]]"]
updated: 2026-08-10
---

# Compliance checking

## What it is
Compliance checking is the use case of determining whether an organization's policies and practices satisfy the obligations imposed by regulation — answering "where do we fall short of what the rules require?" It chains obligation extraction (what the regulation demands) with an alignment step against internal policy, and the output is a set of gaps or confirmations, ideally each grounded in a source provision. Which processing pattern fits depends on the nature of the source documents: regulatory corpora are high-normativity, high-volatility (continuous updates across fragmented jurisdictions), heavily cross-referenced, and provenance-critical because findings must be auditable. Those document-nature attributes — structure, normativity, volatility, sensitivity, provenance, lifecycle — condition how the pattern is realized.

## How sources treat it
- **[[de-jure-regulatory-rules]]** _(article · informational)_ — frames compliance checking as regulation-grounded LLM alignment, transforming raw regulatory documents (HIPAA, SEC Advisers Act, EU AI Act) into structured, machine-readable rule sets so systems can be aligned with codified obligations, not just human preferences ⟨abstract, §1⟩
- **[[de-jure-regulatory-rules]]** _(article · informational)_ — reports that in a downstream compliance-QA-via-RAG comparison on HIPAA, De Jure-grounded responses were preferred by a judge LLM in 73.8% of cases at k=1, rising to 84.0% at k=10 ⟨abstract, §4.4, Table 4⟩
- **[[compliancenlp-gap-detection]]** _(article · informational)_ — presents an end-to-end system that monitors regulatory changes, extracts structured obligations, and maps them to institutional policies with severity-aware scoring to flag COMPLIANT / PARTIAL GAP / FULL GAP across SEC, MiFID II, and Basel III ⟨abstract, §3⟩
- **[[compliancenlp-gap-detection]]** _(article · informational)_ — frames the system as a decision-support tool that augments human professionals, with all high-severity findings requiring human review and full audit trails, stating it should not be the sole basis for compliance decisions ⟨Ethical Considerations⟩

## Where sources differ
Both sources build compliance checking on structured obligation extraction but emphasize different stages. [[de-jure-regulatory-rules]] centers on the *extraction and quality-assurance* half — an annotation-free, judge-refined pipeline producing auditable rule sets — and demonstrates compliance QA as a downstream application. [[compliancenlp-gap-detection]] centers on the *gap-detection and deployment* half — a knowledge-graph-augmented RAG system with severity scoring, production-latency optimization, and a reported multi-month parallel run. One stresses domain-agnostic, human-annotation-free extraction; the other stresses structural (graph) knowledge for cross-reference-heavy matching and operational deployment. Each paper's comparative claims are attributed to its authors on its own page.

## See also
[[obligation-extraction]] · [[regulatory-gap-detection]] · [[rules-as-code]]
