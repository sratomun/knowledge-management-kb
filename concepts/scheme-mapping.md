---
title: "Scheme mapping"
type: concept
tags: [knowledge-organization]
related: ["[[semantic-relation]]", "[[concept-scheme]]", "[[controlled-vocabulary]]"]
updated: 2026-08-09
---

# Scheme mapping

## What it is

Scheme mapping is the act of asserting correspondences between concepts that belong to different concept schemes — for instance stating that a concept in one thesaurus exactly matches, is broader than, or is merely close to a concept in another. It lets separately maintained controlled vocabularies be aligned and traversed together without merging them.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — Mapping properties (`skos:closeMatch`, `skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) link concepts across schemes; all are sub-properties of `skos:mappingRelation`, itself a sub-property of `skos:semanticRelation` (S39, S40); `skos:exactMatch` is transitive and a sub-property of `skos:closeMatch` (S45, S42), while `skos:closeMatch` is deliberately **not** transitive to avoid compound errors ⟨§10⟩
- **[[skos]]** _(standard · normative)_ — Mapping integrity condition S46: "skos:exactMatch is disjoint with each of the properties skos:broadMatch and skos:relatedMatch" ⟨§10.4⟩

## Where sources differ

Among the ingested sources, only SKOS defines mapping between concept schemes. No divergence to report.

## See also
[[semantic-relation]] · [[concept-scheme]] · [[controlled-vocabulary]]
