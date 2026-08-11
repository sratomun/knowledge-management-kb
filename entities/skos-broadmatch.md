---
title: "skos:broadMatch"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[scheme-mapping]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:broadMatch

## What it is
A mapping property stating a hierarchical mapping link between two concepts in different concept schemes, where the object is broader than the subject.

## Key facts
- skos:broadMatch is a sub-property of skos:mappingRelation ⟨S40⟩ and a sub-property of skos:broader ⟨S41⟩.
- skos:narrowMatch is owl:inverseOf the property skos:broadMatch ⟨S43⟩.
- Integrity condition: skos:exactMatch is disjoint with skos:broadMatch (a clash between exact and hierarchical mapping links is not consistent) ⟨S46⟩.

## Relations
- Realizes: [[scheme-mapping]]
- Defined in: [[skos]]
- Related: [[skos-narrowmatch]] · [[skos-broader]]

## See also
[[skos-narrowmatch]]
