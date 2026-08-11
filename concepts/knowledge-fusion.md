---
title: "Knowledge Fusion"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[llm-kg-construction]]", "[[entity-relation-extraction]]", "[[ontology-learning]]"]
updated: 2026-08-10
---

# Knowledge Fusion

## What it is
Knowledge fusion is the integration of heterogeneous knowledge sources into one coherent graph by resolving duplication, conflict, and heterogeneity. Its central subtask is entity alignment — deciding whether entities from different datasets refer to the same real-world object — alongside disambiguation, deduplication, and conflict resolution. Fusion can operate at the schema level (unifying the structural backbone) or the instance level (reconciling individual entities).

## How sources treat it
- **[[llm-kg-construction-survey]]** _(article · informational)_ — Knowledge fusion integrates heterogeneous sources by resolving duplication, conflict, and heterogeneity; its central subtask, entity alignment, decides whether entities from different datasets refer to the same real-world object ⟨§2.3⟩
- **[[llm-kg-construction-survey]]** _(article · informational)_ — LLM-powered knowledge fusion divides into schema-level fusion (unifying the structural backbone), instance-level fusion (entity alignment, disambiguation, deduplication, conflict resolution), and hybrid frameworks that unify both in one workflow ⟨§5⟩
- **[[llm-kg-construction-survey]]** _(article · informational)_ — Schema-level fusion has moved from ontology-driven consistency to data-driven unification to LLM-enabled canonicalization, where LLMs generate natural-language definitions of schema components and compare them by vector similarity ⟨§5.1⟩
- **[[rag-with-graphs-survey]]** _(article · informational)_ — Names graph-construction challenges of granularity and disambiguation, and the difficulty of differentiating neural vs. symbolic knowledge and harmonizing internal vs. external knowledge during retrieval ⟨arXiv 2501.00309, §10.1–§10.4⟩

## Where sources differ
The two sources approach fusion from different stages of the graph lifecycle and are complementary. [[llm-kg-construction-survey]] treats fusion as a distinct construction-time layer, taxonomizing it into schema-level, instance-level, and hybrid, with entity alignment at its center. [[rag-with-graphs-survey]] raises the related concerns — disambiguation during construction, and harmonizing internal (parametric) with external (graph) knowledge during retrieval — as open challenges of a GraphRAG system rather than as a named fusion layer. Neither prescribes a method.

## See also
[[llm-kg-construction]] · [[entity-relation-extraction]] · [[ontology-learning]]
