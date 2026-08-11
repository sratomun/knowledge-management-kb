---
title: "MedGraphRAG"
type: entity
subtype: system
aliases: []
tags: [knowledge-processing]
published: 2024
effective_from: 2024-10
effective_to: ongoing
status: current
concepts: ["[[domain-specific-rag]]", "[[evidence-grounded-generation]]"]
sources: ["[[medical-graph-rag]]"]
updated: 2026-08-10
---

# MedGraphRAG

## What it is
MedGraphRAG is a graph-based RAG framework specifically designed for the medical domain, built
on Triple Graph Construction and U-Retrieval to produce evidence-based, citation-backed medical
responses from private medical data ⟨abstract⟩.

## Key facts
- Its Triple Graph Construction links user documents to credible medical sources and controlled
  vocabularies, turning each RAG entity into a [RAG entity, source, definition] triple that the
  source says makes responses traceable to sources and definitions ⟨abstract, §2.1⟩.
- The RepoGraph it links into has two layers: a bottom UMLS graph of authoritative
  vocabularies and an upper layer of medical textbooks and scholarly articles, connected by
  "the reference of" and "the definition of" edges ⟨§2.1⟩.
- Instead of GraphRAG's hierarchical community construction, it tags each Meta-MedGraph with
  predefined medical categories and uses agglomerative hierarchical clustering with dynamic
  thresholding (up to 12 layers) to generate tag summaries ⟨§2.2⟩.
- Its U-Retrieval combines Top-down Precise Retrieval (from top tag layer down to the target
  Meta-MedGraph) with Bottom-up Response Refinement, which the source says balances global
  context awareness with retrieval efficiency ⟨§2.3⟩.
- The source paper reports that MedGraphRAG consistently outperforms SOTA on medical benchmarks
  and, applied to Llama-70B or GPT, sets a new state of the art across all 11 datasets,
  outperforming fine-tuned medical LLMs such as Med-PaLM 2 and Med-Gemini ⟨abstract, §3⟩.
- The source paper's ablation reports the largest gains from adding Triple Graph Construction,
  and human evaluation is reported as rating it highest in citation precision/recall and
  understandability ⟨§3⟩.

## Relations
- Realizes / relates to: [[domain-specific-rag]] · [[evidence-grounded-generation]]
- Defined in: [[medical-graph-rag]]

## See also
[[medical-graph-rag]]
