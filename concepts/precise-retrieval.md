---
title: "Precise retrieval"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[retrieval-augmented-generation]]", "[[retrieval-evaluation]]"]
updated: 2026-08-10
---

# Precise retrieval

## What it is
Precise retrieval is the practice of returning minimal, highly relevant text segments in response to a query, rather than document identifiers or large blocks of loosely relevant context. The motivation is that downstream generators work better on tight, citable evidence: precision keeps content within context-window limits, reduces cost and latency, enables source citations, and makes human verification tractable. It is measured with precision/recall-style retrieval metrics and is often the first stage of a larger extraction or answering pipeline.

## How sources treat it
- **[[legalbench-rag]]** _(article · informational)_ — emphasizes extracting minimal, highly relevant text segments, arguing such snippets are preferable to returning document IDs or large sequences of imprecise chunks that can exceed context-window limits ⟨Abstract; §1⟩
- **[[legalbench-rag]]** _(article · informational)_ — motivates precision by noting long context windows cost more, add latency, and lead LLMs to forget or hallucinate, whereas precise results let the LLM generate citations and a human quickly verify claims ⟨Abstract; §1⟩
- **[[kyc-multistage-extraction]]** _(article · informational)_ — realizes precise retrieval as a page-localization stage that combines BM25 lexical matching with sentence-embedding semantic similarity per target field, reducing the pages forwarded to the expensive VLM by about 70% ⟨arXiv:2604.26462, §3⟩
- **[[kyc-multistage-extraction]]** _(article · informational)_ — reports page-level retrieval as the most critical component in its ablation, with removal dropping accuracy 16.8–24.0 percentage points ⟨arXiv:2604.26462, §4⟩

## Where sources differ
The two sources apply precise retrieval at different granularities and for different ends. [[legalbench-rag]] retrieves at the *snippet/character-span* level and evaluates precision as an end in itself (a benchmark of the retrieval step), reporting low absolute precision due to the concise nature of ground-truth spans. [[kyc-multistage-extraction]] retrieves at the *page* level as a cost-control filter — narrowing which pages a vision-language model must read — where precision is instrumental to a downstream extraction pipeline rather than the object of evaluation. Their comparative configuration findings are each source's own.

## See also
[[retrieval-augmented-generation]] · [[retrieval-evaluation]]
