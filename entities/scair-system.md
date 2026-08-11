---
title: "SCAIR system"
type: entity
subtype: technique
aliases: []
tags: [doc-processing]
concepts: ["[[agentic-extraction]]", "[[schema-guided-extraction]]"]
sources: ["[[scair]]"]
updated: 2026-08-11
---

# SCAIR system

## What it is
SCAIR (Schema-Conditioned Agentic Iterative Reasoning) is a training-free KG-RAG framework for question answering over dense, schema-driven enterprise knowledge graphs. It unifies structured planning with controlled iterative reasoning by injecting schema-conditioned structural priors, enforcing schema-aware traversal during multi-hop reasoning, and controlling topic-entity propagation to balance exploration and exploitation.

## Key facts
- SCAIR is training-free and combines a lightweight schema-conditioned planning stage (schema-consistent relation paths plus depth-aligned subquestions) with a schema-aware iterative reasoning loop that filters candidate relations by schema constraints before scoring ⟨[[scair]] §4⟩.
- It is evaluated on an enterprise benchmark derived from a real manufacturing CMDB — CMDB-KG with 116,369 triples and 19,080 template-generated questions across 9 query types ⟨[[scair]] §3.2⟩.
- The authors report SCAIR outperforms all baselines (Accuracy 35.14, Hits@Any 47.56, F1 31.72) against the strongest baseline G-Retriever (25.27 Accuracy, 24.28 F1) ⟨[[scair]] Table 1⟩.
- SCAIR uses more LLM calls (42.36) and deeper average traversal (depth 2.54) than ToG (13.95) and PoG (5.60), a cost the authors describe as functional and amenable to prompt caching ⟨[[scair]] Table 2⟩.
- The authors argue the primary bottleneck is traversal control rather than backbone strength — "the failure mode is architectural, not parametric" — since a stronger backbone does not prevent search explosion ⟨[[scair]] §6.1⟩.
- The study's central lesson is that generic agentic designs optimized on public benchmarks often fail to generalize to real enterprise KGs, and effective enterprise graph reasoning must encode the domain's structural and operational constraints ⟨[[scair]] §1 / §7⟩.

## Relations
- Realizes: [[agentic-extraction]] · [[schema-guided-extraction]]
- Defined in: [[scair]]

## See also
[[agentic-extraction]] · [[schema-guided-extraction]] · [[scair]]
