---
title: "rr:GraphMap"
type: entity
subtype: vocabulary-term
aliases: ["R2RML graph map"]
tags: [obda]
concepts: ["[[named-graph-assignment]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:GraphMap

## What it is
The R2RML term map that determines the target graph(s) into which generated triples are placed. It may be attached to a subject map or a predicate-object map.

## Key facts
- "Graph maps are themselves term maps"; the set of target graphs is determined by any graph maps associated with the subject map or predicate-object map ⟨§9⟩
- Any subject map or predicate-object map MAY have one or more associated graph maps, specified via rr:graphMap or the constant shortcut property rr:graph ⟨§9⟩
- If a graph map generates the special IRI rr:defaultGraph, then the target graph is the default graph of the output dataset ⟨§9⟩

## Relations
- Realizes: [[named-graph-assignment]]
- Defined in: [[r2rml]]
- Related: [[r2rml-defaultgraph]], [[r2rml-subjectmap]], [[r2rml-predicateobjectmap]]

## See also
[[r2rml-termmap]] · [[org-w3c]]
