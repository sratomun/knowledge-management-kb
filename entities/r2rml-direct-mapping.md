---
title: "Direct Mapping of Relational Data to RDF"
type: entity
subtype: specification-construct
aliases: ["Direct Mapping (RDB2RDF)", "R2RML DM companion"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# Direct Mapping of Relational Data to RDF

## What it is
The companion W3C specification [DM] that defines a fixed, automatic mapping from a relational database to RDF. R2RML cites it as the contrasting, non-customizable alternative and reuses it to define default mappings.

## Key facts
- In the direct mapping of a database, the structure of the resulting RDF graph directly reflects the structure of the database, the target RDF vocabulary directly reflects the names of database schema elements, and neither structure nor target vocabulary can be changed ⟨§1⟩
- An R2RML default mapping generator's output SHOULD be the Direct Graph corresponding to the input database ⟨§4.4⟩
- The normative reference [DM] is "A Direct Mapping of Relational Data to RDF", a W3C Recommendation of 27 September 2012 ⟨§C.1⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-mapping-document]]

## See also
[[org-w3c]]

<!-- NOTE: [DM] is a distinct W3C Recommendation cited by R2RML. If ingested as its own source later, resolve to that source page rather than duplicating this reference entity. -->
