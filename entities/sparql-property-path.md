---
title: "SPARQL Property Path"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[property-paths]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL Property Path

## What it is
A property path is a SPARQL construct expressing a route through an RDF graph between two graph nodes, generalizing a triple pattern's predicate to a path expression.

## Key facts
- "A property path is a possible route through a graph between two graph nodes. A trivial case is a property path of length exactly 1, which is a triple pattern." ⟨§9⟩
- "Variables can not be used as part of the path itself, only the ends." ⟨§9⟩
- "Property paths allow for more concise expressions for some SPARQL basic graph patterns and they also add the ability to match connectivity of two resources by an arbitrary length path." ⟨§9⟩
- Path syntax includes InversePath (^elt), SequencePath (elt1/elt2), AlternativePath (elt1|elt2), and the arbitrary-length forms ZeroOrMorePath (elt*), OneOrMorePath (elt+) and ZeroOrOnePath (elt?) ⟨§9.1⟩

## Relations
- Realizes: [[property-paths]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-bgp]]

## See also
[[property-paths]] · [[graph-pattern-matching]] · [[org-w3c]]
