---
title: "Retrieval-Augmented Generation"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[graphrag]]", "[[global-vs-local-search]]", "[[entity-relation-extraction]]"]
updated: 2026-08-10
---

# Retrieval-Augmented Generation

## What it is
Retrieval-augmented generation (RAG) is a pattern in which a language model's generation is conditioned on external content fetched at query time, rather than on the model's parameters alone. The external content is retrieved from a knowledge base — classically a corpus of text chunks selected by similarity — to supply domain knowledge, reduce hallucination, and keep answers current. The graph-RAG literature treats conventional similarity-based RAG as the baseline it extends.

## How sources treat it
- **[[graph-rag-survey]]** _(article · informational)_ — Conventional RAG mitigates LLM hallucination, missing domain knowledge, and outdated information by referencing an external knowledge base, but the survey identifies three limitations it targets: neglecting relationships between interconnected texts, redundant information causing the "lost in the middle" problem, and lacking global information needed for tasks such as Query-Focused Summarization ⟨§1⟩
- **[[rag-with-graphs-survey]]** _(article · informational)_ — Frames GraphRAG as retrieval-augmented generation that augments generation by retrieving heterogeneous, relational knowledge from graph-structured sources, offering advantages over similarity-only RAG through graph-based ML and graph analysis ⟨arXiv 2501.00309, Abstract / §1⟩
- **[[rag-with-graphs-survey]]** _(article · informational)_ — Contrasts RAG's uniform "Text-in, Text-out" retrieval with graph retrieval that must additionally capture graph-structure signals BM25/TF-IDF and dense text retrievers overlook ⟨arXiv 2501.00309, §2.4⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — Describes conventional "vector RAG" as retrieving records individually relevant to the query that collectively fit the context window; it works well for queries answerable from information localized within a small set of records but does not support sensemaking queries requiring global understanding of the entire dataset ⟨arxiv 2404.16130, §2.1⟩
- **[[ms-graphrag-implementation]]** _(provider-doc · vendor)_ — States that connecting information across large volumes of data to answer questions spanning many documents, as well as thematic questions such as "what are the top themes in this dataset?", is difficult or impossible for keyword and vector-based search ⟨RAI FAQ, What can GraphRAG do⟩

## Where sources differ
The sources are complementary rather than conflicting: all four take conventional similarity/vector RAG as an established baseline and describe its scope in order to motivate graph-based extensions. [[graph-rag-survey]] enumerates three specific shortcomings, [[graphrag-local-to-global]] and [[ms-graphrag-implementation]] emphasize the local-versus-global limitation in particular, and [[rag-with-graphs-survey]] frames the gap in retrieval terms (structure signals text retrievers miss). None ranks RAG against graph RAG in the abstract; each positions the baseline to describe what graph structure adds.

## See also
[[graphrag]] · [[global-vs-local-search]] · [[entity-relation-extraction]]
