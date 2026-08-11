---
title: "Blank node"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[skolemization]]", "[[iri-identity]]", "[[entailment-equivalence]]"]
updated: 2026-08-09
---

# Blank node

## What it is

A blank node is a node in an RDF graph that stands for a resource without naming it with an IRI or a literal — an existential "something" whose identity matters only within the graph. Blank nodes let RDF assert that a resource exists and has certain properties without committing to a global name for it. Their identifiers are an artifact of a particular serialization or store rather than part of the abstract data, which shapes how graphs are compared and how blank nodes can later be replaced with stable names.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — Blank nodes are one of the three kinds of node in an RDF graph, alongside IRIs and literals, and are collectively RDF terms that are distinct and distinguishable ⟨§1.1, §3.1⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — A triple's subject is an IRI or a blank node, and its object is an IRI, a literal, or a blank node — so blank nodes may occupy subject and object positions ⟨§3.1⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Blank nodes are disjoint from IRIs and literals; RDF makes no reference to their internal structure, and blank node identifiers are local to a concrete syntax or store, not part of the abstract syntax ⟨§3.4⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two RDF graphs are isomorphic if there is a bijection mapping blank nodes to blank nodes and fixing all literals and IRIs such that triples correspond ⟨§3.6⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Systems replacing blank nodes with IRIs SHOULD mint a new globally unique Skolem IRI per blank node ⟨§3.5⟩.

## Where sources differ

This concept is covered by a single source, rdf-11-concepts, so there is no divergence to report here.

## See also

[[rdf-data-model]] · [[skolemization]] · [[iri-identity]] · [[entailment-equivalence]]
