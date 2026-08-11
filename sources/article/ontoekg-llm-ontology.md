---
title: "LLM-Driven Ontology Construction for Enterprise Knowledge Graphs"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["OntoEKG paper"]
publisher: "Liber AI Research"
url: https://arxiv.org/abs/2602.01276
version: "arXiv:2602.01276v1"
published: 2026-02
effective_from: 2026-02
effective_to: ongoing
status: current
tags: [graph-rag]
concepts: ["[[ontology-learning]]", "[[llm-kg-construction]]", "[[enterprise-knowledge-graph]]"]
entities: ["[[ontoekg]]", "[[org-liber-ai]]"]
updated: 2026-08-10
---

# LLM-Driven Ontology Construction for Enterprise Knowledge Graphs

## Scope & purpose
A paper by Abdulsobur Oyewale and Tommaso Soru (Liber AI Research, London) introducing **OntoEKG**, an LLM-driven pipeline for generating domain-specific ontologies from unstructured enterprise data to back enterprise knowledge graphs (EKGs) ⟨arXiv:2602.01276, Abstract⟩. It frames ontology construction as a resource-intensive, largely manual task dependent on domain expertise, and positions the LLM pipeline as an AI copilot that accelerates modelling while preserving semantic quality and governance ⟨arXiv:2602.01276, §I⟩. Written for semantic-web and data-engineering researchers and practitioners.

## Structure
The paper is organised as: §I Introduction (motivation: RDF/semantic tech in the enterprise, manual ontology cost); §II Related Work (prior semi-automatic and LLM-based ontology/KG construction); §III Approach (formalisation and the two-phase pipeline); §IV Evaluation (benchmark gap, custom dataset, exact- and fuzzy-match experiments, limitations); §V Conclusion (contributions and future work) ⟨arXiv:2602.01276, §I–§V⟩.

## Key points
- OntoEKG decomposes ontology modelling into two distinct phases: an extraction module that identifies core classes and properties, and an entailment module that logically structures those elements into a hierarchy before serialising them into standard RDF ⟨arXiv:2602.01276, Abstract⟩
- The pipeline runs a two-step LLM process — first extracting classes and properties, then reasoning about hierarchical (subclass) relationships between those classes ⟨arXiv:2602.01276, §III.B⟩
- Data ingestion enforces structured output using strict Pydantic data models, forcing the LLM to emit valid JSON carrying classes, properties, descriptions, domains, and ranges ⟨arXiv:2602.01276, §III.B.1⟩
- An Ontology Extraction LLM identifies two core elements — Classes (e.g. "Employee", "Vehicle") and Properties (relationships such as "operates", "hasAccessTo") ⟨arXiv:2602.01276, §III.B.2⟩
- An Entailment LLM iteratively analyses the extracted classes to determine inheritance relationships (e.g. checking whether "Apple" is a subclass of "Fruit"), using logical reasoning over the class descriptions ⟨arXiv:2602.01276, §III.B.3⟩
- RDF serialisation uses the rdflib library to convert the merged properties and hierarchy into structured RDF triples (owl:Class and owl:ObjectProperty) saved to a Turtle file ⟨arXiv:2602.01276, §III.B.4⟩
- The two contributions are a text-to-ontology construction pipeline that specifically targets enterprise data, and a call to develop a comprehensive benchmark for evaluating ontology construction from text ⟨arXiv:2602.01276, §III⟩
- The authors adopt their own evaluation dataset of three use cases — excerpts of internal enterprise policy text from the Data, Finance, and Logistics sectors — created to address the lack of end-to-end ontology-construction benchmarks ⟨arXiv:2602.01276, §IV.A⟩
- Fuzzy-match (embedding-based) F1 scores were 0.724 in the Data domain (P=0.656, R=0.807), 0.121 in Finance (P=0.095, R=0.166), and 0.431 in Logistics (P=0.366, R=0.523) ⟨arXiv:2602.01276, §IV.B, Table II⟩
- Exact-match scores were far lower — Data F1=0.102, Finance 0, Logistics F1=0.048 — with the Data use case best overall and Finance the most challenging, attributed to differing interpretations of the input text ⟨arXiv:2602.01276, §IV.B, Table I⟩
- Experiments ran on Google Colab, using Google Gemini 3 Flash (preview) for ontological extraction and Anthropic Claude 4.5 Opus for entailment ⟨arXiv:2602.01276, §IV.B⟩
- Limitation 1: determining the optimal scope of a model is hard for an LLM to manage autonomously, requiring explicit signalling to bound the relevant classes and properties ⟨arXiv:2602.01276, §IV.B⟩
- Limitation 2: the LLM tends to propose individuals instead of classes, owing to no explicit requirement about the target level of abstraction ⟨arXiv:2602.01276, §IV.B⟩
- Limitation 3: during entailment, LLMs confuse the directionality of hierarchy relations and adopt loose definitions of subsumption, harming the logical consistency of the RDF model ⟨arXiv:2602.01276, §IV.B⟩
- Future work targets end-to-end text-to-RDF translation, handling named individuals and entity metadata with provenance, progressive ontology construction by feeding an existing model back into OntoEKG, and community development of an ontology-construction benchmark ⟨arXiv:2602.01276, §V⟩

## Concepts & entities covered
Concepts: [[ontology-learning]] · [[llm-kg-construction]] · [[enterprise-knowledge-graph]]
Entities: [[ontoekg]] · [[org-liber-ai]]
