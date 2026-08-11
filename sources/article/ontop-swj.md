---
title: "Ontop: Answering SPARQL Queries over Relational Databases"
type: source
kind: article
authority: informational
subtype: academic-paper
aliases: ["Ontop SWJ", "Calvanese 2017 Ontop"]
publisher: "Semantic Web Journal"
url: https://www.semantic-web-journal.net/content/ontop-answering-sparql-queries-over-relational-databases
version: "SWJ 8(3), 2017"
published: 2017-01
effective_from: 2017-01
effective_to: ongoing
status: current
tags: [obda, semantic-web]
updated: 2026-08-10
---

# Ontop: Answering SPARQL Queries over Relational Databases

## Scope & purpose

This is the system paper for Ontop, a mature open-source Ontology-Based Data Access
(OBDA) system that lets users query relational databases through a conceptual ontology to
which the data sources are mapped. Authored by Diego Calvanese, Benjamin Cogrel, Sarah
Komla-Ebri, Roman Kontchakov, Davide Lanti, Martin Rezk, Mariano Rodriguez-Muro, and
Guohui Xiao (Free University of Bozen-Bolzano, Birkbeck, and IBM TJ Watson), it appeared
in the Semantic Web Journal. The paper describes Ontop's key features — solid theoretical
foundations, a virtual (non-materializing) approach implemented via query rewriting,
extensive optimizations across the whole OBDA architecture, compliance with the relevant
W3C recommendations (SPARQL, R2RML, OWL 2 QL, RDFS), and support for all major relational
databases — and reviews its architecture, ecosystem, query-answering techniques,
industrial applications, and competing systems.

## Structure

- §1 Introduction — the shift to heterogeneous data sources; OBDA as a conceptual layer
  over relational data; the virtual RDF graph; a running hospital-database example.
- §2 Architecture of Ontop — the four layers (inputs, core, API, application); inputs
  (ontology, mappings, queries, databases) (§2.1); the Quest core (§2.2); API layer —
  OWL API and Sesame/SAIL (§2.3); application layer — Protégé plugin, Sesame Workbench
  SPARQL endpoint, Optique Platform (§2.4).
- §3 Ecosystem — mapping bootstrapping and the Direct Mapping (§3.1); ontology
  bootstrapping (§3.2); SQL federation (§3.3); SPARQL federation (§3.4); ontology-based
  query interfaces (§3.5).
- §4 Answering SPARQL Queries — the off-line stage: ontology classification, T-mapping
  construction, T-mapping optimization (§4.1); the online stage: SPARQL-to-SQL
  translation (§4.2.1), SQL optimization (§4.2.2), execution (§4.2.3), performance
  (§4.2.4).
- §5 Industrial Applications — the Statoil and Siemens use cases in the Optique project.
- §6 Related SPARQL Query Answering Systems — triplestores (§6.1) and OBDA systems (§6.2),
  summarized in a feature matrix (Table 1).
- §7 A Retrospective — five years of Ontop development, from QuOnto/Mastro to Quest.
- §8 Conclusion — summary and future directions.

## Key points

- Ontop is an open-source (Apache-licensed) OBDA system developed at the Free University
  of Bozen-Bolzano that exposes relational databases as virtual RDF graphs by linking
  ontology terms (classes and properties) to the sources through mappings, then answering
  SPARQL by translating it into SQL transparently to the user ⟨§2⟩.
- Ontop takes a virtual approach that avoids materializing triples and is implemented
  through query rewriting; keeping the RDF graph virtual sidesteps the cost of
  materialization and profits from more than 30 years' maturity of relational systems ⟨§1⟩.
- To the authors' knowledge, Ontop is the first OBDA system to support all the W3C
  recommendations related to OBDA — OWL 2 QL, R2RML, SPARQL, SWRL, and the OWL 2 QL
  entailment regime in SPARQL — as well as all major commercial and open-source relational
  databases via JDBC ⟨§2.1⟩.
- The architecture has four layers: the inputs (ontology, database, mappings, queries),
  the core (query translation, optimization, execution), the API layer, and the
  application layer that exposes SPARQL query answering to end users ⟨§2⟩.
- Ontology languages are RDFS and OWL 2 QL; OWL 2 QL is based on the DL-Lite family of
  lightweight description logics, which guarantees that queries over the ontology can be
  rewritten into equivalent queries over the databases (Ontop has also been extended to a
  fragment of SWRL) ⟨§2.1⟩.
- Ontop supports two mapping languages — the W3C R2RML standard and an easier-to-use
  native Ontop mapping language, inter-convertible with R2RML; a mapping assertion pairs a
  source (an SQL query retrieving values) with a target (RDF triples built from those
  values) ⟨§2.1⟩.
- The core of Ontop is the SPARQL engine Quest, in charge of rewriting SPARQL over the
  virtual RDF graph into SQL over the relational database ⟨§2.2⟩.
- A surrounding ecosystem supports OBDA deployment: mapping bootstrappers (Ontop's own
  plus MIRROR, BootOX, Karma) that often follow the W3C Direct Mapping to generate
  mappings from schemas, ontology bootstrappers, SQL federation (e.g. Teiid, Exareme), and
  SPARQL federation in both seamless and SPARQL 1.1 SERVICE forms ⟨§3⟩.
- Query answering is split into an off-line stage — ontology classification, T-mapping
  construction, and T-mapping optimization — and an online stage that translates a SPARQL
  query into optimized SQL exploiting the T-mappings and the database integrity
  constraints ⟨§4⟩⟨§4.1⟩.
- T-mappings are constructed by composing the classified class/property hierarchy with the
  user mappings, so that RDF triples entailed by the ontology (e.g. inferred :Neoplasm
  instances that have no explicit user mapping) are captured in the mapping layer ⟨§4.1⟩.
- The T-mappings are then optimized using SQL disjunction (OR) and interval expressions
  together with semantic query optimization (SQO); the SQO containment check is
  NP-complete but is run only once during the off-line stage, so it has a negligible
  effect on online query processing ⟨§4.1⟩.
- The online SPARQL-to-SQL translation (Algorithm 1) walks the SPARQL algebra tree
  bottom-up, replacing each triple-pattern leaf by the union of the T-mapping SQL
  definitions of its predicate and mapping the SPARQL operators JOIN, OPTIONAL, UNION,
  FILTER, and PROJECT onto InnerJoin, LeftJoin, Union, Filter, and Project ⟨§4.2.1⟩.
- The generated SQL is improved by structural optimizations — pushing joins inside unions,
  pushing functions up the query tree, and eliminating sub-queries ("de-IRIing" joins over
  string concatenations) — and by semantic optimization that uses primary/foreign keys to
  remove redundant self-joins ⟨§4.2.2⟩.
- The tree-witness query rewriting algorithm was implemented to drastically reduce the
  size of rewritings and to take advantage of the T-mappings and the Semantic Index
  (Ontop's RDF-triplestore-mode structure) ⟨§7⟩.
- Performance depends more on the complexity of the ontology-plus-mappings than on dataset
  size, consistent with the worst-case exponential SPARQL-to-SQL translation; on BSBM,
  FishMark, and LUBM (25–200 million triples) Ontop outperforms competitors by orders of
  magnitude, whereas on the harder NPD Benchmark (up to 4 billion triples) SQL that is a
  union of many sub-queries can let Stardog win ⟨§4.2.4⟩.
- Ontop is the core of the Optique Platform (EU Optique project) and is deployed in
  industrial use cases at Statoil (the EPDS database of 1500+ tables) and Siemens Energy
  (~100 TB of timestamped sensor data), where in the streaming Siemens scenario Ontop is
  used only for query reformulation while execution is delegated elsewhere ⟨§5⟩.
- In the related-systems comparison, the common OBDA strategy is query rewriting — favoring
  OWL 2 QL, which forbids recursion and property chains to guarantee rewritability —
  contrasted with triplestores' forward-chaining materialization, and Ultrawrap is noted
  to use an analogue of T-mappings called "saturated mappings" ⟨§6⟩.

## Concepts & entities covered
Concepts: [[ontology-based-data-access]] · [[virtual-knowledge-graph]] · [[query-rewriting]] · [[query-unfolding]] · [[rdb-to-rdf-mapping]]
Entities: [[ontop]] · [[t-mappings]] · [[tree-witness-rewriting]] · [[owl2-ql]] · [[dl-lite]]
