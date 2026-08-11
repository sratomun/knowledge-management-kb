---
title: "rdfs:domain"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-vocabulary-schema]]", "[[rdf-data-model]]"]
sources: ["[[rdf-schema-11]]"]
updated: 2026-08-10
---

# rdfs:domain

## What it is
`rdfs:domain` is the property used to state that any resource that has a given property is an instance of one or more classes.

## Key facts
- "rdfs:domain is an instance of rdf:Property that is used to state that any resource that has a given property is an instance of one or more classes." ⟨§3.2⟩
- `P rdfs:domain C` states the resources denoted by the subjects of triples whose predicate is P are instances of class C; where P has more than one `rdfs:domain`, subjects are instances of all the stated classes ⟨§3.2⟩.
- The `rdfs:domain` of `rdfs:domain` is `rdf:Property` and its `rdfs:range` is `rdfs:Class` ⟨§3.2⟩.
- `rdfs:domain` and `rdfs:range` "do not provide any direct way to indicate property restrictions that are local to a class" ⟨§3 NOTE⟩.

## Relations
- Realizes: [[rdf-vocabulary-schema]]
- Defined in: [[rdf-schema-11]]
- Related: [[rdfs-range]] · [[rdfs-property]] · [[rdfs-class]]

## See also
[[rdfs-range]] · [[org-w3c]]
