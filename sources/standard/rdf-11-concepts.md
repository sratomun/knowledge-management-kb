---
title: "RDF 1.1 Concepts and Abstract Syntax"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["RDF 1.1 Concepts", "RDF Concepts"]
publisher: W3C
url: https://www.w3.org/TR/rdf11-concepts/
version: "1.1"
published: 2014-02
effective_from: 2014-02-25
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-09
---

# RDF 1.1 Concepts and Abstract Syntax

## Scope & purpose

W3C Recommendation (25 February 2014) that defines the abstract syntax — a data model — serving as the central specification of the RDF 1.1 document suite. It links all RDF-based languages and specifications (model-theoretic semantics, serialization syntaxes such as Turtle and JSON-LD, the SPARQL query language, and the RDF Schema vocabulary). It introduces the two key data structures (RDF graphs and the RDF datasets that are new in 1.1), core terminology, datatyping, and the handling of fragment identifiers in IRIs. The document is descriptive of the data model; implementations conform to other specs that normatively reference terms defined here, not to this document directly.

## Structure

- §1 Introduction (non-normative): graph-based data model, resources & statements, referent of an IRI, RDF vocabularies & namespace IRIs, change over time, working with multiple graphs, equivalence/entailment/inconsistency, RDF documents & syntaxes
- §2 Conformance
- §3 RDF Graphs — §3.1 Triples, §3.2 IRIs, §3.3 Literals, §3.4 Blank Nodes, §3.5 Replacing Blank Nodes with IRIs, §3.6 Graph Comparison
- §4 RDF Datasets — §4.1 Dataset Comparison, §4.2 Content Negotiation
- §5 Datatypes — §5.1 XML Schema Built-in Datatypes, §5.2 rdf:HTML, §5.3 rdf:XMLLiteral, §5.4 Datatype IRIs
- §6 Fragment Identifiers
- §7 Generalized RDF Triples, Graphs, and Datasets
- §8 Acknowledgments; Appendix A Changes 1.0→1.1; Appendix B References

## Key points

- An RDF graph is a set of RDF triples; the core structure of the abstract syntax is a set of triples, each consisting of a subject, a predicate, and an object ⟨§1.1, §3, §3.1⟩.
- An RDF triple's subject is an IRI or a blank node, its predicate is an IRI, and its object is an IRI, a literal, or a blank node ⟨§3.1⟩.
- There can be three kinds of nodes in an RDF graph: IRIs, literals, and blank nodes; collectively these are known as RDF terms and are distinct and distinguishable ⟨§1.1, §3.1⟩.
- An IRI within an RDF graph is a Unicode string conforming to RFC 3987 syntax; IRIs in the abstract syntax MUST be absolute and MAY contain a fragment identifier ⟨§3.2⟩.
- Two IRIs are equal if and only if they are equivalent under Simple String Comparison per RFC 3987 §5.1; further normalization MUST NOT be performed when comparing IRIs for equality ⟨§3.2⟩.
- By design IRIs have global scope, so two different appearances of an IRI denote the same resource; an IRI once minted SHOULD never change its intended referent ⟨§1.3, §1.5⟩.
- A literal consists of a lexical form (a Unicode string, which SHOULD be in Normal Form C), a datatype IRI, and — if and only if the datatype IRI is rdf:langString — a non-empty, well-formed language tag per BCP47 ⟨§3.3⟩.
- Simple literals (lexical form only) are syntactic sugar for literals with datatype IRI xsd:string; language-tagged strings always carry datatype IRI rdf:langString ⟨§3.3⟩.
- Implementations MUST accept ill-typed literals and produce RDF graphs from them, and MAY produce warnings; an ill-typed literal is a semantic inconsistency but is not syntactically ill-formed ⟨§3.3⟩.
- Two literals are term-equal if and only if their lexical forms, datatype IRIs, and language tags (if any) compare equal character by character; two literals can share a value without being term-equal (e.g. "1"^^xsd:integer vs "01"^^xsd:integer) ⟨§3.3⟩.
- Blank nodes are disjoint from IRIs and literals; RDF makes no reference to their internal structure, and blank node identifiers are local to a concrete syntax or store, not part of the abstract syntax ⟨§3.4⟩.
- Systems replacing blank nodes with IRIs SHOULD mint a new globally unique Skolem IRI per blank node, and systems wanting them recognizable externally SHOULD use a well-known IRI whose path starts with /.well-known/genid/ ⟨§3.5⟩.
- Two RDF graphs are isomorphic if there is a bijection mapping blank nodes to blank nodes and fixing all literals and IRIs such that triples correspond ⟨§3.6⟩.
- An RDF dataset comprises exactly one default graph (unnamed, possibly empty) and zero or more named graphs, each a pair of a graph name (an IRI or blank node, unique within the dataset) and an RDF graph; blank nodes can be shared between graphs ⟨§4⟩.
- The datatype abstraction is compatible with XML Schema; a datatype consists of a lexical space, a value space, and a lexical-to-value mapping, denoted by one or more IRIs; recognized datatype IRIs have fixed referents ⟨§5, §5.4⟩. RDF processors are not required to recognize datatype IRIs, and SHOULD NOT reject RDF using unrecognized ones ⟨§5.4⟩.
- The RDF data model is atemporal — RDF graphs are static snapshots; an RDF graph is the conjunction (logical AND) of its triples, and graph A entails graph B if every arrangement of the world making A true also makes B true ⟨§1.5, §1.7⟩.
- Generalized RDF triples/graphs/datasets (non-normative) loosen the rules to allow IRIs, blank nodes, and literals in any position; no RDF tool is required to accept, process, or produce anything beyond standard RDF ⟨§7⟩.

## Concepts & entities covered

Concepts: [[rdf-data-model]] · [[iri-identity]] · [[literal-datatyping]] · [[blank-node]] · [[rdf-dataset]] · [[entailment-equivalence]] · [[rdf-vocabulary-namespace]] · [[skolemization]] · [[linked-data]] · [[linked-data-serialization]]
Entities: [[rdf-iri]] · [[rdf-literal]] · [[rdf-blank-node]] · [[rdf-triple]] · [[rdf-graph]] · [[rdf-dataset-term]] · [[rdf-named-graph]] · [[rdf-default-graph]] · [[rdf-langstring]] · [[rdf-html]] · [[rdf-xmlliteral]] · [[rdf-skolem-iri]] · [[rdf-datatype-iri]] · [[rdf-source]] · [[rdf-turtle]] · [[rdf-schema-11]] · [[rdf-semantics]] · [[rdf-trig]] · [[sparql-11-query]]
