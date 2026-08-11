---
title: "SPARQL CONSTRUCT"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[sparql-query-forms]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL CONSTRUCT

## What it is
CONSTRUCT is the SPARQL query form that returns an RDF graph, built by substituting the bindings of each query solution into a graph template of triple patterns.

## Key facts
- "The CONSTRUCT query form returns a single RDF graph specified by a graph template." The result is formed by taking each query solution, substituting for the variables in the graph template, and combining the triples into a single RDF graph by set union ⟨§16.2⟩
- CONSTRUCT "Returns an RDF graph constructed by substituting variables in a set of triple templates." ⟨§16.2⟩
- The CONSTRUCT WHERE short form allows a template to be omitted when it is identical to the WHERE clause pattern ⟨§16.2.4⟩
- Using ORDER BY on a solution sequence for a CONSTRUCT query "has no direct effect because only SELECT returns a sequence of results" ⟨§15.1⟩

## Relations
- Realizes: [[sparql-query-forms]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-select]] · [[sparql-ask]] · [[sparql-describe]]

## See also
[[sparql-query-forms]] · [[org-w3c]]
