---
title: "ql:JSONPath"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[reference-formulation]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# ql:JSONPath

## What it is
The RML reference formulation used to address objects of a JSON data source with JSONPath expressions, declared as the value of `rml:referenceFormulation`.

## Key facts
- "JSONPath is the default reference formulation used by RML for references to JSON data sources" ⟨§3.3, §4.1⟩.
- A JSON logical source requires all three of `rml:source`, `rml:iterator`, and `rml:referenceFormulation` to be defined ⟨§4.1⟩.
- "RML supports writing relative JSONPath expressions. These do not exist in the proposed JSONPath framework"; the current reference value is addressed with the `@` JSONPath expression ⟨§6.2.4⟩.

## Relations
- Realizes: [[reference-formulation]]
- Defined in: [[rml]]
- Related: [[rml-referenceformulation]], [[ql-csv]], [[ql-xpath]]

## See also
[[reference-formulation]] · [[rml-referenceformulation]]
