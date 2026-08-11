---
title: "Named graph"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-dataset]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Named graph

## What it is
A named graph is a component of an RDF dataset: an RDF graph paired with a graph name (an IRI or blank node). All but one of the graphs in a dataset are named.

## Key facts
- Each named graph is a pair consisting of an IRI or a blank node (the graph name), and an RDF graph ⟨§4⟩.
- Graph names are unique within an RDF dataset ⟨§4⟩.
- Despite the use of the word "name", the graph name is not required to denote the graph; it is merely syntactically paired with the graph, and RDF places no formal restriction on what it denotes ⟨§4⟩.
- SPARQL 1.1 Query Language only allows RDF graphs to be identified using an IRI; Skolemizing blank nodes used as graph names can be used to overcome the resulting interoperability problems ⟨§4⟩.

## Relations
- Realizes: [[rdf-dataset]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-dataset]], [[rdf-default-graph]]

## See also
[[rdf-skolem-iri]]
