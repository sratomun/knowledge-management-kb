---
title: "rr:inverseExpression"
type: entity
subtype: vocabulary-term
aliases: ["R2RML inverse expression"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:inverseExpression

## What it is
The R2RML property giving an optional inverse expression for a column- or template-valued term map, used to "reverse" a generated RDF term back to an efficient SQL lookup of its source row.

## Key facts
- "An inverse expression is a string template associated with a column-valued term map or template-value term map"; this property is optional and there MUST NOT be more than one for a term map ⟨§7.7⟩
- Inverse expressions are useful for optimizing term maps that reference derived columns in R2RML views, allowing the use of indexes on the underlying relational tables ⟨§7.7⟩
- Every column reference in the inverse expression MUST be an existing column in the logical table associated with the term map ⟨§7.7⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-r2rmlview]], [[r2rml-column]], [[r2rml-template]]

## See also
[[r2rml-termmap]] · [[org-w3c]]
