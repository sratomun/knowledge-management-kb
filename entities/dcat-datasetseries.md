---
title: "dcat:DatasetSeries"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[dataset-series]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:DatasetSeries

## What it is
The DCAT class, added in DCAT 3, for a dataset series: a collection of datasets that are published separately but share characteristics that group them (for example successive yearly editions of a budget dataset).

## Key facts
- Definition: "A collection of datasets that are published separately, but share some characteristics that group them." ⟨§6.7⟩
- It is a sub-class of `dcat:Dataset`; the class was added in DCAT 3 ⟨§6.7⟩
- A dataset declares membership with `dcat:inSeries` (inverse `dcat:seriesMember`); ordering among members uses `dcat:first`, `dcat:last`, `dcat:prev`, `dcat:next` ⟨§6.6.3, §7, §6.4.31⟩
- Some series properties reflect child-dataset dimensions via upstream inheritance — e.g. the series' temporal or spatial coverage is the union of those of its child datasets ⟨§12.2⟩

## Relations
- Realizes: [[dataset-series]]
- Defined in: [[dcat-3]]
- Related: [[dcat-dataset]], [[dcat-catalog]]

## See also
[[dataset-series]] · [[dcat-dataset]]
