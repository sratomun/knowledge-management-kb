---
title: "All Relations Lead to Rome: Automated Knowledge Graph Creation and Question Generation"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["ARLtR"]
publisher: arXiv
url: https://arxiv.org/abs/2606.22645
published: 2026
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [graph-rag]
updated: 2026-08-10
---
# All Relations Lead to Rome: Automated Knowledge Graph Creation and Question Generation

## Scope & purpose

The paper introduces All Relations Lead to Rome (ARLtR), a unified framework for automated
knowledge graph construction and fact-grounded question-answer generation, authored by
Matthijs Jansen op de Haar (University of Twente), Tobias Stähle (ETH Zürich), and Lorenzo
Gatti (University of Twente). It targets a gap in existing QA resources: no single dataset
jointly provides vector-based retrieval over embedded chunks, an explicit knowledge graph,
ground-truth entity/relation annotations, and QA pairs grounded in the same corpus. The
framework is instantiated as a historical dataset centered on the Roman Empire (over 19,000
entities, 16,000 chunks, 8,400 QA pairs).

## Structure

The paper runs: introduction and the four-component gap it addresses (§1); background on KG
construction and QA generation pipelines (§2); related work across vector-based, KG, and
hybrid QA datasets (§3); the two-phase framework and methodology with a running Roman-Empire
example (§4 — KG creation §4.1, QA generation §4.2); the instantiated ARLtR dataset,
ontology, and QA statistics (§5); discussion of implications, limitations, and future work
(§6); and a persona-prompt appendix (Appendix A).

## Key points

- ARLtR is a unified, entity- and relation-centric framework that integrates vector-based
  retrieval, KG structure, and fact-grounded question-answer generation over a shared corpus
  ⟨§1⟩.
- Phase 1 (KG creation) splits an unstructured text dataset into chunks, extracts entities
  with an LLM according to an ontology, adds them to a knowledge graph, then computes
  embeddings for both entities and chunks to enable vector retrieval ⟨§4.1⟩.
- The input ontology defines allowed entity and relation types and is generally weakly
  defined and encoded in textual form, so an LLM can enforce it via system-prompt
  instructions rather than as a standard formal ontology ⟨§4.1.1⟩.
- Documents are chunked into fixed-size (token) chunks that may overlap to avoid losing
  context; chunk length is a fundamental design trade-off since larger chunks need fewer LLM
  calls while smaller chunks improve recall ⟨§4.1.2⟩.
- Annotation uses an LLM-based entity tagger; relations are obtained either by directly
  extracting triplets or by a two-step process of entity annotation followed by relation
  extraction, the latter a chain-of-thought that improves accuracy for larger ontologies
  ⟨§4.1.3⟩.
- During KG generation, entities and relations are merged by title regardless of
  capitalization to avoid duplicates, and the stage should enforce valid types since
  LLM annotation may introduce incorrect labels ⟨§4.1.4⟩.
- Embeddings are computed per chunk with a pre-trained model in a fixed-dimensional space,
  stored as chunk attributes, and optionally computed for entities to enable entity-level
  dense retrieval such as cosine similarity ⟨§4.1.5⟩.
- Phase 2 (QA generation) pre-defines question configurations and persona specifications,
  selects entities, retrieves associated chunks, extracts facts, formulates a base question,
  and reformulates it per persona ⟨§4.2⟩.
- Question configurations span question type (factoid vs open), relation (entity vs
  relation), complexity (single vs double), persona (novice/intermediate/expert), and
  existent (in vs not in dataset) ⟨§4.2.1, Table 1⟩.
- Sampling retrieves chunks via four strategies — Single-Entity, Double-Entity,
  Single-Relation, and Double-Relation (a relational hop) — with at least five chunks
  required per configuration in ARLtR ⟨§4.2.2⟩.
- An LLM fact extractor selects one or more facts from the retrieved chunks, framed by the
  question configuration so each fact corresponds to the specified entity and relations
  rather than an unrelated chunk fact ⟨§4.2.3⟩.
- A base question is generated that requires the extracted facts to answer, with the fact as
  ground-truth answer, then reformulated across three persona expertise levels (novice,
  intermediate, expert) to produce variants ⟨§4.2.4, Table 2⟩.
- The instantiated ARLtR dataset is built in Neo4j from 300 Wikipedia articles, using an LLM
  (minimax 2.7) and embedding model (gemini-embedding-2, 3,072 dimensions), yielding 16,069
  chunks, 19,374 entities, and 25,304 relations, with Rome the highest-degree node ⟨§5.1⟩.
- ARLtR adopts a weak ontology grounded in historical literature with entity types CITY,
  COUNTRY, REGION, HISTORICAL EVENT, PERSON, STATE, ARTICLE, allowing all types to relate
  without hard constraints on admissible relation pairs ⟨§5.2⟩.
- The dataset provides 8,400 QA pairs — 6,000 grounded in KG entities and 2,400 concerning
  entities or facts not present — enabling evaluation of retrieval precision on unanswerable
  questions ⟨§5.3⟩.

## Concepts & entities covered
Concepts: [[llm-kg-construction]] · [[entity-relation-extraction]] · [[fact-grounded-question-generation]]
Entities: [[rome-framework]]
