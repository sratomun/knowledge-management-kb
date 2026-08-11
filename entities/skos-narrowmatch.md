---
title: "skos:narrowMatch"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[scheme-mapping]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:narrowMatch

## What it is
A mapping property stating a hierarchical mapping link between two concepts in different concept schemes, where the object is narrower than the subject.

## Key facts
- skos:narrowMatch is a sub-property of skos:mappingRelation ⟨S40⟩ and a sub-property of skos:narrower ⟨S41⟩.
- skos:narrowMatch is owl:inverseOf the property skos:broadMatch ⟨S43⟩.
- Because skos:exactMatch is symmetric and skos:broadMatch and skos:narrowMatch are inverses, skos:exactMatch is also disjoint with skos:narrowMatch ⟨S46⟩.

## Relations
- Realizes: [[scheme-mapping]]
- Defined in: [[skos]]
- Related: [[skos-broadmatch]] · [[skos-narrower]]

## See also
[[skos-broadmatch]]
