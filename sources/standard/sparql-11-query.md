---
title: "SPARQL 1.1 Query Language"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["SPARQL 1.1", "SPARQL Query"]
publisher: W3C
url: https://www.w3.org/TR/sparql11-query/
version: "1.1 (2013-03-21)"
published: 2013-03
effective_from: 2013-03-21
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# SPARQL 1.1 Query Language

## Scope & purpose

SPARQL 1.1 Query Language is the W3C Recommendation that defines the syntax and semantics of the SPARQL query language for RDF. SPARQL can be used to express queries across diverse data sources, whether the data is stored natively as RDF or viewed as RDF via middleware. It contains capabilities for querying required and optional graph patterns along with their conjunctions and disjunctions, and it also supports aggregation, subqueries, negation, creating values by expressions, extensible value testing, and constraining queries by source RDF graph. The results of SPARQL queries can be result sets or RDF graphs. The specification is one of eleven SPARQL 1.1 Recommendations produced by the SPARQL Working Group.

## Structure

- §1 Introduction — document outline, conventions, namespaces, terminology.
- §2 Making Simple Queries (Informative) — basic graph patterns, multiple matches, matching literals, values from expressions, building RDF graphs.
- §3 RDF Term Constraints (Informative) — informal introduction to FILTER.
- §4 SPARQL Syntax — RDF term syntax (IRIs, literals, variables, blank nodes) and triple-pattern syntax.
- §5 Graph Patterns — basic graph patterns (§5.1) and group graph patterns (§5.2).
- §6 Including Optional Values — OPTIONAL pattern matching.
- §7 Matching Alternatives — UNION.
- §8 Negation — FILTER NOT EXISTS / EXISTS (§8.1) and MINUS (§8.2), and their differences (§8.3).
- §9 Property Paths — path syntax, examples, equivalent patterns, arbitrary-length matching.
- §10 Assignment — BIND (§10.1) and VALUES inline data (§10.2).
- §11 Aggregates — aggregate example, GROUP BY, HAVING, projection restrictions.
- §12 Subqueries.
- §13 RDF Dataset — default and named graphs, FROM / FROM NAMED, GRAPH.
- §14 Basic Federated Query — refers to the separate SPARQL 1.1 Federated Query document.
- §15 Solution Sequences and Modifiers — ORDER BY, projection, DISTINCT/REDUCED, OFFSET, LIMIT.
- §16 Query Forms — SELECT (§16.1), CONSTRUCT (§16.2), ASK (§16.3), DESCRIBE (§16.4).
- §17 Expressions and Testing Values — operand types, filter evaluation, operator mapping, function library, extensibility.
- §18 Definition of SPARQL — translation to the SPARQL algebra and evaluation semantics.
- §19 SPARQL Grammar — normative EBNF grammar.
- §20 Conformance; §21 Security Considerations (Informative); §22 Internet Media Type, File Extension and Macintosh File Type; Appendix A References.

## Key points

- SPARQL is based around graph pattern matching; more complex graph patterns are formed by combining basic graph patterns, group graph patterns, optional graph patterns, alternative graph patterns, and patterns on named graphs ⟨§5⟩.
- A basic graph pattern is a set of triple patterns, where each of the subject, predicate and object may be a variable; it matches a subgraph when RDF terms may be substituted for the variables and the result is RDF graph equivalent to the subgraph ⟨§2, §5.1⟩.
- Blank node labels are scoped to a basic graph pattern: "A label can be used in only a single basic graph pattern in any query." ⟨§5.1.1⟩.
- A group graph pattern is delimited with braces `{}`; a FILTER constraint "is a restriction on solutions over the whole group in which the filter appears." ⟨§5.2.2⟩.
- Optional matching adds bindings where the optional graph pattern matches, but if the optional part does not match "it creates no bindings but does not eliminate the solution." ⟨§6.1⟩.
- UNION combines graph patterns so that one of several alternatives may match; if more than one alternative matches, all the possible pattern solutions are found ⟨§7⟩.
- SPARQL incorporates two styles of negation — FILTER NOT EXISTS / EXISTS and MINUS — and in some cases they can produce different answers ⟨§8, §8.3⟩.
- Property paths add a compact representation of queries and the ability to match arbitrary-length paths in the graph ⟨§9⟩.
- Assignment binds a new variable to the value of an expression via the BIND keyword, expressions in the SELECT clause, or expressions in the GROUP BY clause; "The variable introduced by the BIND clause must not have been used in the group graph pattern up to the point of use in BIND." ⟨§10, §10.1⟩.
- VALUES provides inline data that can be directly included in a query ⟨§10.2⟩.
- Aggregates (COUNT, SUM, MIN, MAX, AVG, SAMPLE, GROUP_CONCAT) apply over groups formed by GROUP BY, with HAVING filtering the resulting groups ⟨§11⟩.
- A subquery embeds one SELECT query within the graph pattern of another, allowing results to be computed and then joined ⟨§12⟩.
- The four query forms produce results in different forms: SELECT returns variable bindings; CONSTRUCT returns an RDF graph built from a template; ASK returns a boolean; and DESCRIBE (informative) returns an RDF graph describing the resources found ⟨§16⟩.
- Solution sequence modifiers order (ORDER BY), project, remove duplicates (DISTINCT / REDUCED), and slice (OFFSET, LIMIT) the sequence of solutions ⟨§15⟩.
- The RDF Dataset comprises one default graph and zero or more named graphs; FROM and FROM NAMED specify the dataset for a query, and GRAPH scopes matching to named graphs ⟨§13⟩.
- Section 14 refers to the separate document SPARQL 1.1 Federated Query, which uses the SERVICE keyword to query remote SPARQL endpoints ⟨§14⟩.
- Section 17 defines an extensible value-testing and expression framework (a function library over RDF terms, strings, numerics, dates/times and hashes), and section 18 gives the formal SPARQL algebra and evaluation semantics; "SPARQL language extensions may provide additional associations between operators and operator functions." ⟨§17, §17.3.1, §18⟩.

## Concepts & entities covered
Concepts: [[graph-pattern-matching]] · [[sparql-query-forms]] · [[property-paths]]
Entities: [[sparql-select]] · [[sparql-construct]] · [[sparql-ask]] · [[sparql-describe]] · [[sparql-bgp]] · [[sparql-filter]] · [[sparql-optional]] · [[sparql-union]] · [[sparql-property-path]]
