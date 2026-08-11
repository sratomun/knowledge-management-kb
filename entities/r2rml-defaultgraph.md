---
title: "rr:defaultGraph"
type: entity
subtype: vocabulary-term
aliases: ["R2RML default graph term"]
tags: [obda]
concepts: ["[[named-graph-assignment]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:defaultGraph

## What it is
The special R2RML IRI that, when produced by a graph map, directs generated triples into the default graph of the output dataset rather than a named graph.

## Key facts
- If a graph map generates the special IRI rr:defaultGraph, then the target graph is the default graph of the output dataset ⟨§9⟩
- By default, all RDF triples are in the default graph of the output dataset; a triples map can contain graph maps that place some or all triples into named graphs instead ⟨§2⟩
- In the triple-generation algorithm, if the relevant graph maps are empty the target graph is rr:defaultGraph; each target-graph IRI not equal to rr:defaultGraph adds the triple to a named graph of that name ⟨§11.1⟩

## Relations
- Realizes: [[named-graph-assignment]]
- Defined in: [[r2rml]]
- Related: [[r2rml-graphmap]]

## See also
[[r2rml-termtype]] · [[org-w3c]]
