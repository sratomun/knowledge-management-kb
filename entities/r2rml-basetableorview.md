---
title: "rr:BaseTableOrView"
type: entity
subtype: vocabulary-term
aliases: ["SQL base table or view (R2RML)"]
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:BaseTableOrView

## What it is
The R2RML vocabulary class for a logical table that draws its data directly from a base table or view in the input database, identified by name.

## Key facts
- A SQL base table or view is represented by a resource that has exactly one rr:tableName property ⟨§5.1⟩
- The value of rr:tableName MUST be a valid schema-qualified name that names an existing base table or view in the input database ⟨§5.1⟩
- Its effective SQL query is SELECT * FROM {table}, with {table} replaced by the table or view name ⟨§5.1⟩

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[r2rml]]
- Related: [[r2rml-logicaltable]], [[r2rml-r2rmlview]]

## See also
[[r2rml-triplesmap]] · [[org-w3c]]
