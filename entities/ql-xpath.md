---
title: "ql:XPath"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[reference-formulation]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# ql:XPath

## What it is
The RML reference formulation used to address elements of an XML data source with XPath expressions, declared as the value of `rml:referenceFormulation`.

## Key facts
- "[XPath] is the default reference formulation used by RML for XML data sources" ⟨§3.2, §4.1⟩.
- An XML logical source requires all three of `rml:source`, `rml:iterator`, and `rml:referenceFormulation` to be defined ⟨§4.1⟩.
- References to XML elements "follow the syntax of the reference formulation specified at the logical source" ⟨§3.2⟩.

## Relations
- Realizes: [[reference-formulation]]
- Defined in: [[rml]]
- Related: [[rml-referenceformulation]], [[ql-csv]], [[ql-jsonpath]]

## See also
[[reference-formulation]] · [[rml-referenceformulation]]
