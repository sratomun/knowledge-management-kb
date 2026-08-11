---
title: "Concept collection"
type: concept
tags: [knowledge-organization]
related: ["[[concept-scheme]]", "[[semantic-relation]]"]
updated: 2026-08-09
---

# Concept collection

## What it is

A concept collection is a labeled, and optionally ordered, grouping of concepts within a knowledge organization system — for example a set of sibling concepts gathered under a guide term or "node label" in a thesaurus. The collection is a grouping device: it is not itself a concept, and it does not stand as a broader term over its members.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — Collections: `skos:Collection` and `skos:OrderedCollection` are each `owl:Class` (S28), `OrderedCollection` a sub-class of `Collection` (S29); `skos:memberList` is an `owl:FunctionalProperty` (S35) with range `rdf:List` (S34); integrity condition S37 — `skos:Collection` is disjoint with each of `skos:Concept` and `skos:ConceptScheme` ⟨§9⟩

## Where sources differ

Among the ingested sources, only SKOS defines concept collections. No divergence to report.

## See also
[[concept-scheme]] · [[semantic-relation]]
