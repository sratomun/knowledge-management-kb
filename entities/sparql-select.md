---
title: "SPARQL SELECT"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[sparql-query-forms]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL SELECT

## What it is
SELECT is the SPARQL query form that returns variable bindings — a solution sequence in which selected query variables are bound to RDF terms from graph pattern matches.

## Key facts
- The SELECT query form "Returns all, or a subset of, the variables bound in a query pattern match." ⟨§16.1⟩
- SELECT expressions allow new values to be projected by evaluating an expression and binding it to a variable in the SELECT clause ⟨§16.1.2⟩
- In aggregate queries, variables that appear in the query pattern but are not in the GROUP BY clause "can only be projected or used in select expressions if they are aggregated" ⟨§11.4⟩
- Only SELECT returns a sequence of results, so ORDER BY combined with LIMIT and OFFSET selects a slice of that sequence ⟨§15.1⟩

## Relations
- Realizes: [[sparql-query-forms]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-construct]] · [[sparql-ask]] · [[sparql-describe]]

## See also
[[sparql-query-forms]] · [[sparql-bgp]] · [[org-w3c]]
