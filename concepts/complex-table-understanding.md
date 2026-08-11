---
title: "Complex Table Understanding"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[table-serialization]]", "[[table-structure-recognition]]"]
updated: 2026-08-11
---

# Complex Table Understanding

## What it is
Complex table understanding is question answering and reasoning over tables whose layout is not a clean grid — hierarchical or bidirectional headers, merged cells, nested groupings, and irregular non-canonical structure. The difficulty is that meaning is encoded in the layout itself, so a model must recover implicit logical structure before it can answer, especially for multi-hop queries combining lookup, filtering, and numerical aggregation. Sources converge on tree-structured intermediate representations and agentic or programmatic reasoning, and report where flat or rule-based approaches break down.

## How sources treat it
- **[[st-raptor]]** _(article · informational)_ — Names three failure modes of existing solutions on complex tables: flattening nested tables causes semantic loss and header–content misalignment; decomposing multi-level headers into flat tokens ignores hierarchy; and treating merged cells as NULL-filled sparse matrices breaks continuity; its Hierarchical Orthogonal Tree (HO-Tree) representation reportedly surpasses the best baseline by 11.2% on accuracy ⟨Why complex tables are hard; Evaluation⟩
- **[[astra-table-qa]]** _(article · informational)_ — Identifies four challenges (Structural Neglect, Representation Gap, Reasoning Opacity, Schema Inflexibility) and reports SOTA via adaptive selection — AIT-QA 91.6%, SSTQA 81.9%, HiTab 90.1% — stating this beats reasoning model OpenAI o3 (85.3% on HiTab) and greatly exceeds rule-based ST-Raptor (AIT-QA 62.7%, HiTab 49.0%) ⟨§1; §4.2, Table 2⟩
- **[[astra-table-qa]]** _(article · informational)_ — Reports a mode trade-off on its own system: Textual Reasoning beats Symbolic on semantically intensive SSTQA (79.8% vs 75.3%) while Symbolic beats Textual on numerical HiTab (89.3% vs 82.2%), with a lightweight Answer Selector choosing between candidates ⟨§4.2, Table 2; §3.4⟩
- **[[deep-tabular-research]]** _(article · informational)_ — Formalizes Deep Tabular Research as long-horizon multi-hop reasoning over unstructured tables with hierarchical/bidirectional headers and merged cells; reports its DTR agent (DeepSeek-V3) leading across Fact Checking, Numerical Reasoning, Structure Comprehension, and Data Analysis on RealHitBench, and strongest overall on its own DTR-Bench (500 QA pairs) ⟨Abstract; §4.1, Tables 1–2⟩

## Where sources differ
All three build a structured intermediate representation, but disagree on how it should be constructed and reasoned over. [[st-raptor]] builds its HO-Tree with a hybrid of rule-based matching and VLM reasoning, and offers a human-in-the-loop tree editor. [[astra-table-qa]] explicitly calls [[st-raptor]]'s reliance on rule-based/physical-layout construction "fragile" and instead synthesizes a semantic tree adaptively, degenerating to a shallow tree for flat tables, and reports the large accuracy gaps above as evidence. [[deep-tabular-research]] moves away from serialized text entirely toward a programmatic, DataFrame-based execution agent driven by accumulated experience, arguing serialization is limited by token constraints and imprecise numerics. The KB records these comparative claims as each paper's own; [[astra-table-qa]] and [[deep-tabular-research]] both reuse ST-Raptor's SSTQA benchmark, so their numbers sit on shared ground.

## See also
[[table-serialization]] · [[table-structure-recognition]] · [[agentic-extraction]] · [[vision-language-document-model]] · [[retrieval-augmented-generation]]
