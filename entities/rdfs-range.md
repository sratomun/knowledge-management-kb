---
title: "rdfs:range"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-vocabulary-schema]]", "[[rdf-data-model]]"]
sources: ["[[rdf-schema-11]]"]
updated: 2026-08-10
---

# rdfs:range

## What it is
`rdfs:range` is the property used to state that the values of a property are instances of one or more classes.

## Key facts
- "rdfs:range is an instance of rdf:Property that is used to state that the values of a property are instances of one or more classes." ⟨§3.1⟩
- `P rdfs:range C` states the resources denoted by the objects of triples whose predicate is P are instances of class C; where P has more than one `rdfs:range`, objects are instances of all the stated classes ⟨§3.1⟩.
- The `rdfs:range` of `rdfs:range` is `rdfs:Class` and its `rdfs:domain` is `rdf:Property` ⟨§3.1⟩.
- RDF Schema "provides a mechanism for describing this information, but does not say whether or how an application should use it" — domain/range are descriptive, not enforced ⟨§4⟩.

## Relations
- Realizes: [[rdf-vocabulary-schema]]
- Defined in: [[rdf-schema-11]]
- Related: [[rdfs-domain]] · [[rdfs-property]] · [[rdfs-class]]

## See also
[[rdfs-domain]] · [[org-w3c]]
