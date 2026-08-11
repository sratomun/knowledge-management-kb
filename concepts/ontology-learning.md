---
title: "Ontology Learning"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[llm-kg-construction]]", "[[schema-based-vs-schema-free-construction]]", "[[enterprise-knowledge-graph]]", "[[upper-ontology]]"]
updated: 2026-08-10
---

# Ontology Learning

## What it is
Ontology learning is the (semi-)automatic construction of an ontology — the classes, properties, and hierarchical relationships that describe a domain — from text or data rather than by manual expert modelling. In the LLM era, a model is prompted to read source material and propose the ontological vocabulary and its subsumption structure, which can then be serialized into a formal representation such as OWL/RDF.

## How sources treat it
- **[[llm-kg-construction-survey]]** _(article · informational)_ — In the pre-LLM era ontologies were mainly hand-built by domain experts using tools such as Protégé and methodologies like METHONTOLOGY and On-To-Knowledge, offering rigor but limited scalability; semi-automatic ontology learning sought to derive ontological structures from corpora but even frameworks such as NeOn struggled with evolution, modular reuse, and dynamic adaptation ⟨§2.1⟩
- **[[llm-kg-construction-survey]]** _(article · informational)_ — In the top-down paradigm, LLMs act as co-modelers that translate natural-language specifications — competency questions, user stories, domain descriptions — into formal ontologies (typically OWL), with frameworks such as Ontogenia, CQbyCQ, LLMs4OL, and NeOn-GPT ⟨§3.1⟩
- **[[ontoekg-llm-ontology]]** _(article · informational)_ — Runs a two-step LLM process — first extracting classes and properties, then reasoning about hierarchical (subclass) relationships between those classes — before RDF serialisation ⟨arXiv:2602.01276, §III.B⟩
- **[[ontoekg-llm-ontology]]** _(article · informational)_ — An Entailment LLM iteratively analyses the extracted classes to determine inheritance relationships (e.g. checking whether "Apple" is a subclass of "Fruit"), using logical reasoning over the class descriptions ⟨arXiv:2602.01276, §III.B.3⟩
- **[[all-relations-rome]]** _(article · informational)_ — Uses an input ontology that defines allowed entity and relation types but is generally weakly defined and encoded in textual form, so an LLM can enforce it via system-prompt instructions rather than as a standard formal ontology ⟨§4.1.1⟩

## Where sources differ
The sources describe ontology learning at different points on a formality spectrum, and are complementary rather than in conflict. [[llm-kg-construction-survey]] and [[ontoekg-llm-ontology]] treat the target as a formal ontology (OWL/RDF classes, properties, subclass hierarchy), with OntoEKG also reporting characteristic LLM failure modes (proposing individuals instead of classes, confusing subsumption directionality). [[all-relations-rome]], by contrast, deliberately uses a weak, textual ontology enforced only through prompting — an explicit choice to trade formal rigor for simplicity in a QA-generation setting.

## See also
[[llm-kg-construction]] · [[schema-based-vs-schema-free-construction]] · [[enterprise-knowledge-graph]] · [[upper-ontology]]
