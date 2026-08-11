---
title: "skos:related"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[semantic-relation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:related

## What it is
A property asserting an associative link between two SKOS concepts — indicating the two are inherently related, but that neither is in any way more general than the other.

## Key facts
- skos:related is an instance of owl:ObjectProperty ⟨S18⟩ and a sub-property of skos:semanticRelation ⟨S21⟩.
- skos:related is an instance of owl:SymmetricProperty ⟨S23⟩.
- Integrity condition: skos:related is disjoint with the property skos:broaderTransitive (and, because it is symmetric and the transitive properties are inverses, also disjoint with skos:narrowerTransitive) ⟨S27⟩.

## Relations
- Realizes: [[semantic-relation]]
- Defined in: [[skos]]
- Related: [[skos-broadertransitive]] · [[skos-relatedmatch]]

## See also
[[skos-broader]] · [[skos-relatedmatch]]
