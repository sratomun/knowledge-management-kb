---
title: "skos:Collection"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-collection]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:Collection

## What it is
The class of SKOS concept collections — labeled and/or ordered groups of SKOS concepts. Collections are useful where a group of concepts shares something in common and it is convenient to group them under a common label (e.g. thesaurus node labels).

## Key facts
- skos:Collection is an instance of owl:Class ⟨S28⟩.
- The rdfs:domain of skos:member is the class skos:Collection ⟨S31⟩.
- Integrity condition: skos:Collection is disjoint with each of skos:Concept and skos:ConceptScheme ⟨S37⟩.

## Relations
- Realizes: [[concept-collection]]
- Defined in: [[skos]]
- Related: [[skos-orderedcollection]] · [[skos-member]]

## See also
[[skos-member]] · [[skos-orderedcollection]]
