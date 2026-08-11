---
title: "rr:Join"
type: entity
subtype: vocabulary-term
aliases: ["R2RML join condition"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:Join

## What it is
The R2RML vocabulary class for a join condition used by a referencing object map to relate a child logical table to a parent logical table on named columns.

## Key facts
- A join condition is represented by a resource that has exactly one value for each of rr:child and rr:parent ⟨§8⟩
- The rr:child value (the join condition's child column) MUST be a column name that exists in the logical table of the triples map that contains the referencing object map ⟨§8⟩
- The rr:parent value (the join condition's parent column) MUST be a column name that exists in the logical table of the referencing object map's parent triples map ⟨§8⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-refobjectmap]]

## See also
[[r2rml-r2rmlview]] · [[org-w3c]]
