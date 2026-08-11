---
title: "skos:relatedMatch"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[scheme-mapping]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:relatedMatch

## What it is
A mapping property stating an associative mapping link between two concepts in different concept schemes.

## Key facts
- skos:relatedMatch is a sub-property of skos:mappingRelation ⟨S40⟩ and a sub-property of skos:related ⟨S41⟩.
- skos:relatedMatch is an instance of owl:SymmetricProperty ⟨S44⟩.
- Integrity condition: skos:exactMatch is disjoint with skos:relatedMatch (a clash between exact and associative mapping links is not consistent) ⟨S46⟩.

## Relations
- Realizes: [[scheme-mapping]]
- Defined in: [[skos]]
- Related: [[skos-related]] · [[skos-mappingrelation]]

## See also
[[skos-related]]
