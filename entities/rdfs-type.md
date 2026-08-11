---
title: "rdf:type"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-vocabulary-schema]]", "[[rdf-data-model]]"]
sources: ["[[rdf-schema-11]]"]
updated: 2026-08-10
---

# rdf:type

## What it is
`rdf:type` is the property used to state that a resource is an instance of a class.

## Key facts
- "rdf:type is an instance of rdf:Property that is used to state that a resource is an instance of a class." ⟨§3.3⟩
- `R rdf:type C` states that C is an instance of `rdfs:Class` and R is an instance of C ⟨§3.3⟩.
- The `rdfs:domain` of `rdf:type` is `rdfs:Resource` and its `rdfs:range` is `rdfs:Class` ⟨§3.3⟩.

## Relations
- Realizes: [[rdf-vocabulary-schema]]
- Defined in: [[rdf-schema-11]]
- Related: [[rdfs-class]] · [[rdfs-subclassof]] · [[rdfs-property]]

## See also
[[rdfs-class]] · [[org-w3c]]
