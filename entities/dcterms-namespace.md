---
title: "DCMI /terms/ namespace"
type: entity
subtype: vocabulary-term
aliases: ["dcterms:"]
tags: [metadata]
concepts: ["[[descriptive-metadata]]"]
sources: ["[[dcmi-terms]]"]
updated: 2026-08-09
---

# DCMI /terms/ namespace

## What it is
The DCMI namespace holding the full set of DCMI metadata terms, including the fifteen core elements mirrored with formal semantic constraints.

## Key facts
- Base URI `http://purl.org/dc/terms/`; originally created in 2001 for terms coined outside the original fifteen-element Dublin Core. ⟨§1⟩
- In 2008 the original fifteen elements were mirrored here with formal constraints, so `dcterms:date` has a formal range of "literal" while `dc:date` has none; most users can treat the parallel properties as equivalent. ⟨§1⟩
- The most useful properties and classes have been published as ISO 15836-2:2019; DCMI gently encourages use of this namespace. ⟨§1⟩

## Relations
- Realizes: [[descriptive-metadata]]
- Defined in: [[dcmi-terms]]
- Related: [[dc-elements-namespace]]

## See also
[[iso-15836-2-2019]] · [[dcam-namespace]]
