---
title: "skos:hasTopConcept"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[concept-scheme]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:hasTopConcept

## What it is
An object property linking a concept scheme to the SKOS concept(s) that are topmost in the hierarchical relations for that scheme.

## Key facts
- skos:hasTopConcept is an instance of owl:ObjectProperty ⟨S3⟩.
- The rdfs:domain of skos:hasTopConcept is the class skos:ConceptScheme ⟨S5⟩, and its rdfs:range is the class skos:Concept ⟨S6⟩.
- skos:hasTopConcept is owl:inverseOf the property skos:topConceptOf ⟨S8⟩; by convention it links a scheme to topmost concepts, but no integrity condition enforces this ⟨§4.6.3⟩.

## Relations
- Realizes: [[concept-scheme]]
- Defined in: [[skos]]
- Related: [[skos-topconceptof]] · [[skos-conceptscheme]]

## See also
[[skos-topconceptof]]
