---
title: "Microsoft GraphRAG (method)"
type: entity
subtype: system
aliases: []
tags: [graph-rag]
published: 2024-04
effective_from: 2024-04
effective_to: ongoing
status: current
concepts: ["[[graphrag]]", "[[retrieval-augmented-generation]]", "[[global-vs-local-search]]", "[[community-detection-summarization]]", "[[entity-relation-extraction]]", "[[llm-kg-construction]]"]
sources: ["[[graphrag-local-to-global]]"]
updated: 2026-08-10
---

# Microsoft GraphRAG (method)

## What it is
GraphRAG is a graph-based retrieval-augmented-generation method from Microsoft Research for question answering over private text corpora, designed to scale with both the generality of user questions and the quantity of source text. It uses an LLM to build a two-stage graph index — an entity knowledge graph plus pre-generated community summaries — and answers global queries by map-reduce summarization over those community summaries.

## Key facts
- Uses an LLM to build a graph index in two stages: first deriving an entity knowledge graph from the source documents, then pre-generating community summaries for all groups of closely related entities ⟨arxiv 2404.16130, §Abstract⟩
- Constructs a knowledge graph where nodes correspond to key entities and edges represent relationships between those entities, extracted by LLM prompts that can be domain-tailored via few-shot exemplars ⟨arxiv 2404.16130, §1 / §3.1.2⟩
- Partitions the graph into a hierarchy of communities of closely related entities and generates community-level summaries bottom-up, with higher-level summaries recursively incorporating lower-level ones ⟨arxiv 2404.16130, §1⟩
- Answers queries through map-reduce processing: in the map step community summaries independently produce partial answers in parallel, then in the reduce step the partial answers are combined into a final global answer ⟨arxiv 2404.16130, §1⟩
- Contrasts with conventional "vector RAG," which retrieves individually relevant records but cannot support sensemaking over an entire corpus ⟨arxiv 2404.16130, §2.1⟩
- Uses exact string matching for entity matching in the paper's analysis, but is described as generally resilient to duplicate entities since duplicates are typically clustered together for summarization ⟨arxiv 2404.16130, §3.1.3⟩
- Across two ~1M-token datasets, global GraphRAG approaches significantly outperformed vector RAG on comprehensiveness (win rates 72–83%, p<.001) and diversity ⟨arxiv 2404.16130, §5.1⟩
- Root-level community summaries (C0) require 9x–43x fewer tokens per query than source-text summarization while retaining comprehensiveness (72% win rate) and diversity (62% win rate) advantages over vector RAG ⟨arxiv 2404.16130, §5.1⟩
- Released as open-source software at github.com/microsoft/graphrag, with versions also available as extensions to LangChain, LlamaIndex, NebulaGraph, and Neo4J ⟨arxiv 2404.16130, §1⟩

## Relations
- Realizes: [[graphrag]] · [[retrieval-augmented-generation]] · [[global-vs-local-search]] · [[community-detection-summarization]] · [[entity-relation-extraction]] · [[llm-kg-construction]]
- Defined in: [[graphrag-local-to-global]]
- Related: [[leiden-community-detection]] · [[org-microsoft]]

## See also
[[leiden-community-detection]] · [[graphrag]]
