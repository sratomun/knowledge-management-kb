---
title: "Table Serialization"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[complex-table-understanding]]", "[[table-structure-recognition]]"]
updated: 2026-08-11
---

# Table Serialization

## What it is
Table serialization is the step that converts a two-dimensional table into a one-dimensional representation an LLM can consume — flattened text, markdown, a tree, relational triples, or a programmatic skeleton. Because LLMs process sequences, the choice of serialization determines how much of the table's structure and semantics survive. Sources treat serialization as a primary bottleneck for table QA and propose structure-preserving alternatives (semantic/logical trees, meta-graphs) to naive flattening, reporting how representation choice alone shifts accuracy.

## How sources treat it
- **[[astra-table-qa]]** _(article · informational)_ — Treats serialization (converting a 2D table into a sequence an LLM can consume) as the critical TableQA bottleneck and reports that its Semantic Tree representation alone, under direct prompting, reaches 70.55% vs 63.20% for textual serialization (+7.35), read as an intrinsic benefit of hierarchical serialization independent of the reasoning mechanism ⟨Abstract; §4.3, Table 4⟩
- **[[astra-table-qa]]** _(article · informational)_ — Selects among serialization modes by table scale/token density — Direct Semantic Parsing for moderate tables, Symbolic Reference Encoding with coordinate placeholders for verbose content, Programmatic Structure Synthesis for large repetitive tables — and reports an Evaluator-Guided loop triggered in only ~7% of cases, with removing it dropping average coverage 0.929 → 0.745 ⟨§3.2.2; §4.3–4.4, Table 3⟩
- **[[deep-tabular-research]]** _(article · informational)_ — Argues treating tables as serialized text is limited by token constraints and imprecise numerical operations over large irregular headers, motivating a programmatic DataFrame-based execution path; its structured [THINK]+[CODE] scheme reduces code error rate from 42.3% to 28.4% at the highest accuracy (37.5%) ⟨§1; §4.2, Table 4⟩
- **[[st-raptor]]** _(article · informational)_ — Its HO-Tree serialization is layout-aware, capturing relationships among headers, content cells, and merged regions, because flattening nested/hierarchical tables causes severe semantic loss and header–content misalignment and multi-level headers lose hierarchy when decomposed into flat token sequences ⟨Core approach; Why complex tables are hard⟩

## Where sources differ
The sources agree naive flattening loses structure but diverge on the replacement. [[st-raptor]] and [[astra-table-qa]] both use tree serializations, yet [[astra-table-qa]] calls [[st-raptor]]'s rule-based/physical-layout tree construction "fragile" and instead selects a serialization mode adaptively to table scale. [[deep-tabular-research]] rejects text serialization for complex analytical queries altogether, moving to a programmatic DataFrame representation and reporting the code-error-rate reduction above as evidence. So the divergence is over what an LLM should be handed: a semantic/logical tree ([[astra-table-qa]], [[st-raptor]]) versus executable code over structured data ([[deep-tabular-research]]) — with [[astra-table-qa]] also noting its own approach adds overhead on very simple flat tables.

## See also
[[complex-table-understanding]] · [[table-structure-recognition]] · [[agentic-extraction]] · [[vision-language-document-model]]
