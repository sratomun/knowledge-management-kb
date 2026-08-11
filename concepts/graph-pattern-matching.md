---
title: "Graph Pattern Matching"
type: concept
tags: [semantic-web]
related: ["[[sparql-query-forms]]", "[[property-paths]]", "[[rdf-dataset]]"]
updated: 2026-08-10
---

# Graph Pattern Matching

## What it is
The core evaluation model of SPARQL: a query describes a pattern of triples, some positions of which are variables, and answers are the ways RDF terms can be substituted for those variables so the pattern matches a subgraph of the queried data. Larger queries are built by combining basic triple patterns into groups and then adding required, optional, alternative, and negated sub-patterns, with filters restricting which candidate matches survive.

## How sources treat it
- **[[sparql-11-query]]** _(standard · normative)_ — SPARQL is based around graph pattern matching, and more complex graph patterns are formed by combining basic graph patterns, group graph patterns, optional graph patterns, alternative graph patterns, and patterns on named graphs ⟨§5⟩
- **[[sparql-11-query]]** _(standard · normative)_ — a basic graph pattern is a set of triple patterns where each of the subject, predicate and object may be a variable; it matches a subgraph when RDF terms may be substituted for the variables and the result is RDF graph equivalent to the subgraph ⟨§2, §5.1⟩
- **[[sparql-11-query]]** _(standard · normative)_ — blank node labels are scoped to a basic graph pattern: "A label can be used in only a single basic graph pattern in any query." ⟨§5.1.1⟩
- **[[sparql-11-query]]** _(standard · normative)_ — a group graph pattern is delimited with braces `{}`, and a FILTER constraint "is a restriction on solutions over the whole group in which the filter appears." ⟨§5.2.2⟩
- **[[sparql-11-query]]** _(standard · normative)_ — optional matching adds bindings where the optional graph pattern matches, but if the optional part does not match "it creates no bindings but does not eliminate the solution." ⟨§6.1⟩
- **[[sparql-11-query]]** _(standard · normative)_ — UNION combines graph patterns so that one of several alternatives may match, and if more than one alternative matches all the possible pattern solutions are found ⟨§7⟩
- **[[sparql-11-query]]** _(standard · normative)_ — SPARQL incorporates two styles of negation — FILTER NOT EXISTS / EXISTS and MINUS — and in some cases they can produce different answers ⟨§8, §8.3⟩
- **[[sparql-11-query]]** _(standard · normative)_ — the RDF Dataset comprises one default graph and zero or more named graphs; FROM and FROM NAMED specify the dataset for a query, and GRAPH scopes matching to named graphs ⟨§13⟩
- **[[sparql-11-query]]** _(standard · normative)_ — §18 gives the formal SPARQL algebra and evaluation semantics as a translation of graph patterns to algebra operators, defining how matches are computed ⟨§18⟩

## Where sources differ
Only one source in this KB, the normative SPARQL 1.1 Query Language Recommendation, treats graph pattern matching directly, so no cross-source disagreement is recorded. Internally the specification is careful to distinguish the informative introductions to pattern matching (§§2-3) from the normative definitions in §5 and the formal algebra in §18, and it flags that the two negation styles can diverge in their answers ⟨sparql-11-query §5, §8.3, §18⟩.

## See also
[[sparql-query-forms]] · [[property-paths]] · [[rdf-dataset]]
