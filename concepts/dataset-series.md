---
title: "Dataset Series"
type: concept
tags: [metadata]
related: ["[[dataset-description]]", "[[data-catalog]]", "[[catalog-record]]"]
updated: 2026-08-09
---

# Dataset Series

## What it is

A dataset series is a collection of datasets that are published separately but share common characteristics and belong together — for example the successive yearly or monthly editions of the same statistical release. It lets a catalog group related datasets under one identity while still describing each member on its own.

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — DCAT 3 added a `dcat:DatasetSeries` class and properties (`dcat:inSeries`, `dcat:seriesMember`, and ordering properties `dcat:first`/`dcat:last`/`dcat:prev`/`dcat:next`) for representing collections of datasets published separately but sharing characteristics ⟨Status, §6.7, §12⟩
- **[[dcat-3]]** _(standard · normative)_ — Dataset series is one of the seven main classes DCAT is built around and is treated in a dedicated section of the vocabulary ⟨§5.1, §6.7, §12⟩
- **[[dcat-3]]** _(standard · normative)_ — A conforming catalog MUST organize access to data into datasets, distributions, data services and dataset series ⟨§4⟩
- **[[dcat-3]]** _(standard · normative)_ — DCAT 3 is a major revision of DCAT 2 that adds versioning, dataset series, and checksum support while preserving backward compatibility ⟨Status⟩

## Where sources differ

Only DCAT-3 is cited here, so no cross-source divergence is recorded. Note that dataset series was introduced in DCAT 3 and is not present in DCAT 2; DCAT distinguishes the ordering/membership relations of a series from the version chains it also introduced in version 3.

## See also
[[dataset-description]] · [[data-catalog]] · [[catalog-record]]
