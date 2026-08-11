---
title: "RDF dataset"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[blank-node]]", "[[iri-identity]]", "[[named-graph-assignment]]"]
updated: 2026-08-09
---

# RDF dataset

## What it is

An RDF dataset is a container that groups several RDF graphs together: exactly one default (unnamed) graph plus any number of named graphs, each paired with a name. Datasets are what let a single RDF document carry more than one graph — for example separating statements by provenance, source, or context — while still forming one interchangeable unit. The structure was introduced in RDF 1.1 and is the unit that serialization formats such as JSON-LD produce and consume.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — An RDF dataset comprises exactly one default graph (unnamed, possibly empty) and zero or more named graphs, each a pair of a graph name (an IRI or blank node, unique within the dataset) and an RDF graph; blank nodes can be shared between graphs ⟨§4⟩.
- **[[json-ld-11]]** _(standard · normative)_ — A JSON-LD document serializes an RDF Dataset, a collection of graphs comprising exactly one default graph and zero or more named graphs; the default graph does not have a name and MAY be empty ⟨§8⟩.
- **[[json-ld-11]]** _(standard · normative)_ — Each named graph is a pair of a graph name (IRI or blank node identifier) and a graph, and whenever practical the graph name SHOULD be an IRI ⟨§8⟩.

## Where sources differ

The two sources agree on the core structure — one default graph plus zero or more named graphs. They diverge on how graph names should be chosen: rdf-11-concepts allows a graph name to be an IRI or a blank node and notes that blank nodes can be shared between graphs ⟨§4⟩, whereas json-ld-11 permits an IRI or blank node identifier but adds the recommendation that, whenever practical, the graph name SHOULD be an IRI ⟨§8⟩. The KB records both postures without preferring either.

## See also

[[rdf-data-model]] · [[blank-node]] · [[iri-identity]] · [[named-graph-assignment]]
