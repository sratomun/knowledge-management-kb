---
title: "Catalog Record"
type: concept
tags: [metadata]
related: ["[[data-catalog]]", "[[dataset-description]]"]
updated: 2026-08-09
---

# Catalog Record

## What it is

A catalog record is metadata about an entry in a catalog — the registration information for a resource, such as who added it and when — as opposed to metadata about the resource itself. It separates "when the dataset was published" from "when the dataset was listed in this catalog."

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — `dcat:CatalogRecord` represents a metadata record in the catalog, primarily concerning the registration information, such as who added the record and when ⟨§6.5⟩
- **[[dcat-3]]** _(standard · normative)_ — While `dcat:Resource` represents the dataset or service itself, `dcat:CatalogRecord` is the record that describes the registration of a resource in the catalog; its use is considered optional and can be safely ignored if provenance about entries is not needed ⟨§5.6, §6.5⟩
- **[[dcat-3]]** _(standard · normative)_ — Where the publication date of a dataset and of its catalog entry differ, or only the latter is known, the publication date SHOULD only be specified for the catalog record ⟨§6.5⟩
- **[[dcat-3]]** _(standard · normative)_ — If a catalog is represented as an RDF Dataset with named graphs, the description of each dataset (its `dcat:Dataset`, `dcat:CatalogRecord`, and distributions) SHOULD be placed in a separate named graph whose name is the IRI of the catalog record ⟨§6.5⟩

## Where sources differ

Only DCAT-3 is cited here, so no cross-source divergence is recorded. DCAT itself frames the catalog record as an optional layer: the same registration provenance may alternatively be expressed with the W3C PROV Ontology, and catalogs that do not distinguish resource metadata from entry metadata may omit it entirely.

## See also
[[data-catalog]] · [[dataset-description]]
