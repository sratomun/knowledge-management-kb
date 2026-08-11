---
title: "RDF dataset (term)"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-dataset]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# RDF dataset (term)

## What it is
An RDF dataset is a collection of RDF graphs — new in RDF 1.1 — that lets multiple graphs be worked with while keeping their contents separate. It comprises one default graph and zero or more named graphs.

## Key facts
- An RDF dataset is a collection of RDF graphs, comprising exactly one default graph (an RDF graph that does not have a name and may be empty) and zero or more named graphs ⟨§4⟩.
- Each named graph is a pair consisting of an IRI or a blank node (the graph name) and an RDF graph; graph names are unique within an RDF dataset ⟨§4⟩.
- Blank nodes can be shared between graphs in an RDF dataset ⟨§4⟩.
- SPARQL 1.1 also defines the concept of an RDF Dataset, but only allows RDF graphs to be identified using an IRI, whereas this specification also allows a blank node ⟨§4⟩.

## Relations
- Realizes: [[rdf-dataset]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-named-graph]], [[rdf-default-graph]], [[rdf-graph]]

## See also
[[sparql-11-query]] · [[rdf-trig]]
