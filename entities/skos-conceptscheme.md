---
title: "skos:ConceptScheme"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-scheme]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:ConceptScheme

## What it is
The class of SKOS concept schemes. A concept scheme can be viewed as an aggregation of one or more SKOS concepts, together with the semantic relationships between them; it corresponds roughly to an individual thesaurus, classification scheme or subject heading system.

## Key facts
- skos:ConceptScheme is an instance of owl:Class ⟨S2⟩.
- Integrity condition: skos:ConceptScheme is disjoint with skos:Concept ⟨S9⟩.
- There is no way to close the boundary of a concept scheme: SKOS can describe a scheme but "does not provide any mechanism to completely define a concept scheme," and a concept may take part in zero, one or more schemes ⟨§4.6.1⟩.

## Relations
- Realizes: [[concept-scheme]]
- Defined in: [[skos]]
- Related: [[skos-inscheme]] · [[skos-hastopconcept]] · [[skos-topconceptof]]

## See also
[[skos-concept]]
