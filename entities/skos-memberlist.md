---
title: "skos:memberList"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-collection]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:memberList

## What it is
An object property giving the ordered list of members of a skos:OrderedCollection, whose value is an RDF List.

## Key facts
- The rdfs:domain of skos:memberList is the class skos:OrderedCollection ⟨S33⟩ and its rdfs:range is the class rdf:List ⟨S34⟩.
- skos:memberList is an instance of owl:FunctionalProperty ⟨S35⟩.
- For any resource, every item in the list given as the value of skos:memberList is also a value of the skos:member property ⟨S36⟩.

## Relations
- Realizes: [[concept-collection]]
- Defined in: [[skos]]
- Related: [[skos-orderedcollection]] · [[skos-member]]

## See also
[[skos-orderedcollection]] · [[skos-member]]
