---
title: "SPARQL FILTER"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[graph-pattern-matching]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL FILTER

## What it is
FILTER is the SPARQL constraint keyword that restricts a graph pattern's solutions to those for which a boolean-valued expression holds.

## Key facts
- "SPARQL FILTERs restrict solutions to those for which the filter expression evaluates to TRUE." ⟨§3⟩
- "A constraint, expressed by the keyword FILTER, is a restriction on solutions over the whole group in which the filter appears." ⟨§5.2.2⟩
- "FILTERs eliminate any solutions that, when substituted into the expression, either result in an effective boolean value of false or produce an error." These errors "have no effect outside of FILTER evaluation." ⟨§17.2⟩
- The FILTER scope rules apply to the whole group in which the filter appears, including when used with EXISTS and NOT EXISTS ⟨§8.1⟩

## Relations
- Realizes: [[graph-pattern-matching]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-bgp]] · [[sparql-optional]] · [[sparql-union]]

## See also
[[graph-pattern-matching]] · [[org-w3c]]
