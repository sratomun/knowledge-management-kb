---
title: "Blank node (RDF term)"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[blank-node]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Blank node (RDF term)

## What it is
A blank node is one of the three kinds of RDF term. Unlike IRIs and literals it does not identify a specific resource; it asserts the existence of something with the given relationships without naming it.

## Key facts
- Blank nodes are disjoint from IRIs and literals; otherwise, the set of possible blank nodes is arbitrary, and RDF makes no reference to any internal structure of blank nodes ⟨§3.4⟩.
- Statements involving blank nodes say that something with the given relationships exists, without explicitly naming it ⟨§1.2⟩.
- Blank node identifiers are local identifiers used in some concrete RDF syntaxes or store implementations; they are always locally scoped and are not part of the RDF abstract syntax ⟨§3.4⟩.
- Blank nodes can be shared between graphs in an RDF dataset ⟨§4⟩.

## Relations
- Realizes: [[blank-node]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-skolem-iri]]

## See also
[[rdf-triple]] · [[rdf-iri]]
