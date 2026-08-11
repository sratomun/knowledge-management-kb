---
title: "rml:referenceFormulation"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[reference-formulation]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# rml:referenceFormulation

## What it is
The RML property — and class of supported reference formulations — that declares which query/expression language is used to refer to elements of a source (e.g. XPath, JSONPath, SQL2008).

## Key facts
- "rml:referenceFormulation is the class of supported reference formulations" ⟨§2⟩.
- "The reference formulation (rml:referenceFormulation) defines the reference formulation used to refer to the elements of the data source. The reference formulation should always be specified using rml:referenceFormulation" ⟨§4.1⟩.
- In case of relational databases, to remain backwards compliant with R2RML, `rr:sqlVersion` can be used instead of `rml:referenceFormulation` ⟨§4.1⟩.
- Examples of reference formulations are SQL2008 for relational databases, `ql:XPath` for XML, and `ql:JSONPath` for JSON data sources ⟨§4.1⟩.

## Relations
- Realizes: [[reference-formulation]]
- Defined in: [[rml]]
- Related: [[ql-csv]], [[ql-xpath]], [[ql-jsonpath]]
- Reuses (R2RML): [[r2rml-sql2008]]

## See also
[[reference-formulation]] · [[ql-xpath]] · [[ql-jsonpath]]
