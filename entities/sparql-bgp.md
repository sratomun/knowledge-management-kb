---
title: "SPARQL Basic Graph Pattern"
type: entity
subtype: specification-construct
aliases: ["BGP"]
tags: [semantic-web]
concepts: ["[[graph-pattern-matching]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL Basic Graph Pattern

## What it is
A basic graph pattern (BGP) is a set of triple patterns — like RDF triples but with variables permitted in any position — that forms the fundamental building block of SPARQL graph pattern matching.

## Key facts
- "A basic graph pattern matches a subgraph of the RDF data when RDF terms from that subgraph may be substituted for the variables and the result is RDF graph equivalent to the subgraph." ⟨§2⟩
- "A sequence of triple patterns, with optional filters, comprises a single basic graph pattern. Any other graph pattern terminates a basic graph pattern." ⟨§5.1⟩
- In a basic graph pattern match "all the variables used in the query pattern must be bound in every solution." ⟨§2.2⟩
- For blank node labels of the form _:abc, "A label can be used in only a single basic graph pattern in any query." ⟨§5.1.1⟩
- BGP matching is defined using subgraph matching for simple entailment and can be extended to other entailment regimes under stated conditions ⟨§5.1.2⟩

## Relations
- Realizes: [[graph-pattern-matching]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-filter]] · [[sparql-optional]] · [[sparql-union]] · [[sparql-property-path]]

## See also
[[graph-pattern-matching]] · [[org-w3c]]
