---
title: "Named Graph Assignment"
type: concept
tags: [semantic-web]
related: ["[[rdb-to-rdf-mapping]]", "[[term-map]]", "[[rdf-dataset]]"]
updated: 2026-08-09
---

# Named Graph Assignment

## What it is
The part of a mapping that decides into which graph of the output RDF dataset each generated triple is placed. Rather than emitting all triples into a single default graph, a mapping can attach graph maps to subjects or predicate-object rules to route triples into named graphs, with a designated term marking the default graph.

## How sources treat it
- **[[r2rml]]** _(standard · normative)_ — any subject map or predicate-object map MAY have graph maps (rr:graphMap or the shortcut rr:graph); the special IRI rr:defaultGraph targets the default graph, and by default all triples are placed in the default graph ⟨§9⟩
- **[[r2rml]]** _(standard · normative)_ — the constant shortcut property rr:graph MUST be treated exactly as if the corresponding expanded rr:graphMap [ rr:constant … ] triple were present instead ⟨§7.1⟩
- **[[rml]]** _(standard · normative)_ — named graphs are supported via rr:graphMap / rr:graph; if a graph map generates rr:defaultGraph, the target is the default graph, and blank nodes are scoped to a single RDF graph and can never be shared across graphs ⟨§8, §8.2⟩

## Where sources differ
Both specifications reuse the same graph-map vocabulary (rr:graphMap / rr:graph / rr:defaultGraph) with the default graph as the fallback target ⟨r2rml §9; rml §8⟩. RML additionally states explicitly that blank nodes are scoped to a single RDF graph and can never be shared across graphs ⟨rml §8.2⟩; R2RML documents blank-node scope for named graphs within its own named-graphs section ⟨r2rml §9.1⟩.

## See also
[[rdb-to-rdf-mapping]] · [[term-map]]
