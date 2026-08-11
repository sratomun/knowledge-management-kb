---
title: "dcat:Resource"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-catalog]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:Resource

## What it is
The abstract DCAT class for any resource that may be described by a metadata record in a catalog. It is the parent class of `dcat:Dataset`, `dcat:DataService` and `dcat:Catalog`, and serves as the extension point for cataloging other kinds of resource.

## Key facts
- Definition: "Resource published or curated by a single agent." ⟨§6.4⟩
- It is the parent class of `dcat:Dataset`, `dcat:DataService` and `dcat:Catalog`; it is not intended to be used directly ⟨§5.1⟩
- "dcat:Resource is actually an extension point for defining a catalog of any kind of resources"; to extend catalog scope, additional sub-classes SHOULD be defined in a DCAT profile or application ⟨§5.1⟩
- Common cross-cutting properties (access rights, contact point, creator, publisher, keyword, license, versioning, qualified relation/attribution) are declared on this super-class and inherited by its sub-classes ⟨§6.4⟩

## Relations
- Realizes: [[data-catalog]]
- Defined in: [[dcat-3]]
- Related: [[dcat-catalog]], [[dcat-dataset]], [[dcat-dataservice]]

## See also
[[data-catalog]] · [[dcat-dataset]]
