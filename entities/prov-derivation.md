---
title: "prov:Derivation"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[qualification-pattern]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:Derivation

## What it is
A Qualified term: the influence class used to elaborate a prov:wasDerivedFrom relation between two Entities.

## Key facts
- Qualifies prov:wasDerivedFrom: an Entity uses prov:qualifiedDerivation to point at a prov:Derivation, citing the influencing Entity with prov:entity. ⟨§3.3 Table 2⟩
- "The instance of prov:Derivation cites the activity ... and the Usages and Generations that the activity conduced to create" the derived Entity. ⟨§3.3⟩
- A prov:Derivation instance may carry prov:hadActivity, prov:hadUsage, and prov:hadGeneration. ⟨§3.3⟩

## Relations
- Realizes: [[qualification-pattern]]
- Defined in: [[prov-o]]
- Related: [[prov-wasderivedfrom]], [[prov-influence]]

## See also
[[prov-wasderivedfrom]] [[prov-influence]] [[derivation]]
