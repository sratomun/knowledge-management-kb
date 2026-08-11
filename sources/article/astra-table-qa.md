---
title: "ASTRA: Adaptive Semantic Tree Reasoning Architecture for Complex Table Question Answering"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["ASTRA paper"]
publisher: arXiv
url: https://arxiv.org/abs/2604.08999
version: "arXiv:2604.08999v2 [cs.CL]"
published: 2026
effective_from: 2026-05
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]"]
entities: ["[[astra]]"]
updated: 2026-08-11
---

# ASTRA: Adaptive Semantic Tree Reasoning Architecture for Complex Table Question Answering

## Scope & purpose

ASTRA (Zhejiang University) is a training-free method for complex table question answering
that treats table serialization — converting a 2D table into a sequential representation an
LLM can consume — as the critical bottleneck for TableQA ⟨Abstract; §1⟩. It comprises two
modules: AdaSTR, which reconstructs a table into a Logical/Semantic Tree, and DuTR, a
dual-mode reasoning engine combining tree-search textual navigation with symbolic code
execution ⟨Abstract; §3.1⟩. The KB records the paper's SOTA and comparative claims
descriptively, preserving its stated hedges.

## Key points

- The paper identifies four serialization challenges for complex tables: Structural Neglect
  (LLMs overlook hierarchical relationships and semantic dependencies in layout),
  Representation Gap (the mismatch between 2D tables and the 1D sequential nature of LLMs
  hinders fine-grained evidence localization), Reasoning Opacity (direct LLM numeric
  computation is a black box that produces unverified numerical hallucinations), and Schema
  Inflexibility (rigid rule-based parsing fails to adapt to irregular layouts) ⟨§1⟩.
- It positions itself against prior families it says each address only some challenges:
  triple-based atomization (GraphOTTER) obscures explicit hierarchy; relational conversion
  (RelationalCoder) introduces redundancy/sparsity on asymmetric structures; and tree-based
  ST-Raptor's reliance on rule-based/physical-layout construction is called "fragile" and
  unable to discern physical hierarchy from semantic associations ⟨§1; §2.1; App D⟩.
- AdaSTR runs three stages: Header Identification & Normalization (consolidating vertical
  dependencies into qualified keys, e.g. merging "Yukon" with "Percent" → "Yukon-Percent"),
  Hierarchy Identification (mining hidden semantic groups into an explicit hierarchy), and
  adaptive tree synthesis, degenerating to a shallow tree for flat tables so overhead stays
  proportional to structural complexity ⟨§3.2.1⟩.
- Adaptive synthesis selects among three modes by table scale/token density: Direct Semantic
  Parsing (DSP) for moderate tables, Symbolic Reference Encoding (SRE) using coordinate
  placeholders for verbose-content tables, and Programmatic Structure Synthesis (PSS)
  generating a loop-based construction script for large repetitive tables ⟨§3.2.2⟩.
- An Evaluator-Guided Refinement Loop validates the tree via Structural Integrity (path
  consistency vs grid coordinates) and Information Coverage (percent of mapped cells), revising
  up to a maximum number of iterations if a composite score falls below threshold; the paper
  reports acceptance thresholds of 80% (coverage) and 70% (integrity) with up to 3 attempts,
  and that the loop is triggered in only ~7% of cases ⟨§3.2.3; §4.4; App A.2⟩.
- DuTR reasons in two modes over the semantic tree: Adaptive Tree Navigation picks Leaf-to-Root
  (for aggregation/conditional-counting queries) or Root-to-Leaf (for localized lookup queries)
  traversal, and Symbolic Tree Manipulation generates Python over a value-free tree skeleton
  with a self-correction loop that feeds runtime error traces back to the LLM ⟨§3.3⟩; an Answer
  Selector (a lightweight open-source LLM, Qwen3-8B) picks between the Textual and Symbolic
  candidate answers ⟨§3.4; App A.2⟩.
- Evaluation is on three complex-table benchmarks — AIT-QA, HiTab, and SSTQA (introduced by
  ST-Raptor) — with DeepSeek-V3 as the shared backbone for all training-free methods and GPT-5
  as an LLM-as-judge for accuracy; the paper reports 98.25% (393/400) judge–human agreement on
  a 200-query SSTQA subset ⟨§4.1; App A.2–A.3⟩.
- The paper reports ASTRA achieves SOTA accuracy via Adaptive Selection — AIT-QA 91.6%, SSTQA
  81.9%, HiTab 90.1% — stating this outperforms the reasoning model OpenAI o3 (85.3% on HiTab)
  and greatly exceeds the rule-based ST-Raptor baseline (AIT-QA 62.7%, HiTab 49.0%), which it
  reads as exposing ST-Raptor's fragility across diverse layouts ⟨§4.2; Table 2⟩.
- It reports a mode trade-off: on semantically intensive SSTQA, Textual Reasoning (79.8%)
  beats Symbolic (75.3%); on numerical HiTab, Symbolic (89.3%) beats Textual (82.2%) ⟨§4.2;
  Table 2⟩.
- An ablation reports that the Semantic Tree representation alone, under direct prompting,
  reaches 70.55% vs 63.20% for textual serialization (+7.35), which the paper reads as an
  intrinsic benefit of hierarchical serialization independent of the reasoning mechanism
  ⟨§4.3; Table 4⟩; removing the Evaluator-Guided loop drops average coverage 0.929 → 0.745
  ⟨§4.3; Table 3⟩.
- On efficiency, the paper reports lower QA latency than ST-Raptor and GraphOTTER via a
  write-once/read-many design, and that ASTRA surpasses GraphOTTER on amortized cost once query
  count per table N ≥ 3 (AIT-QA/HiTab) or N ≥ 10 (SSTQA) ⟨§4.4; Table 5⟩.
- Stated limitations: for extremely simple flat tables the reconstruction may add overhead vs
  direct serialization, and ASTRA relies on textual/structural parsing and does not yet use
  visual cues (background colors, bold fonts) that convey implicit semantic constraints
  ⟨Limitations⟩.

## Concepts & entities covered
Concepts: [[complex-table-understanding]] · [[table-serialization]]
Entities: [[astra]]
