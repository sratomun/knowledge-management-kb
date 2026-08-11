---
title: "rr:constant"
type: entity
subtype: vocabulary-term
aliases: ["R2RML constant-valued term map"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:constant

## What it is
The R2RML property defining a constant-valued term map, which ignores the table row and always generates the same fixed RDF term.

## Key facts
- "A constant-valued term map is a term map that ignores the logical table row and always generates the same RDF term"; it is represented by a resource that has exactly one rr:constant property ⟨§7.1⟩
- If the constant-valued term map is a subject map, predicate map or graph map, then its constant value MUST be an IRI; if it is an object map, its constant value MUST be an IRI or literal ⟨§7.1⟩
- Constant-valued term maps can be expressed more concisely using the constant shortcut properties rr:subject, rr:predicate, rr:object and rr:graph ⟨§7.1⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-column]], [[r2rml-template]], [[r2rml-termmap]]

## See also
[[r2rml-predicatemap]] · [[org-w3c]]
