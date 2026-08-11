---
title: "rr:ObjectMap"
type: entity
subtype: vocabulary-term
aliases: ["R2RML object map"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:ObjectMap

## What it is
The R2RML term map that generates the object of RDF triples within a predicate-object map. Objects may be IRIs, blank nodes, or literals.

## Key facts
- "An object map is a term map" ⟨§6.3⟩
- An object map may be specified using the rr:objectMap property (whose value must be an object map or a referencing object map) or the constant shortcut property rr:object ⟨§6.3⟩
- If an object map has an rr:termType it MUST be rr:IRI, rr:BlankNode, or rr:Literal; absent an explicit value the default is rr:Literal when it is column-based or has rr:language or rr:datatype, and rr:IRI otherwise ⟨§7.4⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-predicateobjectmap]], [[r2rml-refobjectmap]], [[r2rml-termtype]]

## See also
[[r2rml-template]] · [[org-w3c]]
