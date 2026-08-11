---
title: "GraphRAG"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[retrieval-augmented-generation]]", "[[global-vs-local-search]]", "[[community-detection-summarization]]", "[[entity-relation-extraction]]", "[[llm-kg-construction]]"]
updated: 2026-08-10
---

# GraphRAG

## What it is
GraphRAG is retrieval-augmented generation that retrieves from graph-structured data — nodes, relations, triples, paths, or subgraphs — rather than from an i.i.d. text corpus. A graph index is built over (or selected for) a corpus, relevant graph elements are retrieved for a query, and the generator produces an answer conditioned on that relational knowledge. Different sources decompose the pipeline into different stages, but all share the move from flat similarity retrieval to retrieval over an explicit graph.

## How sources treat it
- **[[graphrag-local-to-global]]** _(article · informational)_ — GraphRAG uses an LLM to build a graph index in two stages: first deriving an entity knowledge graph from the source documents, then pre-generating community summaries for all groups of closely related entities ⟨arxiv 2404.16130, §Abstract⟩
- **[[graph-rag-survey]]** _(article · informational)_ — Formalizes GraphRAG as a three-stage workflow — Graph-Based Indexing (G-Indexing), Graph-Guided Retrieval (G-Retrieval), and Graph-Enhanced Generation (G-Generation) — and organizes its taxonomy of techniques and training methods around these stages ⟨§Abstract; §4⟩
- **[[graph-rag-survey]]** _(article · informational)_ — Treats GraphRAG as a branch of RAG that retrieves graph elements carrying relational knowledge — nodes, triples, paths, or subgraphs — from a pre-constructed graph database rather than a text corpus ⟨§1; §2.1⟩
- **[[rag-with-graphs-survey]]** _(article · informational)_ — Proposes a holistic GraphRAG framework of five components: query processor, retriever, organizer, generator, and graph data source, arranged as Q → processor → retriever → organizer → generator → answer ⟨arXiv 2501.00309, §2.1⟩
- **[[ms-graphrag-implementation]]** _(provider-doc · vendor)_ — Describes GraphRAG as a data pipeline and transformation suite that extracts meaningful, structured data from unstructured text using the power of LLMs, presented as a demonstration methodology rather than an officially supported offering ⟨README, Overview⟩

## Where sources differ
The sources agree that GraphRAG retrieves over an explicit graph but decompose the pipeline differently, and the decompositions are complementary framings rather than competing claims. [[graphrag-local-to-global]] presents a concrete two-stage build (entity graph, then community summaries) tied to global summarization; [[graph-rag-survey]] abstracts the pipeline into three stages (G-Indexing / G-Retrieval / G-Generation); [[rag-with-graphs-survey]] uses a five-component decomposition (query processor / retriever / organizer / generator / graph data source). [[ms-graphrag-implementation]] describes the Microsoft open-source system implementing the local-to-global method. The three surveys and the Microsoft work use the name "GraphRAG" at different levels of generality — one specific method versus a whole design space.

## See also
[[retrieval-augmented-generation]] · [[global-vs-local-search]] · [[community-detection-summarization]] · [[entity-relation-extraction]] · [[llm-kg-construction]]
