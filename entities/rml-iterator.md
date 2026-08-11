---
title: "rml:iterator"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# rml:iterator

## What it is
The RML property that defines the per-record iteration loop over a logical source, generalizing R2RML's implicit row iteration to elements (XML) and objects (JSON).

## Key facts
- "The logical iterator (rml:iterator) defines the iteration loop used to map the data of the input source" ⟨§4.1⟩.
- A base source has "exactly one logical iterator over the data source's rml:iterator" ⟨§4.1⟩.
- "A logical iterator must be a valid identifier, considering the reference formulation (rml:referenceFormulation) specified" ⟨§4.1⟩.
- "As default iterator is considered the row"; if not specified it is a "row" for databases, CSV or TSV, and for XML/JSON it is a valid reference to an element or object respectively ⟨§4.1⟩.

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[rml]]
- Related: [[rml-logicalsource]], [[rml-referenceformulation]]

## See also
[[logical-source-abstraction]] · [[rml-logicalsource]]
