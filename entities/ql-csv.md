---
title: "ql:CSV"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[reference-formulation]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# ql:CSV

## What it is
The RML reference formulation used to address records of a CSV data source, declared as the value of `rml:referenceFormulation`.

## Key facts
- A CSV logical source is declared with `rml:referenceFormulation ql:CSV` ⟨§3.1, §4.1⟩.
- "RML mappings for CSV data sources follow exactly the same syntax as in R2RML to refer to the CSV's records. It is considered as a correspondence of CSV records to the databases' rows, delimited by a line break (CRLF)" ⟨§3.1⟩.
- For CSV data sources only the source and, optionally, the logical iterator need be defined ⟨§4.1⟩.

## Relations
- Realizes: [[reference-formulation]]
- Defined in: [[rml]]
- Related: [[rml-referenceformulation]], [[ql-xpath]], [[ql-jsonpath]]

## See also
[[reference-formulation]] · [[rml-referenceformulation]]
