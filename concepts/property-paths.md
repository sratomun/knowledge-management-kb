---
title: "Property Paths"
type: concept
tags: [semantic-web]
related: ["[[graph-pattern-matching]]", "[[sparql-query-forms]]", "[[constraint-validation]]"]
updated: 2026-08-10
---

# Property Paths

## What it is
A route through an RDF graph between two nodes, written as a path expression over predicates rather than a single triple pattern. Paths let a query follow a predicate, its inverse, an alternative of several predicates, a sequence, or a repeated predicate of arbitrary length, giving a compact way to express connectivity that would otherwise require many triple patterns or would be impossible to bound in advance.

## How sources treat it
- **[[sparql-11-query]]** _(standard · normative)_ — property paths add a compact representation of queries and the ability to match arbitrary-length paths in the graph ⟨§9⟩
- **[[sparql-11-query]]** _(standard · normative)_ — §9 defines path syntax, gives examples, states equivalent (path-free) patterns for the simpler cases, and specifies arbitrary-length matching ⟨§9⟩
- **[[shacl]]** _(standard · normative)_ — SHACL property paths cover a subset of SPARQL property paths: predicate, inverse (sh:inversePath), sequence (SHACL list), alternative (sh:alternativePath), and sh:zeroOrMorePath / sh:oneOrMorePath / sh:zeroOrOnePath ⟨§2.3.1⟩
- **[[shacl]]** _(standard · normative)_ — a SHACL property shape is the subject of a triple with sh:path and applies to the nodes reached from the focus node by that path ⟨§2.3⟩

## Where sources differ
Both sources describe property paths as expressions over predicates including inverse, sequence, alternative and repeated (zero-or-more / one-or-more / zero-or-one) forms. They differ in role and coverage. SPARQL 1.1 defines property paths as a full query-language feature, including arbitrary-length matching and equivalent path-free patterns for the bounded cases ⟨sparql-11-query §9⟩. SHACL reuses only a subset of SPARQL property paths, recording them in RDF (via sh:inversePath, sh:alternativePath, SHACL lists, and the sh:zeroOrMorePath family) to say where in the graph a property shape's constraints apply, rather than to return query solutions ⟨shacl §2.3.1, §2.3⟩.

## See also
[[graph-pattern-matching]] · [[sparql-query-forms]] · [[constraint-validation]]
