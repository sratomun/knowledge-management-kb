---
title: "skos:OrderedCollection"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-collection]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:OrderedCollection

## What it is
The class of ordered SKOS concept collections — collections whose members are arranged in a meaningful order, expressed via skos:memberList.

## Key facts
- skos:OrderedCollection is an instance of owl:Class ⟨S28⟩.
- skos:OrderedCollection is a sub-class of skos:Collection ⟨S29⟩.
- The rdfs:domain of skos:memberList is the class skos:OrderedCollection ⟨S33⟩; a collection can be inferred from an ordered collection via S36, but SKOS provides no way to explicitly state that a collection is not ordered ⟨§9.6.1⟩.

## Relations
- Realizes: [[concept-collection]]
- Defined in: [[skos]]
- Related: [[skos-collection]] · [[skos-memberlist]]

## See also
[[skos-collection]] · [[skos-memberlist]]
