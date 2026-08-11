---
title: "ST-Raptor: An Agentic System for Semi-Structured Table QA"
type: source
kind: article
authority: informational
subtype: system
aliases: ["ST-Raptor"]
publisher: arXiv
url: https://arxiv.org/abs/2602.07034
version: "arXiv:2602.07034v1 [cs.AI]"
published: 2026
effective_from: 2026-02
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]", "[[agentic-extraction]]", "[[extraction-self-verification]]"]
entities: ["[[st-raptor-system]]"]
updated: 2026-08-11
---

# ST-Raptor: An Agentic System for Semi-Structured Table QA

## Scope & purpose

ST-Raptor is a demo-paper agentic system (Shanghai Jiao Tong University, Tsinghua, HKBU)
for question answering over semi-structured tables — tables that require both precise
extraction of cell contents/positions and recovery of the implicit logical structures,
hierarchical relationships, and semantic associations encoded in their layout ⟨Abstract⟩.
It combines visual editing, tree-based structural modeling, and agent-driven query
resolution, and is positioned against Text-to-SQL, Text-to-Code, and multimodal-LLM QA
approaches that the authors say lose information or mishandle complex layouts ⟨Abstract⟩.
The KB records the paper's comparative claims descriptively.

## Key points

- The paper frames why complex tables are hard as three concrete failure modes of existing
  solutions: (1) flattening nested/hierarchical tables causes severe semantic loss and
  header–content misalignment; (2) decomposing multi-level headers into flat token sequences
  ignores hierarchical relationships critical for grouped/aggregated indicators; (3) treating
  irregular merged cells as sparse matrices filled with artificial NULLs breaks the
  continuity and semantics of logically connected regions (e.g. merged "Total" rows)
  ⟨Why complex tables are hard⟩.
- Its core representation is the Hierarchical Orthogonal Tree (HO-Tree), a layout-aware
  structure capturing relationships among headers, content cells, and merged regions;
  multiple interrelated sheets are unified under one root for global reasoning
  ⟨Core approach⟩.
- HO-Trees are built by a hybrid strategy integrating rule-based matching with multimodal-LLM
  reasoning: render tables to high-resolution images → prompt a VLM to identify candidate
  meta-information keys → align keys to cells via embedding-based similarity → partition the
  table around meta cells → recursively construct HO-Trees using layout principles such as
  top-level header identification ⟨Core approach⟩.
- Table2Tree ingests multimodally from .xlsx/.csv/.html/.md and screenshots ⟨Core approach⟩.
- A human-in-the-loop Tree Editor (web UI) lets users visualize, edit, and correct misaligned
  headers and adjust hierarchical groupings by drag-and-drop and build HO-Trees from scratch;
  small edits (e.g. removing one row) do not trigger costly re-parsing of the whole table
  ⟨Core approach⟩.
- Nine core tree operations abstract common analytical tasks to enable modular reasoning,
  which the paper states offers "higher accuracy than a general execute-then-reflect
  mechanism" ⟨Core approach⟩.
- The Answer Generator decomposes questions into sub-operations aligned with the HO-Tree,
  performs top-down and bottom-up subtree retrieval over deeply nested layouts, and applies
  column-type-aware tagging to distinguish numerical/categorical/free-text fields
  ⟨Core approach⟩.
- Two-stage verification reduces hallucination: FORWARD verification checks the logic and
  execution trace of sub-operations, and BACKWARD verification rephrases the question and
  ensures answer consistency ⟨Core approach⟩.
- An Orchestration Agent tracks query history, resolves ambiguous references (e.g. "this
  product" → "Product A"), routes queries to retrieval/aggregation modules, maintains a
  dynamic memory loop across files/tables/turns, and invokes VLMs for extraction on images
  ⟨Core approach⟩.
- Evaluation uses Gemini-3.0-preview (VLM), Gemini-2.0 (LLM), and text-embedding-v1, against
  baselines including OpenSearch-SQL, TableLLaMA, TableLLM, ReAcTable, TAT-LLM, TableLLaVA,
  mPLUG-DocOwl1.5, GPT-4o, and DeepSeekV3, on SSTQA (102 tables filtered from 2,031 real-world
  tables across 19 scenarios) and WikiTQ (25% converted to images) ⟨Evaluation⟩.
- The paper reports ST-Raptor achieves the highest accuracy, surpassing the best-performing
  baseline by 11.2%, and attributes the gain to HO-Tree decoupling layout parsing from logical
  reasoning, question decomposition aligned with tree operations, and the agent coordinating
  vision-based extraction with multi-turn context; it states agent-based baselines (ReAcTable,
  DocOwl) struggle with structural comprehension because they flatten multi-level headers and
  treat each header independently ⟨Evaluation⟩.

## Concepts & entities covered
Concepts: [[complex-table-understanding]] · [[table-serialization]] · [[agentic-extraction]] · [[extraction-self-verification]]
Entities: [[st-raptor-system]]
