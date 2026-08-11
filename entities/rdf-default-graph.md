---
title: "Default graph"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-dataset]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Default graph

## What it is
The default graph is the single unnamed RDF graph in an RDF dataset. Every RDF dataset has exactly one.

## Key facts
- An RDF dataset comprises exactly one default graph, being an RDF graph; the default graph does not have a name and may be empty ⟨§4⟩.
- If an RDF dataset is returned and the consumer is expecting an RDF graph, the consumer is expected to use the RDF dataset's default graph ⟨§4.2⟩.

## Relations
- Realizes: [[rdf-dataset]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-dataset]], [[rdf-named-graph]]

## See also
[[rdf-graph]]
