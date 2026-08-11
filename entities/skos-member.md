---
title: "skos:member"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-collection]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:member

## What it is
An object property relating a SKOS collection to a member, where a member may itself be either a concept or a (nested) collection.

## Key facts
- skos:member and skos:memberList are each instances of owl:ObjectProperty ⟨S30⟩.
- The rdfs:domain of skos:member is the class skos:Collection ⟨S31⟩.
- The rdfs:range of skos:member is the union of the classes skos:Concept and skos:Collection ⟨S32⟩.

## Relations
- Realizes: [[concept-collection]]
- Defined in: [[skos]]
- Related: [[skos-collection]] · [[skos-memberlist]]

## See also
[[skos-collection]]
