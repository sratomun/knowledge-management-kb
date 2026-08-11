---
title: "RDF graph"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# RDF graph

## What it is
An RDF graph is the core data structure of the RDF abstract syntax: a set of RDF triples, visualizable as a node-and-directed-arc diagram.

## Key facts
- An RDF graph is a set of RDF triples ⟨§3⟩.
- There can be three kinds of nodes in an RDF graph: IRIs, literals, and blank nodes ⟨§1.1⟩.
- The set of nodes of an RDF graph is the set of subjects and objects of triples in the graph; a predicate IRI may also occur as a node in the same graph ⟨§3.1⟩.
- Two RDF graphs G and G' are isomorphic if there is a bijection between their sets of nodes that maps blank nodes to blank nodes, fixes all literals and IRIs, and preserves the triples ⟨§3.6⟩.
- The RDF data model is atemporal: RDF graphs are static snapshots of information ⟨§1.5⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-triple]], [[rdf-dataset]]

## See also
[[rdf-source]]
