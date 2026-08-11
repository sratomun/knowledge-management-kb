---
title: "dcat:Distribution"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-distribution]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:Distribution

## What it is
The DCAT class for a specific, accessible representation of a dataset, such as a downloadable file or an API-served form. A single dataset may have multiple distributions.

## Key facts
- Definition: "A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways, including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or profiles." ⟨§6.8⟩
- Access is expressed via `dcat:accessURL` (a location that gives access) and/or `dcat:downloadURL` (a direct download link); an API-backed distribution links to a `dcat:DataService` via `dcat:accessService` ⟨§6.8.9, §6.8.11, §6.8.10⟩
- Format is described with `dcat:mediaType` and/or `dcterms:format`, with size in `dcat:byteSize` ⟨§6.8.16, §6.8.17, §6.8.12⟩
- DCAT 3 added `spdx:checksum` linking a distribution to an `spdx:Checksum` digest ⟨§6.8.20⟩
- In many actual catalogs distributions are represented as blank nodes nested inside the dataset, though global identifiers are recommended ⟨§5.2⟩

## Relations
- Realizes: [[data-distribution]]
- Defined in: [[dcat-3]]
- Related: [[dcat-dataset]], [[dcat-accessurl]], [[dcat-downloadurl]], [[dcat-checksum]], [[dcat-dataservice]]

## See also
[[data-distribution]] · [[dcat-dataset]]
