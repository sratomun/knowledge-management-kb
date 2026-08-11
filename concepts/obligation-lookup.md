---
title: "Obligation lookup"
type: concept
subtype: use-case-profile
aliases: []
tags: [knowledge-processing]
related: ["[[obligation-extraction]]", "[[precise-retrieval]]", "[[legislative-document-model]]"]
updated: 2026-08-10
---

# Obligation lookup

## What it is
Obligation lookup is the use case of retrieving the specific legal, regulatory, or contractual obligation(s) that bear on a query — answering "what must this entity do, and where exactly is that stated?" It differs from open-ended question answering in that the target is a precise, citable span carrying a binding requirement, not a paraphrase. Which processing pattern fits depends on the nature of the source documents: legislative and contract text is high-normativity (MUST/SHALL modality that must be preserved), hierarchically structured, provenance-sensitive (answers must trace to an exact provision), moderately volatile, and lifecycle-bound to enactment and amendment. Those document-nature attributes — structure, normativity, volatility, sensitivity, provenance, lifecycle — condition how the pattern is realized.

## How sources treat it
- **[[legalbench-rag]]** _(article · informational)_ — targets the retrieval step of legal RAG, emphasizing precise retrieval of minimal, highly relevant snippets so downstream LLMs can generate citations and stay within context-window limits ⟨Abstract; §1⟩
- **[[legalbench-rag]]** _(article · informational)_ — pairs each query with an array of (filename, character-index-range) tuples over a human-annotated corpus, so a looked-up obligation resolves to exact source spans, including non-adjacent ones ⟨§3⟩
- **[[euro-5k-obligation-extraction]]** _(article · informational)_ — casts obligation identification as a sentence-level task: given legislative text, identify the sentences that mandate information submission from an entity to a regulatory authority for supervisory purposes ⟨§3.1, Eq. 1⟩
- **[[euro-5k-obligation-extraction]]** _(article · informational)_ — its Definition 1 scopes a reporting obligation as a mandatory requirement to submit specific information to an oversight authority, explicitly excluding behavioural, disclosure, and non-supervisory obligations ⟨§3.1, Definition 1⟩

## Where sources differ
The two sources address different halves of "lookup." [[legalbench-rag]] treats it as a retrieval problem — locating and returning the exact snippet(s) responsive to a query — and evaluates retrieval precision/recall without classifying what kind of provision was found. [[euro-5k-obligation-extraction]] treats it as a classification/extraction problem — deciding which sentences *are* obligations (of a specific reporting subtype) — and applies a definitional framework to include or exclude candidates. One optimizes for finding the right text; the other for typing the text as an obligation. Both report comparative results (retriever configurations; model families), which their own pages attribute to the respective authors.

## See also
[[obligation-extraction]] · [[precise-retrieval]] · [[legislative-document-model]]
