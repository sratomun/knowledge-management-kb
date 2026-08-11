---
title: "Semantic relation"
type: concept
tags: [knowledge-organization]
related: ["[[concept-scheme]]", "[[scheme-mapping]]", "[[concept-collection]]"]
updated: 2026-08-09
---

# Semantic relation

## What it is

A semantic relation is a typed link between two concepts within a knowledge organization system. Such relations fall into two kinds: hierarchical links, which connect a broader concept to a narrower one, and associative links, which connect two related concepts without implying a hierarchy. These links are what turn a flat list of terms into a navigable structure.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — Semantic relations distinguish hierarchical (`skos:broader`/`skos:narrower`) from associative (`skos:related`) links; `skos:broader`/`skos:narrower` are, by convention, used only for direct (immediate) links and are deliberately **not** declared transitive ⟨§8.1⟩
- **[[skos]]** _(standard · normative)_ — `skos:semanticRelation` has domain and range `skos:Concept` (S19, S20); `skos:broaderTransitive`/`skos:narrowerTransitive`/`skos:related` are sub-properties of it (S21); `skos:broader` is a sub-property of `skos:broaderTransitive` (S22); `skos:related` is symmetric (S23); the transitive properties are `owl:TransitiveProperty` (S24) ⟨§8.3⟩
- **[[skos]]** _(standard · normative)_ — Semantic-relation integrity condition: "skos:related is disjoint with the property skos:broaderTransitive" (S27) — so hierarchical and associative links between the same pair clash ⟨§8.4⟩

## Where sources differ

Among the ingested sources, only SKOS defines semantic relations between concepts. No divergence to report.

## See also
[[concept-scheme]] · [[scheme-mapping]] · [[concept-collection]]
