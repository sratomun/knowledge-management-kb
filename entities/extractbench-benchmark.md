---
title: "ExtractBench benchmark"
type: entity
subtype: benchmark
aliases: []
tags: [doc-processing]
published: 2026-07
effective_from: 2026-07
effective_to: ongoing
status: current
concepts: ["[[schema-guided-extraction]]", "[[agentic-extraction]]", "[[structured-output-generation]]"]
sources: ["[[extractbench]]"]
updated: 2026-08-11
---

# ExtractBench benchmark

## What it is
ExtractBench is a benchmark for schema-guided enterprise document extraction, in which a system is given a document and a user-defined JSON Schema and must return schema-valid JSON with source evidence as grounding metadata. Its authors (from runllama.ai / LlamaIndex) state it is, to their knowledge, the first evaluation to report value accuracy, record completeness at scale, grounding, and measured cost together. (A separate, unrelated benchmark from Contextual AI shares the name.)

## Key facts
- Contains 370 enterprise documents (4,869 pages) across 8 business domains and 67 document types, each document type sharing exactly one schema ⟨[[extractbench]] Abstract; §2.2⟩.
- Tags every document along five independent axes — task challenge, perception challenge, table structure, length, and business domain (22 challenge tags) — so failures can be traced to a cause ⟨[[extractbench]] §2.2⟩.
- Scores value accuracy with an order-insensitive unified value F1 (records aligned by the Hungarian algorithm; normalized comparison, no numeric tolerance, no LLM judge) ⟨[[extractbench]] §2.4⟩.
- Reports two grounding metrics — word-level F1 (correct value plus box overlap at IoU 0.5) and page-level F1 (correct value plus source page) — scored only where box ground truth is human-verified ⟨[[extractbench]] §2.4⟩.
- Builds ground truth from three sources with different trust bases: cross-model agreement plus human review (real documents), by-construction values (synthetic long lists), and per-field human verification (scanned forms, yielding 169 human-verified documents, 84% of fields with a human-placed box) ⟨[[extractbench]] §2.3⟩.
- Evaluates 14 systems spanning commercial/self-hosted VLMs, coding agents, and specialized APIs, without benchmark-specific tuning ⟨[[extractbench]] §3.1⟩.
- The authors report per-page cost spanning roughly 0.2¢–34¢ across systems, and that their own LlamaExtract Agentic Plus ranks first on all three metrics (95.6% overall value F1 at 8.1 ¢/page) versus coding agents at 16.2–27.8 ¢/page — a vendor-authored comparative claim ⟨[[extractbench]] Abstract; §3.2⟩.
- The authors report that even the best word-level grounding F1 is only 46.4%, and that VLMs and coding agents return no evidence by default and so score zero on grounding — described as an open problem ⟨[[extractbench]] §3.4; Table 3⟩.

## Relations
- Realizes: [[schema-guided-extraction]] · [[agentic-extraction]] · [[structured-output-generation]]
- Defined in: [[extractbench]]

## See also
[[schema-guided-extraction]] · [[agentic-extraction]] · [[structured-output-generation]] · [[extractbench]]
