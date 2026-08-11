---
title: "rr:termType"
type: entity
subtype: vocabulary-term
aliases: ["R2RML term type"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:termType

## What it is
The R2RML property that selects the kind of RDF term a column- or template-valued term map produces: an IRI, a blank node, or a literal.

## Key facts
- The value of rr:termType MUST be an IRI and MUST be one of the options allowed for the map's position — subject map: rr:IRI or rr:BlankNode; predicate map: rr:IRI; object map: rr:IRI, rr:BlankNode, or rr:Literal; graph map: rr:IRI ⟨§7.4⟩
- If the term map does not have a rr:termType property, its term type is rr:Literal when it is an object map that is column-based or has rr:language or rr:datatype, and rr:IRI otherwise ⟨§7.4⟩
- Constant-valued term maps are not considered as having a term type, and specifying rr:termType on them has no effect ⟨§7.4⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-termmap]], [[r2rml-objectmap]], [[r2rml-defaultgraph]]

## See also
[[r2rml-template]] · [[org-w3c]]
