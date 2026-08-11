---
title: "Deep Tabular Research agent"
type: entity
subtype: system
aliases: []
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]", "[[agentic-extraction]]"]
sources: ["[[deep-tabular-research]]"]
published: 2026
effective_from: 2026-03
effective_to: ongoing
status: current
updated: 2026-08-11
---

# Deep Tabular Research agent

## What it is
The Deep Tabular Research (DTR) agent is an agentic framework for long-horizon, multi-hop
analytical reasoning over unstructured tables with hierarchical/bidirectional headers and
non-canonical layouts, treating tabular reasoning as a closed-loop decision process that
decouples strategic planning from low-level programmatic execution ⟨deep-tabular-research
Abstract; §1⟩.

## Key facts
- It builds a hierarchical meta graph from bi-directional headers and implicit metadata (units,
  temporal/categorical markers, aggregation indicators), where a sub-item can belong to both
  row and column parents, giving each cell row-wise and column-wise descriptors ⟨deep-tabular-
  research §3.1⟩.
- It maps queries onto a seed operation bank ({CLEAN, FILTER, GROUP, AGG, JOIN, SORT, ...}) and
  plans over candidate operation paths using an expectation-aware (p-UCB-style) score that
  balances exploitation of high-return paths against exploration of structurally plausible ones
  ⟨deep-tabular-research §3.2; §3.3; Eq. 1⟩.
- A siamese structured memory records parameterized execution signals (validity, time,
  output-type consistency) for immediate refinement and abstracted textual experience (e.g.
  "insert CHECK/CLEAN before AGG") for cross-instance transfer, with a final answer chosen by
  majority agreement across executed paths ⟨deep-tabular-research §3.4; §3.5; Eq. 4, Eq. 6⟩.
- The source reports DTR (DeepSeek-V3) achieves the strongest overall performance on its own
  DTR-Bench (500 analytical QA pairs) across accuracy, analysis depth, feasibility, and
  aesthetics, and leads all task types on RealHitBench (e.g. 100.0 ECR on visualization)
  ⟨deep-tabular-research §4.1; Table 1; Table 2⟩.
- The source reports an architecture ablation gain of 4.0 accuracy points over a pure
  DeepSeek-V3 baseline (33.5% → 37.5%), with structural meta-information and query decomposition
  the largest contributors ⟨deep-tabular-research §4.2; Table 3⟩.
- The source reports the structured [THINK]+[CODE] prompting scheme cuts code error rate from
  42.3% to 28.4% at 4.78 average LLM calls, and that DTR's operating point outperforms the
  CodeLoop baseline (27.5% accuracy at 8.8 calls) ⟨deep-tabular-research §4.2; §4.3; Table 4;
  Figure 3⟩.

## Relations
- Realizes: [[complex-table-understanding]] · [[table-serialization]] · [[agentic-extraction]]
- Defined in: [[deep-tabular-research]]
- Related: [[st-raptor-system]]

## See also
[[deep-tabular-research]] · [[st-raptor-system]]
