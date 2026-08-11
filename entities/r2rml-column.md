---
title: "rr:column"
type: entity
subtype: vocabulary-term
aliases: ["R2RML column-valued term map"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:column

## What it is
The R2RML property defining a column-valued term map, whose generated term is taken from the value of a single named column in the logical table row.

## Key facts
- A column-valued term map is represented by a resource that has exactly one rr:column property ⟨§7.2⟩
- The value of the rr:column property MUST be a valid column name; the column value of the term map is the data value of that column in a given logical table row ⟨§7.2⟩
- The referenced columns of a column-valued term map is the singleton set containing the value of the term map's rr:column property ⟨§7.2⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-template]], [[r2rml-constant]], [[r2rml-termmap]]

## See also
[[r2rml-inverseexpression]] · [[org-w3c]]
