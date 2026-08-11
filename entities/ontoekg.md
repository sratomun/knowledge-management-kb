---
title: "OntoEKG"
type: entity
subtype: system
aliases: []
tags: [graph-rag]
published: 2026-02
effective_from: 2026-02
effective_to: ongoing
status: current
concepts: ["[[ontology-learning]]", "[[llm-kg-construction]]", "[[enterprise-knowledge-graph]]"]
sources: ["[[ontoekg-llm-ontology]]"]
updated: 2026-08-10
---

# OntoEKG

## What it is
OntoEKG is an LLM-driven pipeline from Liber AI Research that generates domain-specific ontologies from unstructured enterprise data to back enterprise knowledge graphs. It chains an extraction module (classes and properties) into an entailment module (class hierarchy) and serialises the result into standard RDF.

## Key facts
- Decomposes ontology modelling into two phases: an extraction module that identifies core classes and properties, and an entailment module that logically structures those elements into a hierarchy before RDF serialisation ⟨arXiv:2602.01276, Abstract⟩
- The extraction module (an Ontology Extraction LLM) identifies Classes (e.g. "Employee", "Vehicle") and Properties (relationships such as "operates", "hasAccessTo") from raw unstructured text ⟨arXiv:2602.01276, §III.B.2⟩
- The entailment module (an Entailment LLM) iteratively analyses extracted classes to infer inheritance relationships using logical reasoning over class descriptions ⟨arXiv:2602.01276, §III.B.3⟩
- Merges the extracted properties and constructed hierarchy and serialises them to RDF triples (owl:Class and owl:ObjectProperty) via the rdflib library, saving a Turtle file ⟨arXiv:2602.01276, §III.B.4⟩
- Enforces structured LLM output with strict Pydantic data models, forcing valid JSON carrying classes, properties, descriptions, domains, and ranges ⟨arXiv:2602.01276, §III.B.1⟩
- Specifically targets enterprise data, reifying datatypes into their own classes as in Schema.org ⟨arXiv:2602.01276, §III / §III.A⟩
- Positioned as a text-to-ontology contribution paired with a call to develop a comprehensive benchmark for evaluating ontology construction from text ⟨arXiv:2602.01276, §III⟩
- Evaluated with Google Gemini 3 Flash (preview) for extraction and Anthropic Claude 4.5 Opus for entailment on Google Colab, reaching a fuzzy-match F1 of 0.724 in the Data domain ⟨arXiv:2602.01276, §IV.B⟩
- Source code and data are published at the OntoEKG GitHub repository (github.com/LiberAI/OntoEKG) ⟨arXiv:2602.01276, §IV.A⟩

## Relations
- Realizes: [[ontology-learning]] · [[llm-kg-construction]] · [[enterprise-knowledge-graph]]
- Defined in: [[ontoekg-llm-ontology]]
- Related: [[org-liber-ai]]

## See also
[[ontoekg-llm-ontology]] · [[org-liber-ai]]
