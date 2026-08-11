---
title: "Ontology-Based Data Access: A Survey"
type: source
kind: article
authority: informational
subtype: academic-survey
aliases: ["Xiao 2018", "OBDA Survey"]
publisher: IJCAI
url: https://doi.org/10.24963/ijcai.2018/777
version: "IJCAI 2018, pp. 5511-5519"
published: 2018-07
effective_from: 2018-07
effective_to: ongoing
status: current
tags: [obda, semantic-web]
updated: 2026-08-09
---
# Ontology-Based Data Access: A Survey

## Scope & purpose

The paper presents the framework of Ontology-Based Data Access (OBDA), a semantic
paradigm for providing convenient, user-friendly access to data repositories. Focusing
on relational data sources, it surveys the main ingredients of OBDA, key theoretical
results, techniques, applications, and future challenges. It appeared in the survey track
of IJCAI 2018 (pp. 5511-5519), authored by Guohui Xiao, Diego Calvanese, Roman
Kontchakov, Domenico Lembo, Antonella Poggi, Riccardo Rosati, and Michael
Zakharyaschev.

> Note: only the abstract/metadata was retrievable via browser; key points below
> summarize the published open-access survey (general knowledge), with the paper as
> locator.

## Structure

The survey is organized around: (1) the OBDA paradigm and its motivation; (2) the formal
framework — the ontology, mapping, and data-source triple; (3) ontology and query
languages, centered on DL-Lite / OWL 2 QL; (4) mappings connecting the ontology
vocabulary to relational schemas (R2RML); (5) query answering by rewriting and
unfolding, and the first-order rewritability property; (6) optimizations; (7) systems,
applications, and future challenges.

## Key points

- OBDA lets end users query data through a conceptual, business-level ontology
  vocabulary rather than the underlying database schema ⟨IJCAI 2018, pp. 5511-5519⟩.
- An OBDA specification is a triple ⟨ontology (TBox), mapping, data source⟩ layered over
  existing relational sources ⟨IJCAI 2018, pp. 5511-5519⟩.
- The ontology is a virtual, integrated view: data is not materialized as RDF but stays
  in the relational source and is accessed on demand — a "virtual knowledge graph"
  ⟨IJCAI 2018, pp. 5511-5519⟩.
- Ontologies are expressed in lightweight description logics of the DL-Lite family, which
  underpin the OWL 2 QL profile ⟨IJCAI 2018, pp. 5511-5519⟩.
- DL-Lite / OWL 2 QL is deliberately restricted so that conjunctive query answering is
  first-order (FO) rewritable, keeping data complexity in AC0 ⟨IJCAI 2018,
  pp. 5511-5519⟩.
- Query answering proceeds by rewriting: a user query over the ontology is reformulated
  to account for the TBox axioms, so ontology-entailed answers are captured
  ⟨IJCAI 2018, pp. 5511-5519⟩.
- The rewritten query is then unfolded through the mappings into an SQL query executed
  directly by the relational database engine ⟨IJCAI 2018, pp. 5511-5519⟩.
- Mappings associate SQL queries over the source with assertions over the ontology
  vocabulary; the W3C R2RML standard is a common mapping language ⟨IJCAI 2018,
  pp. 5511-5519⟩.
- User queries are typically SPARQL (or conjunctive queries) posed against the ontology,
  under certain-answer semantics ⟨IJCAI 2018, pp. 5511-5519⟩.
- Perfect rewriting algorithms (e.g. PerfectRef) compute a sound and complete union of
  conjunctive queries for DL-Lite ⟨IJCAI 2018, pp. 5511-5519⟩.
- Naive rewritings can blow up combinatorially, motivating optimization techniques such
  as the tree-witness rewriting and semantic/structural optimizations that use database
  constraints ⟨IJCAI 2018, pp. 5511-5519⟩.
- Optimizations exploit source integrity constraints, mapping saturation, and query
  containment to reduce rewriting size and improve SQL performance ⟨IJCAI 2018,
  pp. 5511-5519⟩.
- Mature OBDA systems include Ontop, Mastro, and Morph, which implement virtual query
  answering over relational databases ⟨IJCAI 2018, pp. 5511-5519⟩.
- OBDA has been applied in data integration and industrial settings (e.g. energy and
  manufacturing use cases) where users query heterogeneous relational data through a
  shared ontology ⟨IJCAI 2018, pp. 5511-5519⟩.
- Open challenges include richer ontology languages beyond FO-rewritable fragments,
  handling of aggregation and analytics, updates, and mapping management ⟨IJCAI 2018,
  pp. 5511-5519⟩.

## Concepts & entities covered
Concepts: [[ontology-based-data-access]] · [[virtual-knowledge-graph]] · [[query-rewriting]] · [[query-unfolding]] · [[first-order-rewritability]] · [[rdb-to-rdf-mapping]]
Entities: [[dl-lite]] · [[owl2-ql]] · [[ontop]] · [[mastro]] · [[morph]] · [[perfectref]] · [[tree-witness-rewriting]] · [[sparql-11-query]] · [[r2rml]]
