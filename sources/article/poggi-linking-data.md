---
title: "Linking Data to Ontologies"
type: source
kind: article
authority: informational
subtype: academic-paper
aliases: ["Poggi 2008", "Linking Data to Ontologies"]
publisher: "Journal on Data Semantics"
url: https://www.inf.unibz.it/~calvanese/papers-html/JODS-2008.html
version: "JoDS X, 2008"
published: 2008-01
effective_from: 2008-01
effective_to: ongoing
status: current
tags: [obda, semantic-web]
updated: 2026-08-10
---

# Linking Data to Ontologies

## Scope & purpose

This is the foundational paper on ontology-based data access (OBDA): superimposing a
conceptual (ontology) layer over pre-existing relational data sources so clients query a
high-level conceptual view that abstracts away from how data is physically stored.
Authored by Antonella Poggi, Domenico Lembo, Diego Calvanese, Giuseppe De Giacomo,
Maurizio Lenzerini, and Riccardo Rosati, it appeared in the Journal on Data Semantics X
(LNCS 4900, pp. 133-173, 2008). The paper contributes three ingredients: (1) a new
Description Logic, DL-LiteA, tailored to reason with large amounts of instances while
delegating data-dependent reasoning to a relational DBMS; (2) a novel mapping language
that solves the impedance mismatch between data values at the sources and objects at the
conceptual level; and (3) a sound and complete query answering method combining
reasoning over the ontology with mechanisms for taking mappings into account and
efficiently accessing the sources.

## Structure

- §1 Introduction — motivation for OBDA; the five issues (ontology language expressivity
  vs. complexity, large data volumes / relational technology, mapping, impedance
  mismatch, query answering); survey of prior mapping/alignment proposals (C-OWL, DDLs,
  MAFRA, OMWG).
- §2 The Description Logic DL-LiteA — expressions (§2.1), ontologies TBox/ABox (§2.2),
  conjunctive queries and certain answers (§2.3), reasoning by reduction to SQL over
  db(A), PerfectRef, Violates (§2.4).
- §3 Linking Relational Data to DL-LiteA Ontologies — the impedance mismatch; object
  terms built from data values via function symbols; mapping assertions; the ontology
  with mappings triple ⟨T, M, DB⟩; typing vs. data-to-object mappings.
- §4 Overview of the Reasoning Method — splitting mappings (§4.1), virtual ABox (§4.2),
  bottom-up approach (§4.3), top-down approach of reformulation/unfolding/evaluation
  (§4.4).
- §5 Dealing with Mappings — the unfolding step via logic programming and partial
  evaluation; UnfoldDB.
- §6 Reasoning over DL-LiteA Ontologies with Mappings — satisfiability algorithm Sat
  (§6.1), query answering algorithm Answer (§6.2), computational complexity (§6.3).
- §7 Conclusions — LogSpace data complexity, reduction to SQL, QuOnto implementation.

## Key points

- Ontology-based data access superimposes a conceptual (ontology) layer over pre-existing
  data sources, giving clients a conceptual view that is the unique access point and
  abstracts away from how data is maintained; the sources exist autonomously and
  independently of the ontology ⟨§1⟩.
- An ontology with mappings is characterized as a triple Om = ⟨T, M, DB⟩: a DL-LiteA TBox
  T, a set of mapping assertions M, and a relational database DB ⟨§3⟩.
- The paper introduces DL-LiteA, a new logic of the DL-Lite family that takes seriously
  the distinction between objects and values, adding attributes (binary relations between
  objects and values) alongside concepts, roles, and value-domains ⟨§2⟩.
- DL-LiteA merges features of DL-LiteF and DL-LiteR under restrictions (identifying
  properties must be primitive) so that reasoning stays in LogSpace with respect to data
  complexity, whereas unrestricted merging loses this property ⟨§1⟩.
- Ontology satisfiability, instance checking, and conjunctive query answering in DL-LiteA
  can all be done in LogSpace in data complexity, and after a data-independent
  preprocessing phase the data-dependent part is delegated to the relational DBMS ⟨§2⟩.
- The impedance mismatch problem is that sources store data values whereas instances of
  concepts are objects denoted by object identifiers not to be confused with data values;
  the mapping language must address it ⟨§1⟩⟨§3⟩.
- To solve the impedance mismatch, DL-LiteA builds object identifiers as logic terms of
  the form f(d1,...,dn) — object-generating function symbols applied to data values drawn
  from the sources — an idea borrowed from object invention in deductive object-oriented
  databases ⟨§3⟩.
- Mappings are partitioned into typing assertions (Φ ~> Ti, assigning source values to
  DL-LiteA/RDF data types) and data-to-object assertions (Φ ~> Ψ, where Φ is an arbitrary
  SQL query over DB and Ψ a conjunctive query over the ontology possibly involving
  variable terms) ⟨§3⟩.
- Mapping assertions are read as material implications: the closed-world semantics of DB
  is captured by evaluating Φ as a standard relational query, while the open-world
  semantics of the ontology allows additional facts beyond those the mapping supplies
  ⟨§3⟩.
- A conjunctive query is answered by computing certain answers — tuples that hold in every
  model of the ontology (with mappings) — which is the correct semantics under incomplete
  information ⟨§2⟩⟨§3⟩.
- Query answering follows a top-down method of three steps: reformulation (rewriting),
  unfolding, and evaluation, which keeps the ABox virtual rather than materializing it
  bottom-up ⟨§4⟩.
- The reformulation step, PerfectRef, rewrites a UCQ against the TBox into a new UCQ whose
  evaluation over the data alone yields the certain answers, compiling all relevant TBox
  knowledge into the query — a form of first-order/FO rewritability ⟨§2⟩⟨§4⟩.
- The unfolding step (UnfoldDB) translates the reformulated query into an SQL query over
  the source relations using logic-programming partial-evaluation techniques, thereby
  completely getting rid of the mappings at evaluation time ⟨§5⟩.
- The evaluation step simply delegates the resulting SQL query to the DBMS; the overall
  Answer and Sat algorithms are proved sound, complete, and terminating ⟨§6⟩.
- Both satisfiability checking and query answering run in LogSpace in the size of the data
  (data complexity), polynomial in the size of the mappings and TBox, and exponential in
  the size of the query ⟨§6⟩.
- The mapping and impedance-mismatch ideas are argued to be of general value beyond
  DL-LiteA, and the solution is implemented on top of the QuOnto reasoner ⟨§7⟩.

## Concepts & entities covered
Concepts: [[ontology-based-data-access]] · [[virtual-knowledge-graph]] · [[rdb-to-rdf-mapping]] · [[query-rewriting]] · [[query-unfolding]] · [[first-order-rewritability]] · [[impedance-mismatch]] · [[object-generating-terms]] · [[certain-answer-semantics]]
Entities: [[dl-lite]] · [[dl-lite-a]] · [[quonto]]
