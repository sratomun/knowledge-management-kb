---
title: "prov:wasGeneratedBy"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[provenance-influence]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:wasGeneratedBy

## What it is
A Starting Point object property relating an Entity to the Activity that generated it.

## Key facts
- Activities can generate entities, "described with prov:used and prov:wasGeneratedBy, respectively." ⟨§3.1⟩
- "prov:generated ... [is] the inverse of prov:wasGeneratedBy." ⟨§3.2⟩
- Can be qualified with prov:qualifiedGeneration and the class prov:Generation, whose influencing Activity is cited with prov:activity. ⟨§3.3 Table 2⟩

## Relations
- Realizes: [[provenance-influence]]
- Defined in: [[prov-o]]
- Related: [[prov-generation]], [[prov-used]]

## See also
[[prov-entity]] [[prov-activity]] [[prov-generation]]
