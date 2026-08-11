---
title: "skos:note"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: []
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:note

## What it is
The general SKOS documentation property for associating a note of any kind (plain text, hypertext, image, definition, scope information, editorial information, etc.) with a resource. It is the parent property of the six specific note types and an extension point for defining more specific notes.

## Key facts
- skos:note, skos:changeNote, skos:definition, skos:editorialNote, skos:example, skos:historyNote and skos:scopeNote are each instances of owl:AnnotationProperty ⟨S16⟩.
- skos:changeNote, skos:definition, skos:editorialNote, skos:example, skos:historyNote and skos:scopeNote are each sub-properties of skos:note ⟨S17⟩.
- No domain or range is stated for the SKOS documentation properties; their effective domain and range is the class of all resources (rdfs:Resource) ⟨§7.5.1⟩ ⟨§7.5.2⟩.

## Relations
- Defined in: [[skos]]
- Related: [[skos-concept]]

## See also
[[skos-concept]]
