---
title: "prov:Generation"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[qualification-pattern]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:Generation

## What it is
A Qualified term: the influence class used to elaborate a prov:wasGeneratedBy relation between an Entity and an Activity.

## Key facts
- Qualifies prov:wasGeneratedBy: an Entity uses prov:qualifiedGeneration to point at a prov:Generation, whose influencing Activity is cited with prov:activity. ⟨§3.3 Table 2⟩
- "The instance of prov:Generation cites the time ... that the activity ... generated the chart," provided via prov:atTime. ⟨§3.3⟩
- prov:Generation is among the prov:InstantaneousEvent subclasses describable with prov:atTime. ⟨§3.3⟩

## Relations
- Realizes: [[qualification-pattern]]
- Defined in: [[prov-o]]
- Related: [[prov-wasgeneratedby]], [[prov-influence]]

## See also
[[prov-wasgeneratedby]] [[prov-influence]]
