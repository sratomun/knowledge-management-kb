---
title: "skosxl:prefLabel"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skosxl:prefLabel

## What it is
The SKOS-XL object property used to label a SKOS concept with a preferred skosxl:Label instance — analogous to skos:prefLabel but pointing to a reified label rather than a plain literal.

## Key facts
- skosxl:prefLabel, skosxl:altLabel and skosxl:hiddenLabel are each instances of owl:ObjectProperty ⟨S53⟩, with rdfs:range the class skosxl:Label ⟨S54⟩.
- The property chain (skosxl:prefLabel, skosxl:literalForm) is a sub-property of skos:prefLabel ⟨S55⟩ — the "dumbing-down" link back to SKOS lexical labels.
- skosxl:prefLabel, skosxl:altLabel and skosxl:hiddenLabel are pairwise disjoint properties ⟨S58⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skosxl-label]] · [[skos-preflabel]]

## See also
[[skosxl-label]] · [[skos-preflabel]]
