---
title: "skos:altLabel"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:altLabel

## What it is
An alternative lexical label for a resource — a synonym, near-synonym or abbreviation useful alongside the preferred label when creating human-readable representations of a KOS.

## Key facts
- skos:altLabel is an instance of owl:AnnotationProperty ⟨S10⟩ and a sub-property of rdfs:label ⟨S11⟩, with rdfs:range the class of RDF plain literals ⟨S12⟩.
- Integrity condition: skos:prefLabel, skos:altLabel and skos:hiddenLabel are pairwise disjoint properties ⟨S13⟩.
- SKOS allows alternative labels without a preferred label; there is no condition requiring a skos:prefLabel where a skos:altLabel is asserted ⟨§5.6.4⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skos-preflabel]] · [[skos-hiddenlabel]]

## See also
[[skos-preflabel]] · [[skosxl-label]]
