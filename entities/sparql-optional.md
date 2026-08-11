---
title: "SPARQL OPTIONAL"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[graph-pattern-matching]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL OPTIONAL

## What it is
OPTIONAL is the SPARQL construct for optional pattern matching: it adds bindings to a solution where the optional graph pattern matches, but does not discard the solution when it does not.

## Key facts
- "Optional matching provides this facility: if the optional part does not match, it creates no bindings but does not eliminate the solution." ⟨§6⟩
- "In an optional match, either the optional graph pattern matches a graph, thereby defining and adding bindings to one or more solutions, or it leaves a solution unchanged without adding any additional bindings." ⟨§6.1⟩
- "The OPTIONAL keyword is left-associative." ⟨§6.1⟩
- A graph pattern may have zero or more optional graph patterns, and any part of a query pattern may have an optional part ⟨§6.3⟩

## Relations
- Realizes: [[graph-pattern-matching]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-bgp]] · [[sparql-filter]] · [[sparql-union]]

## See also
[[graph-pattern-matching]] · [[org-w3c]]
