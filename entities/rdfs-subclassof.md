---
title: "rdfs:subClassOf"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-vocabulary-schema]]"]
sources: ["[[rdf-schema-11]]"]
updated: 2026-08-10
---

# rdfs:subClassOf

## What it is
`rdfs:subClassOf` is the property used to state that all the instances of one class are instances of another class.

## Key facts
- "The property rdfs:subClassOf is an instance of rdf:Property that is used to state that all the instances of one class are instances of another." ⟨§3.4⟩
- `C1 rdfs:subClassOf C2` states that C1 and C2 are instances of `rdfs:Class` and C1 is a subclass of C2; "The rdfs:subClassOf property is transitive." ⟨§3.4⟩
- The `rdfs:domain` of `rdfs:subClassOf` is `rdfs:Class` and its `rdfs:range` is `rdfs:Class` ⟨§3.4⟩.

## Relations
- Realizes: [[rdf-vocabulary-schema]]
- Defined in: [[rdf-schema-11]]
- Related: [[rdfs-class]] · [[rdfs-subpropertyof]] · [[rdfs-type]]

## See also
[[rdfs-subpropertyof]] · [[org-w3c]]
