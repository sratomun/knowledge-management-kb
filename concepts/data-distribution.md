---
title: "Data Distribution"
type: concept
tags: [metadata]
related: ["[[dataset-description]]", "[[data-service]]", "[[data-catalog]]", "[[dataset-series]]"]
updated: 2026-08-09
---

# Data Distribution

## What it is

A distribution is a specific, accessible form of a dataset — for example a downloadable CSV file, an Excel workbook, or an RDF dump. One dataset may have many distributions, each representing the same data in a different format or delivered through a different mechanism.

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — `dcat:Distribution` represents an accessible form of a dataset such as a downloadable file; a dataset may be available in many distributions differing in format or access mechanism ⟨§5.1⟩
- **[[dcat-3]]** _(standard · normative)_ — `dcat:accessURL` gives a location that gives access to a distribution, while `dcat:downloadURL` is used for a direct, downloadable distribution ⟨§6.8.9, §6.8.11⟩
- **[[dcat-3]]** _(standard · normative)_ — DCAT 3 added the `spdx:checksum` property and `spdx:Checksum` class (with `spdx:algorithm` and `spdx:checksumValue`) to provide a digest for DCAT distributions ⟨Status, §6.8.20, §6.17⟩
- **[[dcat-3]]** _(standard · normative)_ — Where possible, DCAT properties do not have specified domains, to leave the property open for reuse with any kind of resource ⟨§6.1⟩

## Where sources differ

Only DCAT-3 is cited here, so no cross-source divergence is recorded. Within DCAT, a distinction is drawn between a distribution reached indirectly via an `dcat:accessURL` (a landing point, service, or page) and one fetched directly via a `dcat:downloadURL`; a distribution differs from a data service in that it is a concrete serialized form rather than an operational interface.

## See also
[[dataset-description]] · [[data-service]] · [[data-catalog]]
