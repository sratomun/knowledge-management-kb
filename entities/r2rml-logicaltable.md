---
title: "rr:LogicalTable"
type: entity
subtype: vocabulary-term
aliases: ["R2RML logical table"]
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:LogicalTable

## What it is
The R2RML vocabulary class for a logical table: the tabular SQL query result that a triples map maps to RDF. It abstracts the input the mapping reads from, whether a stored table/view or a query.

## Key facts
- "A logical table is a tabular SQL query result that is to be mapped to RDF triples"; it is either a SQL base table or view, or an R2RML view ⟨§5⟩
- Every logical table has an effective SQL query that, if executed over the SQL connection, produces the contents of the logical table ⟨§5⟩
- rr:LogicalTable has two subclasses, rr:R2RMLView and rr:BaseTableOrView ⟨§4.1⟩

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[r2rml]]
- Related: [[r2rml-basetableorview]], [[r2rml-r2rmlview]], [[r2rml-triplesmap]]

## See also
[[r2rml-sql2008]] · [[org-w3c]]
