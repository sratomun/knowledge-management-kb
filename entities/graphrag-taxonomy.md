---
title: "GraphRAG survey taxonomy"
type: entity
subtype: framework
aliases: ["Han et al. GraphRAG framework"]
tags: [graph-rag]
concepts: ["[[graphrag]]", "[[retrieval-augmented-generation]]", "[[entity-relation-extraction]]"]
sources: ["[[rag-with-graphs-survey]]"]
updated: 2026-08-10
---

# GraphRAG survey taxonomy

## What it is

The holistic GraphRAG framework proposed by Han et al. (arXiv:2501.00309), which
decomposes a GraphRAG system into five components — query processor, retriever, organizer,
generator, and graph data source — and cross-cuts it with a ten-domain categorization of
graph types. It serves as the survey's organizing scheme for reviewing GraphRAG
techniques both globally (per component) and locally (per domain).

## Key facts

- The framework defines five components pipelined as query processor → retriever →
  organizer → generator over a graph data source ⟨arXiv 2501.00309, §2.1⟩.
- The query processor covers named entity recognition, relational extraction, query
  structuration, query decomposition, and query expansion ⟨arXiv 2501.00309, §2.3⟩.
- Retrievers are categorized as heuristic-based, learning-based, and advanced-strategy
  (integrated, iterative, adaptive) ⟨arXiv 2501.00309, §2.4⟩.
- The organizer's techniques are graph pruning, reranking, graph augmentation, and
  verbalizing ⟨arXiv 2501.00309, §2.5⟩.
- Generators are typed as discrimination-based, LLM-based, and graph-based ⟨arXiv 2501.00309, §2.6⟩.
- Graph data sources are distinguished by explicit vs. implicit construction and by
  representation (adjacency matrix, edge list, adjacency list, node sequence, natural
  language) ⟨arXiv 2501.00309, §2.7⟩.
- The domain axis spans ten graph types: knowledge, document, scientific, social,
  planning & reasoning, tabular, infrastructure, biological, scene, and random graphs ⟨arXiv 2501.00309, §1⟩.

## Relations

- Realizes: [[graphrag]] · [[retrieval-augmented-generation]] · [[entity-relation-extraction]]
- Defined in: [[rag-with-graphs-survey]]
- Related: [[microsoft-graphrag]]

## See also

[[graphrag]] · [[retrieval-augmented-generation]]
