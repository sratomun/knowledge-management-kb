---
title: "dcat:Dataset"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[dataset-description]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:Dataset

## What it is
The DCAT class for a dataset: a collection of data, published or curated by a single agent, treated as a conceptual entity that can be represented by one or more distributions.

## Key facts
- Definition: "A collection of data, published or curated by a single agent, and available for access or download in one or more representations." ⟨§6.6⟩
- It is a sub-class of `dcat:Resource` ⟨§6.6⟩
- A dataset is a conceptual entity distinct from its distributions; DCAT does not make assumptions about serialization formats but distinguishes the abstract dataset from its manifestations ⟨§1, §5.1⟩
- The notion of dataset is broad and inclusive — data may be numbers, text, pixels, imagery, sound and other multi-media ⟨§5.1⟩
- The DCAT 1 sub-class relationship to `dctype:Dataset` was removed in DCAT 2 because the scope also includes other DCMI Types such as imagery, sound and text ⟨§6.6⟩
- Distributions are attached with `dcat:distribution`; membership in a series with `dcat:inSeries` ⟨§6.6.1, §6.6.3⟩

## Relations
- Realizes: [[dataset-description]]
- Defined in: [[dcat-3]]
- Related: [[dcat-distribution]], [[dcat-datasetseries]], [[dcat-catalog]]

## See also
[[dataset-description]] · [[dcat-distribution]]
