---
title: "ST-Raptor (system)"
type: entity
subtype: system
aliases: []
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]", "[[agentic-extraction]]", "[[extraction-self-verification]]"]
sources: ["[[st-raptor]]"]
published: 2026
effective_from: 2026-02
effective_to: ongoing
status: current
updated: 2026-08-11
---

# ST-Raptor

## What it is
ST-Raptor is an agentic system for question answering over semi-structured tables that
combines visual editing, tree-based structural modeling, and agent-driven query resolution,
centered on a layout-aware Hierarchical Orthogonal Tree (HO-Tree) representation of the
table ⟨st-raptor Abstract⟩.

## Key facts
- Its HO-Tree captures structural relationships among headers, content cells, and merged
  regions and unifies multiple interrelated sheets under one root for global reasoning, aiming
  to avoid the semantic loss the paper attributes to flattening nested tables, de-hierarchizing
  multi-level headers, and NULL-filling merged cells ⟨st-raptor Why complex tables are hard;
  Core approach⟩.
- HO-Trees are built by a hybrid strategy pairing rule-based matching with multimodal-LLM
  reasoning: render the table to a high-resolution image, prompt a VLM for candidate
  meta-information keys, align keys to cells by embedding similarity, partition around meta
  cells, and recursively construct the tree using layout principles ⟨st-raptor Core approach⟩.
- Nine core tree operations abstract common analytical tasks for modular reasoning, which the
  paper states offers "higher accuracy than a general execute-then-reflect mechanism"
  ⟨st-raptor Core approach⟩.
- It applies two-stage verification — FORWARD verification of sub-operation logic/execution
  traces and BACKWARD verification that rephrases the question to check answer consistency — to
  reduce hallucination ⟨st-raptor Core approach⟩.
- A human-in-the-loop Tree Editor lets users correct misaligned headers and adjust hierarchical
  groupings by drag-and-drop, where small edits do not trigger re-parsing of the whole table
  ⟨st-raptor Core approach⟩.
- The source reports ST-Raptor achieves the highest accuracy in its evaluation, surpassing the
  best-performing baseline by 11.2% on SSTQA (102 real-world tables) and WikiTQ ⟨st-raptor
  Evaluation⟩.

## Relations
- Realizes: [[complex-table-understanding]] · [[table-serialization]] · [[agentic-extraction]] · [[extraction-self-verification]]
- Defined in: [[st-raptor]]

## See also
[[st-raptor]]
