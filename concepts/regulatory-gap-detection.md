---
title: "Regulatory gap detection"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[compliance-checking]]", "[[graphrag]]"]
updated: 2026-08-10
---

# Regulatory gap detection

## What it is
Regulatory gap detection is the practice of comparing extracted regulatory obligations against an organization's internal policies to find where the policies fail to meet, or only partially meet, the obligations. It is the analytical core of compliance checking: after obligations are extracted and structured, each is aligned to the corresponding internal clause and scored, producing labels such as compliant, partial gap, or full gap, often with a severity weighting and an audit trail. Because regulations change continuously and reference one another, gap detection is typically coupled with change monitoring and cross-reference resolution.

## How sources treat it
- **[[compliancenlp-gap-detection]]** _(article · informational)_ — presents an end-to-end system that monitors regulatory changes, extracts structured obligations, and identifies compliance gaps against institutional policies, representing each obligation as ⟨entity, action, modality, condition, source_provision⟩ and classifying aligned clauses as COMPLIANT, PARTIAL GAP, or FULL GAP ⟨abstract, §3.3⟩
- **[[compliancenlp-gap-detection]]** _(article · informational)_ — grounds retrieval in a Regulatory Knowledge Graph (12,847 provisions across SEC, MiFID II, Basel III) and re-ranks passages by KG proximity, reporting that removing KG re-ranking causes the largest ablation drop (−4.6 gap F1) ⟨abstract, §3.1, §6⟩
- **[[compliancenlp-gap-detection]]** _(article · informational)_ — reports grounding accuracy degrading with cross-reference complexity (97.1% at 0 references down to ~79% on nested conditional obligations), motivating mandatory analyst review for findings whose source obligation involves ≥3 cross-references ⟨§6.1⟩

## Where sources differ
Only one source treats regulatory gap detection directly, so the KB records no cross-source divergence. Its comparative claims — reaching 87.7 gap-detection F1 and outperforming GPT-4o+RAG by +3.5 F1, and the ablation results attributing the largest gain to knowledge-graph re-ranking — are reported as the authors' own benchmark and deployment findings, not as KB conclusions. The authors themselves frame the system as decision support requiring human review, not an autonomous compliance decider.

## See also
[[compliance-checking]] · [[graphrag]]
