---
title: "dcat:Catalog"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-catalog]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:Catalog

## What it is
The DCAT class representing a data catalog: a curated collection of metadata about resources such as datasets and data services. A Web-based data catalog is typically represented as a single instance of this class.

## Key facts
- Definition: "A curated collection of metadata about resources." ⟨§6.3⟩
- It is a sub-class of `dcat:Dataset`, so a catalog is itself a kind of dataset whose member items are descriptions of datasets and data services ⟨§6.3⟩
- Members are attached via `dcat:resource` and its sub-properties `dcat:dataset`, `dcat:service`, and `dcat:catalog` (allowing catalogs of catalogs) ⟨§6.3.3⟩
- Since DCAT 2 the class was generalized, with properties common to all cataloged resources moved to the super-class `dcat:Resource` ⟨§6.3⟩
- A catalog classifies its resources against a knowledge organization system linked with `dcat:themeTaxonomy` ⟨§6.3.2⟩

## Relations
- Realizes: [[data-catalog]]
- Defined in: [[dcat-3]]
- Related: [[dcat-resource]], [[dcat-dataset]], [[dcat-catalogrecord]]

## See also
[[data-catalog]] · [[dcat-dataset]]
