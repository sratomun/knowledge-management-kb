---
title: "dcat:CatalogRecord"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[catalog-record]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:CatalogRecord

## What it is
The DCAT class for a metadata record describing the registration of a single resource in a catalog — capturing information about the catalog entry (such as who added it and when) as distinct from the described resource itself.

## Key facts
- Definition: "A record in a catalog, describing the registration of a single dcat:Resource." ⟨§6.5⟩
- The class is optional; it exists for catalogs that distinguish metadata about a dataset/service from metadata about the catalog entry ⟨§6.5⟩
- Where a resource's publication date and its catalog-entry date differ, or only the latter is known, the publication date SHOULD only be specified for the catalog record ⟨§6.5⟩
- The described resource is linked with `foaf:primaryTopic`; the catalog attaches records via `dcat:record` ⟨§6.5.5, §6.3.7⟩
- The W3C PROV Ontology [PROV-O] can add further provenance about the process and agent involved in a change to a resource or its registration ⟨§6.5⟩

## Relations
- Realizes: [[catalog-record]]
- Defined in: [[dcat-3]]
- Related: [[dcat-catalog]], [[dcat-resource]]

## See also
[[catalog-record]] · [[dcat-catalog]]
