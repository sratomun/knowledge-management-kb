---
title: "skos:prefLabel"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:prefLabel

## What it is
The preferred lexical label for a resource in a given natural language — the label providing the strongest clue to a concept's meaning, used when generating human-readable representations of a KOS.

## Key facts
- skos:prefLabel, skos:altLabel and skos:hiddenLabel are each instances of owl:AnnotationProperty ⟨S10⟩ and each sub-properties of rdfs:label ⟨S11⟩; their rdfs:range is the class of RDF plain literals ⟨S12⟩.
- Integrity condition: skos:prefLabel, skos:altLabel and skos:hiddenLabel are pairwise disjoint properties ⟨S13⟩.
- Integrity condition: "A resource has no more than one value of skos:prefLabel per language tag" ⟨S14⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skos-altlabel]] · [[skos-hiddenlabel]]

## See also
[[skos-altlabel]] · [[skosxl-preflabel]]
