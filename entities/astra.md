---
title: "ASTRA"
type: entity
subtype: technique
aliases: []
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]"]
sources: ["[[astra-table-qa]]"]
published: 2026
effective_from: 2026-05
effective_to: ongoing
status: current
updated: 2026-08-11
---

# ASTRA

## What it is
ASTRA (Adaptive Semantic Tree Reasoning Architecture) is a training-free method for complex
table question answering that treats table serialization as the critical bottleneck, pairing
an adaptive semantic-tree reconstruction module (AdaSTR) with a dual-mode reasoning engine
(DuTR) ⟨astra-table-qa Abstract; §3.1⟩.

## Key facts
- AdaSTR reconstructs a table into a Logical Semantic Tree via header identification and
  normalization (e.g. merging "Yukon" with "Percent" → "Yukon-Percent"), hierarchy
  identification, and one of three scale-adaptive synthesis modes (Direct Semantic Parsing,
  Symbolic Reference Encoding, Programmatic Structure Synthesis), degenerating to a shallow
  tree for flat tables ⟨astra-table-qa §3.2.1; §3.2.2⟩.
- An Evaluator-Guided Refinement Loop validates the tree on Structural Integrity and
  Information Coverage (reported thresholds 70% and 80%, up to 3 attempts) and is reported to
  trigger in only ~7% of cases ⟨astra-table-qa §3.2.3; §4.4; App A.2⟩.
- DuTR reasons over the tree in two modes — query-adaptive Leaf-to-Root or Root-to-Leaf textual
  navigation, and symbolic Python manipulation over a value-free skeleton with an error-trace
  self-correction loop — and an Answer Selector chooses between the textual and symbolic
  candidates ⟨astra-table-qa §3.3; §3.4⟩.
- The source reports ASTRA reaches SOTA accuracy via Adaptive Selection — 91.6% (AIT-QA), 81.9%
  (SSTQA), 90.1% (HiTab) — stating this exceeds OpenAI o3 (85.3% HiTab) and the rule-based
  ST-Raptor baseline (62.7% AIT-QA, 49.0% HiTab) ⟨astra-table-qa §4.2; Table 2⟩.
- The source reports the Semantic Tree representation alone (70.55% under direct prompting)
  outperforms textual serialization (63.20%, +7.35), presented as an intrinsic benefit of
  hierarchical serialization ⟨astra-table-qa §4.3; Table 4⟩.
- The source frames prior tree-based ST-Raptor as "fragile" because of its rule-based/physical
  construction, and states ASTRA does not yet exploit visual cues such as background colors or
  bold fonts ⟨astra-table-qa §1; App D; Limitations⟩.

## Relations
- Realizes: [[complex-table-understanding]] · [[table-serialization]]
- Defined in: [[astra-table-qa]]
- Related: [[st-raptor-system]]

## See also
[[astra-table-qa]] · [[st-raptor-system]]
