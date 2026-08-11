---
title: "The GraphRAG Manifesto: Adding Knowledge to GenAI (Neo4j)"
type: source
kind: blog
authority: practitioner
subtype: article
aliases: ["GraphRAG Manifesto"]
publisher: "Neo4j"
url: https://neo4j.com/blog/genai/graphrag-manifesto/
version: "2024"
published: 2024-07
effective_from: 2024-07
effective_to: ongoing
status: current
tags: [graph-rag]
updated: 2026-08-10
---

# The GraphRAG Manifesto: Adding Knowledge to GenAI (Neo4j)

> _Authored from general knowledge, not from the primary text (the browser fetch was unavailable this session). Verify against the primary Neo4j blog post before relying on specifics; can be upgraded to a full-text ingest once retrievable._

## Scope & purpose
A vendor practitioner article (attributed to Neo4j's Philip Rathle) arguing that adding a knowledge graph to retrieval-augmented generation ("GraphRAG") improves answer quality, explainability, and governability relative to vector-only RAG. Captured **lightweight** as practitioner framing that parallels the research sources in this wave.

## Key points
- Frames **GraphRAG** as RAG in which the retrieval step draws on a knowledge graph, not only vector similarity over text chunks ⟨Neo4j GraphRAG Manifesto, definition⟩ [gen]
- Argues GraphRAG tends to improve **accuracy and completeness** of answers by supplying explicit relationships and structure that vector-only retrieval misses ⟨Neo4j GraphRAG Manifesto, benefits⟩ [gen]
- Emphasizes **explainability and traceability**: graph-structured context lets answers be traced back to identifiable entities and relationships ⟨Neo4j GraphRAG Manifesto, explainability⟩ [gen]
- Positions the knowledge graph as a form of durable, curatable **knowledge / long-term memory** for GenAI applications, enabling governance and access control over what the model can use ⟨Neo4j GraphRAG Manifesto, governance⟩ [gen]
- Describes knowledge graphs as buildable both from structured sources and by **LLM-assisted extraction** from unstructured text ⟨Neo4j GraphRAG Manifesto, construction⟩ [gen]

## Concepts & entities covered
Concepts: [[graphrag]] · [[retrieval-augmented-generation]]
Entities: [[org-neo4j]]
