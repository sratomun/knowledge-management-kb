---
title: "LegalBench-RAG benchmark"
type: entity
subtype: benchmark
aliases: []
tags: [knowledge-processing]
published: 2024-08
effective_from: 2024-08
effective_to: ongoing
status: current
concepts: ["[[precise-retrieval]]", "[[retrieval-evaluation]]"]
sources: ["[[legalbench-rag]]"]
updated: 2026-08-10
---

# LegalBench-RAG benchmark

## What it is
LegalBench-RAG is, as its authors describe it, the first benchmark designed to evaluate the retrieval step of retrieval-augmented generation in the legal domain. It measures how well a system retrieves minimal, highly relevant snippets from a legal corpus, complementing the generation-focused LegalBench benchmark.

## Key facts
- Its authors describe it as the first benchmark specifically designed to evaluate the retrieval component of RAG pipelines in the legal space ⟨[[legalbench-rag]] Abstract; §1⟩.
- It consists of 6,858 query–answer pairs entirely human-annotated by legal experts, over a corpus of more than 79M characters (reported as ~79.7M characters across 714 documents) ⟨[[legalbench-rag]] Abstract; §3⟩.
- The corpus is assembled from four source datasets — PrivacyQA, CUAD, MAUD, and ContractNLI — by retracing LegalBench annotations back to their original spans in the source documents ⟨[[legalbench-rag]] §3⟩.
- It emphasizes precise, minimal-snippet retrieval, with each query labelled by file path, exact quote, and precise character indices so that retrieved text can be cited ⟨[[legalbench-rag]] Abstract; §3⟩.
- A lightweight subset, LegalBench-RAG-mini, comprises 776 queries (194 from each source dataset) over 72 documents and 8.68M characters for rapid iteration ⟨[[legalbench-rag]] §3⟩.
- The benchmark evaluates retrieval only and, because each query is answered by exactly one document, does not assess multi-document (multi-hop) reasoning ⟨[[legalbench-rag]] §3⟩.

## Relations
- Realizes: [[precise-retrieval]] · [[retrieval-evaluation]]
- Defined in: [[legalbench-rag]]
- Related: [[cuad-dataset]]

## See also
[[precise-retrieval]] · [[retrieval-evaluation]] · [[obligation-lookup]] · [[legalbench-rag]]
