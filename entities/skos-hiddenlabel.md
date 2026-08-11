---
title: "skos:hiddenLabel"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:hiddenLabel

## What it is
A lexical label that should be accessible to text-based indexing/search but not otherwise visible to users — useful for capturing misspellings so a query can still match the relevant concept without encouraging further mistakes.

## Key facts
- skos:hiddenLabel is an instance of owl:AnnotationProperty ⟨S10⟩ and a sub-property of rdfs:label ⟨S11⟩, with rdfs:range the class of RDF plain literals ⟨S12⟩.
- Integrity condition: skos:prefLabel, skos:altLabel and skos:hiddenLabel are pairwise disjoint properties ⟨S13⟩.
- Hidden labels are useful when interacting with a KOS via a text-based search function, e.g. matching a mis-spelled query while remaining invisible to the user ⟨§5.1⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skos-preflabel]] · [[skos-altlabel]]

## See also
[[skos-altlabel]] · [[skosxl-label]]
