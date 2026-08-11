---
title: "Financial Report Chunking for Effective Retrieval Augmented Generation"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Financial report chunking"]
publisher: "Jimeno Yepes, You, Milczek, Laverde, Li (Unstructured Technologies)"
url: https://arxiv.org/abs/2402.05131
version: "arXiv:2402.05131v3 [cs.CL]"
published: 2024
effective_from: 2024-02
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# Financial Report Chunking for Effective Retrieval Augmented Generation

## Scope & purpose
This paper proposes chunking documents primarily by their structural element components (element-type-based chunking) rather than by fixed-size paragraph splits, arguing that treating all text as equal neglects information in document structure. The authors (Unstructured Technologies) introduce a framework to evaluate how element-type-based chunking — with element types annotated by document-understanding models — affects retrieval context, retrieval accuracy, and downstream RAG question-answering. Findings are reported on U.S. SEC financial reports using the FinanceBench dataset.

## Structure
The paper is organized as: (1) an introduction on context-window limits, chunking, and RAG for financial reports (10-Ks, 10-Qs, 8-Ks); (2) related work surveying fixed-size, recursive, contextual, and hybrid chunking and prior financial-document structure work; (3) methods — the RAG setup, baseline vs. element-based chunking strategies, and metadata enrichment; (4) results on retrieval and Q&A accuracy plus efficiency; and (5–6) discussion and conclusion.

## Key points
- The authors propose chunking documents primarily by structural element components (element types), contrasting this with fixed-size, recursive, contextual, and hybrid strategies that overlook document structure ⟨arXiv:2402.05131, Abstract / §2⟩.
- Element types are extracted with computer vision plus NLP using the Unstructured library and Chipper, a vision encoder-decoder model (inspired by Donut) that outputs a JSON representation of per-page elements with element type, bounding box, and text ⟨arXiv:2402.05131, §3⟩.
- Element-based chunks are formed by iteratively merging elements up to a target length without breaking an element, starting a new chunk at each TITLE element, and starting a new chunk at each TABLE element while preserving the entire table ⟨arXiv:2402.05131, §3⟩.
- Chunks are enriched with three metadata representations: up to six GPT-4 keywords, a GPT-4 summarized paragraph, and a "Naive" prefix (first two sentences, plus table caption description for tables) ⟨arXiv:2402.05131, §3⟩.
- The RAG setup indexes chunks into a Weaviate vector DB, encodes with a multi-qa-mpnet-base-dot-v1 sentence transformer, retrieves the top-10 chunks per question, and generates answers with GPT-4, varying only the chunking method ⟨arXiv:2402.05131, §3⟩.
- Evaluation uses FinanceBench (open-book financial questions); the authors recovered 80 documents yielding 141 questions, with documents ranging 4–549 pages (avg 147.34) and evidence spread through the documents ⟨arXiv:2402.05131, §3⟩.
- The authors report that combining chunking strategies (aggregation) yields the highest retrieval scores — Chipper Aggregation reaching 84.40% page accuracy, ROUGE 0.568, and BLEU 0.452 — and that basic chunking has higher page-level but lower and less consistent paragraph-level accuracy than element-based strategies ⟨arXiv:2402.05131, §4⟩.
- The authors report that element-based chunking gives the best Q&A accuracy (manual accuracy up to 53.19% vs. 48.23% for Base 512), consistent with its retrieval accuracy ⟨arXiv:2402.05131, §4 / §5-6⟩.
- The authors state that dissecting documents into constituent elements yields the best chunk size without tuning the token-count hyper-parameter, making the method more generalizable to new document types, whereas the best basic chunk size varies from dataset to dataset ⟨arXiv:2402.05131, Abstract / §4 / §5-6⟩.
- The authors report an efficiency advantage: element-based chunking achieves the highest retrieval scores with only about half the chunks of structure-agnostic aggregation methods (62,529 vs. 112,155), reducing indexing cost and query latency ⟨arXiv:2402.05131, §4⟩.

## Concepts & entities covered
Concepts: [[structure-aware-chunking]] · [[semantic-chunking]] · [[extraction-verification]] · [[retrieval-augmented-generation]]
Entities: —
