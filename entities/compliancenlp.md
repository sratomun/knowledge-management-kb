---
title: "ComplianceNLP"
type: entity
subtype: system
aliases: []
tags: [knowledge-processing]
published: 2026
effective_from: 2026-04
effective_to: ongoing
status: current
concepts: ["[[regulatory-gap-detection]]", "[[compliance-checking]]"]
sources: ["[[compliancenlp-gap-detection]]"]
updated: 2026-08-10
---

# ComplianceNLP

## What it is
ComplianceNLP is an end-to-end knowledge-graph-augmented RAG system for multi-framework
regulatory gap detection that automatically monitors regulatory changes, extracts structured
obligations, and identifies compliance gaps against institutional policies across SEC, MiFID
II, and Basel III ⟨abstract, §1⟩.

## Key facts
- It integrates three components: a KG-augmented RAG pipeline over a Regulatory Knowledge Graph
  of 12,847 provisions, multi-task obligation extraction (NER + deontic classification +
  cross-reference resolution over a shared LEGAL-BERT encoder), and severity-aware compliance
  gap analysis ⟨abstract, §3⟩.
- It classifies each obligation–policy pair as COMPLIANT, PARTIAL GAP, or FULL GAP using a
  generator LLM, with thresholds δ=0.6 (evaluation) and δ=0.45 (recall-optimized deployment)
  ⟨§3.3⟩.
- The source paper reports 87.7 gap-detection F1 at δ=0.6, stated to outperform GPT-4o+RAG by
  +3.5 F1, with 94.2% grounding accuracy and 83.4 F1 under realistic end-to-end error
  propagation ⟨abstract, §6, Table 2⟩.
- The source paper's ablation reports that removing KG re-ranking causes the largest drop (−4.6
  gap F1), presented as evidence that structural regulatory knowledge is critical for
  cross-reference-heavy tasks ⟨abstract, §6⟩.
- For production latency it distills a LLaMA-3-70B teacher into an 8B student and adds Medusa
  speculative-decoding heads, with the source reporting a combined 2.8× speedup and 91.3%
  draft-token acceptance attributed to regulatory text's low entropy ⟨§4, §7.1⟩.
- The source paper reports four months of parallel-run deployment at a financial institution
  (9,847 updates) achieving an estimated 96.0% production recall and 90.7% precision with a
  3.1× sustained analyst efficiency gain ⟨§7, Table 4⟩.

## Relations
- Realizes / relates to: [[regulatory-gap-detection]] · [[compliance-checking]]
- Defined in: [[compliancenlp-gap-detection]]

## See also
[[compliancenlp-gap-detection]]
