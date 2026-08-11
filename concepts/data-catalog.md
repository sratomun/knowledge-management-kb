---
title: "Data Catalog"
type: concept
tags: [metadata]
related: ["[[dataset-description]]", "[[data-distribution]]", "[[data-service]]", "[[dataset-series]]", "[[catalog-record]]", "[[data-product]]", "[[metadata-management]]"]
updated: 2026-08-09
---

# Data Catalog

## What it is

A data catalog is a curated collection of descriptions of data assets — datasets, the services and files that deliver them, and the metadata that lets people and machines discover, evaluate, and access those assets. It is the inventory-and-index layer over an organization's (or the Web's) data, meant to make otherwise scattered data findable and comparable.

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — Defines a `dcat:Catalog` class for a curated collection of metadata about resources; DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs and to enable federated search across catalogs ⟨Abstract⟩
- **[[dcat-3]]** _(standard · normative)_ — A conforming catalog MUST organize access to data into datasets, distributions, data services and dataset series, and an RDF description of the catalog, its cataloged resources and distributions MUST be available ⟨§4⟩
- **[[dcat-3]]** _(standard · normative)_ — Builds the catalog around seven main classes: `dcat:Catalog`, `dcat:Resource`, `dcat:Dataset`, `dcat:Distribution`, `dcat:DataService`, `dcat:DatasetSeries`, and `dcat:CatalogRecord` ⟨§5.1⟩
- **[[dcat-3]]** _(standard · normative)_ — It does not prescribe any particular method of deploying catalogs, syntax, access protocol, or access policy ⟨§1, §4⟩
- **[[dama-dmbok2]]** _(whitepaper · informational)_ — Positions the discipline that produces and maintains catalogs — Metadata Management — as a distinct knowledge area underpinning trust and usability across the other functions ⟨DAMA Wheel⟩

## Where sources differ

DCAT-3 gives a concrete, normative RDF class model with explicit conformance requirements (what a catalog MUST contain) while deliberately staying silent on deployment, protocol, and policy. DAMA-DMBOK2 does not supply a vocabulary at all; it locates cataloging within the broader Metadata Management knowledge area as an organizational practice rather than a machine-readable model. The two operate at different levels: one specifies an interoperability format, the other a management discipline.

## See also
[[dataset-description]] · [[data-distribution]] · [[metadata-management]] · [[data-product]]
