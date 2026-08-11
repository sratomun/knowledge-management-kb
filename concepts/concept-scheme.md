---
title: "Concept scheme"
type: concept
tags: [knowledge-organization]
related: ["[[controlled-vocabulary]]", "[[concept-collection]]", "[[semantic-relation]]"]
updated: 2026-08-09
---

# Concept scheme

## What it is

A concept scheme is the container that aggregates a set of concepts together with the links among them, giving a controlled vocabulary an identity as a single knowledge organization system. It lets a thesaurus, taxonomy, or classification scheme be named, referred to, and distinguished from the individual concepts it groups.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — A concept scheme aggregates concepts and their links: `skos:ConceptScheme` is an `owl:Class` (S2), disjoint with `skos:Concept` (S9, an integrity condition); `skos:topConceptOf` is a sub-property of `skos:inScheme` (S7) and `owl:inverseOf skos:hasTopConcept` (S8) ⟨§4⟩
- **[[skos]]** _(standard · normative)_ — There is no way to close the boundary of a concept scheme: SKOS can describe a scheme but provides no mechanism to completely define one, and a concept may take part in zero, one, or more schemes ⟨§4.6.1⟩

## Where sources differ

Among the ingested sources, only SKOS models the concept scheme as an explicit construct. No divergence to report.

## See also
[[controlled-vocabulary]] · [[concept-collection]] · [[semantic-relation]]
