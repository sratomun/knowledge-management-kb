---
title: "Community Detection and Summarization"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[graphrag]]", "[[global-vs-local-search]]", "[[entity-relation-extraction]]"]
updated: 2026-08-10
---

# Community Detection and Summarization

## What it is
Community detection and summarization is the graph-RAG indexing step that partitions an entity graph into groups of closely related entities (communities) and pre-generates a natural-language summary for each community. Because the communities form a mutually exclusive, collectively exhaustive cover of the graph — often hierarchically — their summaries can be combined divide-and-conquer to answer questions about the whole corpus without retrieving individual records.

## How sources treat it
- **[[graphrag-local-to-global]]** _(article · informational)_ — Uses Leiden community detection (Traag et al., 2019) in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned ⟨arxiv 2404.16130, §3.1.4⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — Each level of the hierarchy provides a community partition covering the graph's nodes in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization ⟨arxiv 2404.16130, §3.1.4⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — Community summaries are generated bottom-up: leaf-level community element summaries are prioritized by combined source-and-target node degree and added until the token limit, and higher-level summaries substitute shorter sub-community summaries for longer element summaries when they do not fit ⟨arxiv 2404.16130, §3.1.5⟩
- **[[graphrag-local-to-global]]** _(article · informational)_ — Root-level community summaries (C0) required 9x–43x fewer tokens per query than source-text summarization, offering a highly efficient method for iterative global question answering while retaining comprehensiveness and diversity advantages over vector RAG ⟨arxiv 2404.16130, §5.1⟩
- **[[ms-graphrag-implementation]]** _(provider-doc · vendor)_ — States GraphRAG can answer thematic questions such as "what are the top themes in this dataset?" that are difficult or impossible for keyword and vector-based search — the class of question community summaries are built to serve ⟨RAI FAQ, What can GraphRAG do⟩

## Where sources differ
The two sources describe the same mechanism at different levels of detail rather than disagreeing. [[graphrag-local-to-global]] specifies the algorithmic construction (Leiden hierarchical partitioning, degree-prioritized bottom-up summarization, token-efficient root summaries). [[ms-graphrag-implementation]], the vendor documentation for the corresponding open-source system, describes the user-facing capability the summaries enable — answering thematic, whole-dataset questions — without restating the community-detection internals.

## See also
[[graphrag]] · [[global-vs-local-search]] · [[entity-relation-extraction]]
