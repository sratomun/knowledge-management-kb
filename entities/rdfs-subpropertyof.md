---
title: "rdfs:subPropertyOf"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-vocabulary-schema]]"]
sources: ["[[rdf-schema-11]]"]
updated: 2026-08-10
---

# rdfs:subPropertyOf

## What it is
`rdfs:subPropertyOf` is the property used to state that all resources related by one property are also related by another.

## Key facts
- "The rdfs:subPropertyOf property may be used to state that one property is a subproperty of another." If a property P is a subproperty of P', then all pairs of resources related by P are also related by P' ⟨§3.5⟩.
- `P1 rdfs:subPropertyOf P2` states P1 and P2 are instances of `rdf:Property` and P1 is a subproperty of P2; "The rdfs:subPropertyOf property is transitive." ⟨§3.5⟩
- The `rdfs:domain` and `rdfs:range` of `rdfs:subPropertyOf` are both `rdf:Property`; the specification "does not define a top property that is the super-property of all properties." ⟨§3.5⟩

## Relations
- Realizes: [[rdf-vocabulary-schema]]
- Defined in: [[rdf-schema-11]]
- Related: [[rdfs-property]] · [[rdfs-subclassof]]

## See also
[[rdfs-subclassof]] · [[org-w3c]]
