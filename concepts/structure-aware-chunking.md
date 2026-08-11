---
title: "Structure-aware chunking"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[semantic-chunking]]", "[[document-element-classification]]"]
updated: 2026-08-10
---

# Structure-aware chunking

## What it is
Structure-aware chunking splits a document into retrieval units according to its **physical structural elements** — titles, sections, tables, lists — rather than by fixed character or token counts. The premise is that a document's layout carries information that flat, structure-agnostic splitting discards: a table should stay whole, a new section should begin a new chunk. It depends on a prior document-understanding step that classifies each element by type, and it is typically evaluated by its effect on retrieval accuracy and downstream question answering.

This is the structure-driven end of the broader family of [[semantic-chunking]]: where semantic chunking may locate boundaries by *meaning* (topical/linguistic coherence, sometimes independent of layout), structure-aware chunking locates them at the document's *element boundaries*. The two overlap — element boundaries often coincide with semantic ones — and sources use the labels with varying breadth.

## How sources treat it
- **[[financial-report-chunking]]** _(article · informational)_ — proposes chunking primarily by structural element components (element types), contrasting this with fixed-size, recursive, contextual, and hybrid strategies that overlook document structure ⟨arXiv:2402.05131, Abstract / §2⟩
- **[[financial-report-chunking]]** _(article · informational)_ — forms chunks by merging elements up to a target length without breaking an element, starting a new chunk at each TITLE element and at each TABLE element while preserving the entire table ⟨arXiv:2402.05131, §3⟩
- **[[financial-report-chunking]]** _(article · informational)_ — reports that dissecting documents into constituent elements yields a good chunk size without tuning a token-count hyper-parameter, which the authors say makes the method more generalizable to new document types, whereas the best basic chunk size varies from dataset to dataset ⟨arXiv:2402.05131, Abstract / §4 / §5-6⟩
- **[[financial-report-chunking]]** _(article · informational)_ — reports an efficiency advantage: the highest retrieval scores with only about half the chunks of structure-agnostic aggregation (62,529 vs. 112,155), reducing indexing cost and query latency ⟨arXiv:2402.05131, §4⟩

## Where sources differ
Only one source (a single technique paper) treats this practice directly, so the KB records no cross-source divergence. Its comparative claims — element-based versus fixed-size, recursive, contextual, and hybrid chunking, and the reported retrieval and Q&A gains — are attributed to the authors and reported as their FinanceBench findings, not as KB conclusions. The practice's generality beyond SEC financial reports is the paper's own conjecture.

## See also
[[semantic-chunking]] · [[document-element-classification]]
