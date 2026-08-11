---
title: "SPARQL Query Forms"
type: concept
tags: [semantic-web]
related: ["[[graph-pattern-matching]]", "[[property-paths]]", "[[rdf-dataset]]"]
updated: 2026-08-10
---

# SPARQL Query Forms

## What it is
The four shapes a SPARQL query can take, each producing a different kind of result once its graph pattern has matched: a table of variable bindings, a new RDF graph, a yes/no answer, or a description of resources. Solution-sequence modifiers (ordering, projection, duplicate removal, slicing) and higher-level features (aggregation, subqueries, inline values) shape the solutions that the chosen form then returns.

## How sources treat it
- **[[sparql-11-query]]** _(standard · normative)_ — the four query forms produce results in different forms: SELECT returns variable bindings; CONSTRUCT returns an RDF graph built from a template; ASK returns a boolean; and DESCRIBE (informative) returns an RDF graph describing the resources found ⟨§16⟩
- **[[sparql-11-query]]** _(standard · normative)_ — the results of SPARQL queries can be result sets or RDF graphs ⟨§1, Scope⟩
- **[[sparql-11-query]]** _(standard · normative)_ — solution sequence modifiers order (ORDER BY), project, remove duplicates (DISTINCT / REDUCED), and slice (OFFSET, LIMIT) the sequence of solutions ⟨§15⟩
- **[[sparql-11-query]]** _(standard · normative)_ — aggregates (COUNT, SUM, MIN, MAX, AVG, SAMPLE, GROUP_CONCAT) apply over groups formed by GROUP BY, with HAVING filtering the resulting groups ⟨§11⟩
- **[[sparql-11-query]]** _(standard · normative)_ — a subquery embeds one SELECT query within the graph pattern of another, allowing results to be computed and then joined ⟨§12⟩
- **[[sparql-11-query]]** _(standard · normative)_ — assignment binds a new variable to the value of an expression via BIND, expressions in the SELECT clause, or expressions in GROUP BY; "The variable introduced by the BIND clause must not have been used in the group graph pattern up to the point of use in BIND." ⟨§10, §10.1⟩
- **[[sparql-11-query]]** _(standard · normative)_ — VALUES provides inline data that can be directly included in a query ⟨§10.2⟩
- **[[sparql-11-query]]** _(standard · normative)_ — §14 refers to the separate SPARQL 1.1 Federated Query document, which uses the SERVICE keyword to query remote SPARQL endpoints ⟨§14⟩

## Where sources differ
Only one source in this KB, the normative SPARQL 1.1 Query Language Recommendation, treats the query forms directly, so no cross-source disagreement is recorded. Internally the specification marks DESCRIBE as informative — its exact output is left to the implementation — while SELECT, CONSTRUCT and ASK are normatively defined ⟨sparql-11-query §16⟩.

## See also
[[graph-pattern-matching]] · [[property-paths]] · [[rdf-dataset]]
