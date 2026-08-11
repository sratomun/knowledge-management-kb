---
title: "Global vs. Local Search"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[graphrag]]", "[[community-detection-summarization]]", "[[retrieval-augmented-generation]]"]
updated: 2026-08-10
---

# Global vs. Local Search

## What it is
Global vs. local search is a distinction between two kinds of question a retrieval system must serve. Local questions are answerable from information localized within a small set of records and suit conventional similarity retrieval. Global (sensemaking) questions ask about an entire corpus — its themes, aggregate structure, or high-level patterns — and cannot be answered by retrieving a few individually relevant records. Graph-RAG methods treat the global case as a query-focused summarization problem addressed by summarizing the whole graph rather than fetching local matches.

## How sources treat it
- **[[graphrag-local-to-global]]** _(article · informational)_ — Vector RAG works well for queries answerable from information localized within a small set of records but does not support sensemaking queries requiring global understanding of the entire dataset ⟨arxiv 2404.16130, §2.1⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — For a global answer, community summaries are randomly shuffled and chunked, intermediate "map" answers are generated in parallel with a helpfulness score, then a "reduce" step adds answers in descending helpfulness order until the token limit, producing the final global answer ⟨arxiv 2404.16130, §3.1.6⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — Across two ~1M-token datasets, global approaches significantly outperformed conventional vector RAG on comprehensiveness (win rates 72–83%, p<.001) and diversity, while vector RAG produced the most direct responses ⟨arxiv 2404.16130, §5.1⟩
- **[[graph-rag-survey]]** _(article · informational)_ — Lists lacking global information — needed for tasks such as Query-Focused Summarization (QFS) — as one of three limitations of traditional RAG that GraphRAG targets, alongside neglecting relationships and redundant "lost in the middle" information ⟨§1⟩
- **[[graph-rag-survey]]** _(article · informational)_ — Distinguishes retrieval granularities (nodes, triplets, paths, subgraphs, hybrid), noting granularity choice trades retrieval content against efficiency — the machinery by which local versus broader retrieval scope is set ⟨§6.3⟩

## Where sources differ
The two sources are complementary. [[graphrag-local-to-global]] operationalizes the global case concretely, via map-reduce over community summaries, and reports head-to-head evaluation in which global methods win on comprehensiveness and diversity while vector RAG wins on directness. [[graph-rag-survey]] treats "lacking global information" more abstractly as one of three motivating limitations of traditional RAG and connects retrieval scope to a granularity spectrum. Neither recommends one mode over the other; both describe global and local as suited to different question types.

## See also
[[graphrag]] · [[community-detection-summarization]] · [[retrieval-augmented-generation]]
