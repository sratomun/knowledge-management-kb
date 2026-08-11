---
title: "Dataset Description"
type: concept
tags: [metadata]
related: ["[[data-catalog]]", "[[data-distribution]]", "[[data-service]]", "[[dataset-series]]", "[[catalog-record]]", "[[data-product]]"]
updated: 2026-08-09
---

# Dataset Description

## What it is

A dataset description is the metadata that identifies and characterizes a dataset — what it is, who published it, what it covers, and how it can be obtained — as a conceptual entity separate from any particular file or download that carries its contents.

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — Defines a dataset as a "collection of data, published or curated by a single agent, and available for access or download in one or more serializations or formats"; a dataset is a conceptual entity distinct from its distributions ⟨§5.1⟩
- **[[dcat-3]]** _(standard · normative)_ — Models the dataset with the `dcat:Dataset` class and describes its properties (title, distributions, and related metadata) in the vocabulary specification ⟨§6.6⟩
- **[[dcat-3]]** _(standard · normative)_ — Incorporates terms from pre-existing vocabularies (e.g., `foaf:homepage`, `dcterms:title`) for describing datasets; definitions of terms outside the DCAT namespace are provided for convenience and MUST NOT be considered normative ⟨External terms, §6.2.2⟩
- **[[dcat-3]]** _(standard · normative)_ — It is recommended that instances of the DCAT main classes have a global identifier (IRI); use of blank nodes is generally discouraged when encoding DCAT in RDF ⟨§5.2⟩

## Where sources differ

Only DCAT-3 is cited here, so no cross-source divergence is recorded. Within DCAT, note the deliberate separation the vocabulary insists on: the dataset (a conceptual entity) is described independently of its distributions (the concrete files or endpoints that serve it) and independently of the catalog record (the registration entry about it).

## See also
[[data-catalog]] · [[data-distribution]] · [[data-service]] · [[catalog-record]]
