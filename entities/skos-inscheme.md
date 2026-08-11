---
title: "skos:inScheme"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-scheme]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:inScheme

## What it is
An object property relating a resource (typically a SKOS concept) to a concept scheme in which it is included.

## Key facts
- skos:inScheme is an instance of owl:ObjectProperty ⟨S3⟩.
- The rdfs:range of skos:inScheme is the class skos:ConceptScheme ⟨S4⟩.
- No domain is stated for skos:inScheme; its effective domain is the class of all resources (rdfs:Resource), so extensions may use it to link new classes of resource to a skos:ConceptScheme ⟨§4.6.5⟩.

## Relations
- Realizes: [[concept-scheme]]
- Defined in: [[skos]]
- Related: [[skos-conceptscheme]] · [[skos-topconceptof]]

## See also
[[skos-conceptscheme]]
