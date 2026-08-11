---
title: "SPARQL DESCRIBE"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[sparql-query-forms]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL DESCRIBE

## What it is
DESCRIBE is the SPARQL query form that returns an RDF graph describing the resources found, where the shape of the description is chosen by the query service rather than the query. Section 16.4 is informative.

## Key facts
- "The DESCRIBE form returns a single result RDF graph containing RDF data about resources." ⟨§16.4⟩
- The description "is not prescribed by a SPARQL query" but "is determined by the SPARQL query processor"; the DESCRIBE form takes each resource identified in a solution, together with any resources directly named by IRI, and assembles a single RDF graph ⟨§16.4⟩
- "The description is determined by the query service." ⟨§16.4⟩
- "The syntax DESCRIBE * is an abbreviation that describes all of the variables in a query." ⟨§16.4⟩

## Relations
- Realizes: [[sparql-query-forms]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-select]] · [[sparql-construct]] · [[sparql-ask]]

## See also
[[sparql-query-forms]] · [[org-w3c]]
