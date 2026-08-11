---
title: "OWL 2 Web Ontology Language Document Overview"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["OWL 2 Overview"]
publisher: W3C
url: https://www.w3.org/TR/owl2-overview/
version: "2 (2012-12-11)"
published: 2012-12
effective_from: 2012-12
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# OWL 2 Web Ontology Language Document Overview

## Scope & purpose

W3C Recommendation (11 December 2012, Second Edition) that provides a non-normative, high-level overview of the OWL 2 Web Ontology Language and serves as a roadmap to the other OWL 2 documents. OWL 2 (informally "OWL 2") is an ontology language for the Semantic Web with formally defined meaning; OWL 2 ontologies provide classes, properties, individuals, and data values, are stored as Semantic Web documents, can be used alongside RDF information, and are primarily exchanged as RDF documents. The document describes the syntaxes for OWL 2, the two kinds of semantics (Direct and RDF-Based), the three available profiles (sub-languages EL, QL, RL), and the relationship between OWL 1 and OWL 2. It is positioned as the starting point and primary reference point for OWL 2. Although endorsed as a W3C Recommendation, the overview content itself is explicitly non-normative/informative; the language is normatively defined by the five core specification documents it points to.

## Structure

- §1 Introduction — purpose as high-level overview and roadmap; ontologies as formalized vocabularies of terms; OWL 2 as an extension/revision of OWL 1 (2004), developed by the W3C OWL Working Group
- §2 Overview — Figure 1 (the structure of OWL 2): ontology in the center, concrete syntaxes at the top, semantic specifications at the bottom
  - §2.1 Ontologies — conceptual structure (Structural Specification, UML, functional-style syntax); dual view as abstract structure or RDF graph (Mapping to RDF Graphs)
  - §2.2 Syntaxes — RDF/XML (mandatory) plus Turtle, OWL/XML, Manchester, functional-style; syntax table with status and purpose
  - §2.3 Semantics — Direct Semantics (SROIQ / OWL 2 DL) and RDF-Based Semantics (OWL 2 Full); correspondence theorem
  - §2.4 Profiles — OWL 2 EL, QL, RL as syntactic subsets, each more restrictive than OWL DL
- §3 Relationship to OWL 1 — backwards compatibility; new features (keys, property chains, richer datatypes, qualified cardinality restrictions, etc.); new profiles and Manchester syntax
- §4 Documentation Roadmap — five core specification documents, three additional specification documents, and the user documents (Primer, New Features and Rationale, Quick Reference Guide); numbered parts table (Parts 1–13)
- §5 Appendix: Change Log (Informative)
- §6 Acknowledgements
- §7 References

## Key points

- The OWL 2 Web Ontology Language, informally OWL 2, is an ontology language for the Semantic Web with formally defined meaning; OWL 2 ontologies provide classes, properties, individuals, and data values, are stored as Semantic Web documents, can be used along with information written in RDF, and are themselves primarily exchanged as RDF documents ⟨Abstract⟩.
- An OWL 2 ontology can be understood either as an abstract structure (defined in the Structural Specification using UML) or, equivalently, as an RDF graph; the Mapping to RDF Graphs document defines the mapping between the two views in both directions ⟨§2, §2.1⟩.
- The primary exchange syntax for OWL 2 is RDF/XML; this is indeed the only syntax that must be supported by all OWL 2 tools ⟨§2.2⟩.
- Besides the mandatory RDF/XML, other concrete syntaxes may be used: alternative RDF serializations such as Turtle, an XML serialization (OWL/XML), the more readable Manchester Syntax used in several ontology editing tools, and the functional-style syntax (whose main purpose is specifying the structure of the language) — all optional ⟨§2.2⟩.
- Two semantic specifications assign meaning to OWL 2 ontologies — the Direct Semantics and the RDF-Based Semantics — with a correspondence theorem providing a link between the two; these semantics are used by reasoners and other tools to answer class consistency, subsumption, and instance retrieval queries ⟨§2.3⟩.
- The Direct Semantics assigns meaning directly to ontology structures and is compatible with the model-theoretic semantics of the SROIQ description logic; ontologies satisfying the syntactic conditions required for translation into a SROIQ knowledge base are called OWL 2 DL ontologies ("OWL 2 DL") ⟨§2.3⟩.
- The RDF-Based Semantics assigns meaning directly to RDF graphs (and indirectly to ontology structures via the mapping), is fully compatible with the RDF Semantics, and can be applied to any OWL 2 ontology without restrictions; such graphs interpreted this way are informally called "OWL 2 Full" ⟨§2.3⟩.
- The correspondence theorem (§7.2 of the RDF-Based Semantics document) states, in essence, that given an OWL 2 DL ontology, inferences drawn using the Direct Semantics remain valid when the ontology is mapped into an RDF graph and interpreted using the RDF-Based Semantics ⟨§2.3⟩.
- OWL 2 Profiles are sub-languages (syntactic subsets) of OWL 2 offering advantages in particular application scenarios; three profiles are defined — OWL 2 EL, OWL 2 QL, and OWL 2 RL — each defined as a syntactic restriction of the Structural Specification and each more restrictive than OWL DL, trading expressive power for computational and/or implementational benefits ⟨§2.4⟩.
- OWL 2 EL enables polynomial time algorithms for all the standard reasoning tasks and is particularly suitable where very large ontologies are needed; OWL 2 QL enables conjunctive queries to be answered in LogSpace (more precisely, AC0) using standard relational database technology; OWL 2 RL enables polynomial time reasoning using rule-extended database technologies operating directly on RDF triples ⟨§2.4⟩.
- When using OWL 2 RL a rule-based implementation can operate directly on an arbitrary RDF graph; in this case reasoning will always be sound (only correct answers computed) but may not be complete, though Theorem PR1 of the Profiles document states that for an ontology consistent with the structural definition of OWL 2 RL a suitable rule-based implementation performing ground atomic queries will be both sound and complete ⟨§2.4⟩.
- OWL 2 has a very similar overall structure to OWL 1 and backwards compatibility is, to all intents and purposes, complete: all OWL 1 ontologies remain valid OWL 2 ontologies with identical inferences in all practical cases ⟨§3⟩.
- OWL 2 adds new functionality over OWL 1, including keys, property chains, richer datatypes and data ranges, qualified cardinality restrictions, asymmetric/reflexive/disjoint properties, and enhanced annotation capabilities, plus three new profiles and the Manchester syntax ⟨§3⟩.
- The OWL 2 language is normatively defined by five core specification documents (Structural Specification, Mapping to RDF Graphs, Direct Semantics, RDF-Based Semantics, Conformance) plus three additional specification documents (Profiles, XML Serialization, Manchester Syntax) and several user documents (Primer, New Features and Rationale, Quick Reference Guide) ⟨§4⟩.

## Concepts & entities covered
Concepts: [[description-logic]]
Entities: [[owl2]] · [[owl2-el]] · [[owl2-ql]] · [[owl2-rl]]
