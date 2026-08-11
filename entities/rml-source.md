---
title: "rml:source"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# rml:source

## What it is
The RML property that locates the input data source of a logical source, replacing R2RML's database-specific table/query addressing with a format-agnostic source reference.

## Key facts
- "The source (rml:source) locates the input data source. It is a [URI] that represents the data source where the data source is" ⟨§4.1⟩.
- A base source has "exactly one source (rml:source property)" ⟨§4.1⟩.
- "The value of the source (rml:source) specifies the data source or the database to be mapped. Its value can be either a string (implicit reference to the data source) or a valid [URI] of an existing source" ⟨§4.1⟩.

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[rml]]
- Related: [[rml-logicalsource]], [[rml-iterator]], [[rml-referenceformulation]]

## See also
[[logical-source-abstraction]] · [[rml-logicalsource]]
