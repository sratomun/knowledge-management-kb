---
title: "RDF source"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# RDF source

## What it is
An RDF source is a persistent yet mutable container of RDF graphs whose state can change over time. It provides the mutable counterpart to the atemporal RDF graph.

## Key facts
- An RDF source is a persistent yet mutable source or container of RDF graphs; it is a resource that may be said to have a state that can change over time, and a snapshot of that state can be expressed as an RDF graph ⟨§1.5⟩.
- Like all resources, RDF sources may be named with IRIs and therefore described in other RDF graphs ⟨§1.5⟩.
- Some RDF sources may be immutable snapshots of another RDF source, archiving its state at some point in time ⟨§1.5⟩.
- Any web document that has an RDF-bearing representation may be considered an RDF source ⟨§1.5⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-graph]]

## See also
[[rdf-dataset]]
