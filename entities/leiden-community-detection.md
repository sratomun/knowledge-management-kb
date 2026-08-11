---
title: "Leiden community detection"
type: entity
subtype: technique
aliases: ["Leiden algorithm"]
tags: [graph-rag]
status: current
concepts: ["[[community-detection-summarization]]"]
sources: ["[[graphrag-local-to-global]]"]
updated: 2026-08-10
---

# Leiden community detection

## What it is
Leiden community detection (Traag et al., 2019) is the graph community-detection algorithm GraphRAG uses to partition its entity knowledge graph into nested communities of closely related nodes. GraphRAG applies it hierarchically to produce the community structure over which community summaries are generated.

## Key facts
- GraphRAG uses Leiden community detection (Traag et al., 2019) in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned ⟨arxiv 2404.16130, §3.1.4⟩
- It is presented as one of a variety of community detection algorithms that may be used to partition the graph into communities of strongly connected nodes ⟨arxiv 2404.16130, §3.1.4⟩
- Each level of the resulting hierarchy provides a community partition that covers the graph's nodes in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization ⟨arxiv 2404.16130, §3.1.4⟩
- It is cited alongside Louvain (Blondel et al., 2008) as a means of partitioning graphs into nested modular communities, exploiting graph modularity (Newman, 2006) ⟨arxiv 2404.16130, §2.2⟩
- In the paper's implementation, Leiden community detection was implemented using the graspologic library (Chung et al., 2019) ⟨arxiv 2404.16130, §4.1.3⟩

## Relations
- Realizes / relates to: [[community-detection-summarization]]
- Defined in: [[graphrag-local-to-global]]
- Related: [[microsoft-graphrag]]

## See also
[[microsoft-graphrag]]
