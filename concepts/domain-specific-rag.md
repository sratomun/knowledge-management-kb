---
title: "Domain-specific RAG"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[retrieval-augmented-generation]]", "[[graphrag]]"]
updated: 2026-08-10
---

# Domain-specific RAG

## What it is
Domain-specific RAG is retrieval-augmented generation specialized to a particular knowledge domain — medicine, law, finance — by grounding retrieval in that domain's authoritative sources, controlled vocabularies, and structural conventions rather than a generic corpus. The specialization can appear in the graph or index construction (linking content to domain ontologies), the retrieval strategy (domain-aware hierarchies), and the evaluation (domain expert judgment). The motivation is that general-purpose RAG may be too coarse or may distort domain-specific terminology and established facts.

## How sources treat it
- **[[medical-graph-rag]]** _(article · informational)_ — presents a graph-based RAG framework designed specifically for the medical domain, motivated against general-purpose GraphRAG which the authors say is overly complex for general use and lacks the ability to generate evidence-based, credibility-authenticated responses — a limitation they argue is critical in medicine where precise terminology and established truths must not be distorted ⟨abstract, §1⟩
- **[[medical-graph-rag]]** _(article · informational)_ — grounds the domain via Triple Graph Construction, linking user documents to credible medical sources and controlled vocabularies (a RepoGraph with a bottom UMLS layer and an upper layer of textbooks/scholarly articles), typing entities by UMLS semantic types ⟨abstract, §2, §2.1⟩
- **[[medical-graph-rag]]** _(article · informational)_ — reports MedGraphRAG outperforming SOTA, with roughly 8% (fact-checking) and 5% (Q&A) improvement over GraphRAG and more pronounced gains in smaller LLMs, which the authors attribute to the framework acting as external memory ⟨abstract, §3⟩

## Where sources differ
Only one source treats domain-specific RAG directly here. Its comparative claims — outperforming general GraphRAG and fine-tuned medical LLMs such as Med-PaLM 2 and Med-Gemini, and the ablation attributing gains to Triple Graph Construction plus U-Retrieval acting together — are reported as the authors' own findings on medical benchmarks, not as KB conclusions. The paper's argument that general-purpose GraphRAG is "overly complex" for the medical setting is its motivating claim, attributed to its authors.

## See also
[[retrieval-augmented-generation]] · [[graphrag]]
