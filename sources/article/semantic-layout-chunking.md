---
title: "Enhancing RAG System Performance Through Semantic Layout Chunking"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Semantic Layout Chunking"]
publisher: "Qin, Sun, French, Liu (The University of Western Australia)"
url: https://link.springer.com/chapter/10.1007/978-981-95-4969-6_3
version: "AI 2025; LNAI vol 16370; DOI 10.1007/978-981-95-4969-6_3"
published: 2025-11
effective_from: 2025-11
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Enhancing RAG System Performance Through Semantic Layout Chunking

## Scope & purpose
This chapter proposes "semantic layout chunking," a document-chunking strategy for Retrieval-Augmented Generation (RAG) that combines semantic coherence signals with document layout/structural cues to determine chunk boundaries. It argues that combining both signals better preserves structural integrity and semantic flow, particularly in formal documents with logical organizational patterns, and evaluates the approach on the Unstructured Document Analysis (UDA) benchmark. It appeared in AI 2025 (Australasian Joint Conference on Artificial Intelligence), LNAI vol 16370, Springer, authored by Man Qin, Qiang Sun, Tim French, and Wei Liu (The University of Western Australia).

> _Only the abstract was retrievable (subscription content); claims beyond the abstract are from general knowledge — verify against the full chapter._

## Structure
Only the abstract and publisher metadata were available; the internal chapter structure could not be retrieved. Referenced code is at github.com/Lumanman9/Semantic_Layout_Chunking, and the stated evaluation dataset is the UDA (Unstructured Document Analysis) benchmark.

## Key points
- The paper proposes semantic layout chunking, arguing it better preserves both structural integrity and semantic flow, particularly in formal documents that follow logical organizational patterns ⟨Springer 10.1007/978-981-95-4969-6_3, Abstract⟩.
- It observes that chunking strategy is critical to RAG performance yet often overlooked, with common strategies being chunking by character or token count or recursive splitting ⟨Springer 10.1007/978-981-95-4969-6_3, Abstract⟩.
- It positions prior advanced approaches as relying either on semantic coherence between sentences or on presentational layout cues; the proposed method integrates both ⟨Springer 10.1007/978-981-95-4969-6_3, Abstract⟩.
- The method integrates semantic labels during chunk storage to enable structure retrieval ⟨Springer 10.1007/978-981-95-4969-6_3, Abstract⟩.
- The approach is evaluated on the Unstructured Document Analysis (UDA) dataset — PDF documents across multiple domains — against purely semantic and boundary-aware baselines on retrieval accuracy and question-answering accuracy, and is reported to achieve superior performance ⟨Springer 10.1007/978-981-95-4969-6_3, Abstract⟩.
- Semantic layout chunking is, in general terms, a hybrid that draws on layout-aware parsing (using section/heading structure and layout boundaries) alongside sentence-level semantic chunking, rather than either signal alone ⟨general knowledge⟩ [gen].

## Concepts & entities covered
Concepts: [[semantic-chunking]] · [[layout-aware-parsing]] · [[retrieval-evaluation]] · [[retrieval-augmented-generation]]
Entities: —
