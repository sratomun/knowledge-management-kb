---
title: "rml:reference"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# rml:reference

## What it is
The RML property that refers to a column, record, element, or object of a source, defining a reference-valued term map — RML's format-agnostic replacement for R2RML's column-only `rr:column`.

## Key facts
- A reference (`rml:reference`) is used to refer to a column (databases), a record (CSV/TSV), an element (XML), or an object (JSON) ⟨§6.2⟩.
- "A reference must be a valid expression, considering the reference formulation (rml:referenceFormulation) specified" ⟨§6.2⟩.
- "A reference-valued term map is a term map that is represented by a resource that has exactly one rml:reference property" ⟨§6.2⟩.
- "The object of the rml:reference property must be an RDF literal encoding a valid reference formulation, e.g. a column identifier according to the SQL2008 specification..., a valid XPath expression..., or a valid JSONPath expression" ⟨§6.2⟩.

## Relations
- Realizes: [[term-map]]
- Defined in: [[rml]]
- Related: [[rml-referenceformulation]]
- Reuses (R2RML): [[r2rml-subjectmap]], [[r2rml-predicateobjectmap]]

## See also
[[term-map]] · [[rml-referenceformulation]]
