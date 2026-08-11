---
title: "ROME (KG creation + question generation framework)"
type: entity
subtype: framework
aliases: ["ARLtR framework"]
tags: [graph-rag]
published: 2026
effective_from: 2026-07
effective_to: ongoing
status: current
concepts: ["[[llm-kg-construction]]", "[[entity-relation-extraction]]", "[[fact-grounded-question-generation]]"]
sources: ["[[all-relations-rome]]"]
updated: 2026-08-10
---

# ROME (KG creation + question generation framework)

## What it is
ROME (All Relations Lead to Rome, ARLtR) is a unified, domain-agnostic framework for
automated knowledge graph construction and fact-grounded question-answer generation. It
jointly produces a knowledge graph, chunk and entity embeddings, and QA pairs explicitly
grounded in extracted entities, relations, and supporting textual evidence.

## Key facts
- The framework has two phases: (i) knowledge graph creation and (ii) fact-grounded
  question-answer generation ⟨§4⟩.
- Phase 1 proceeds through inputs (documents + ontology), sampling (chunking), annotation
  (entity then relation extraction), generation (integration into the KG), and embedding
  ⟨§4.1⟩.
- It uses a weak ontology encoded in textual form and enforced by an LLM via system-prompt
  instructions, only specifying entity and relation types rather than a full formal ontology
  ⟨§4.1.1⟩.
- Relation extraction can be done as direct triplet extraction or as a two-step
  chain-of-thought (entities first, then relations), improving accuracy for larger
  ontologies ⟨§4.1.3⟩.
- Entities and relations are merged by title regardless of capitalization to reduce
  duplicates during KG generation ⟨§4.1.4⟩.
- Phase 2 defines question configurations and persona specifications, retrieves chunks,
  extracts facts, generates a base question, and reformulates it per persona ⟨§4.2⟩.
- Question configurations cover question type, relation, complexity, persona, and existent
  categories ⟨§4.2.1, Table 1⟩.
- Persona reformulation uses three expertise levels — novice, intermediate, and expert — to
  produce question variants ⟨§4.2.4, Table 2⟩.
- The framework is intentionally domain-agnostic; its weak ontology lowers upfront
  ontological engineering and generalizes to domains such as medical or financial ⟨§6.1⟩.
- It was instantiated as the ARLtR Roman-Empire dataset in Neo4j with 19,374 entities,
  16,069 chunks, and 8,400 QA pairs ⟨§5.1, §5.3⟩.

## Relations
- Realizes / relates to: [[llm-kg-construction]] · [[entity-relation-extraction]] · [[fact-grounded-question-generation]]
- Defined in: [[all-relations-rome]]

## See also
[[all-relations-rome]]
