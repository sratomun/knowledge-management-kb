---
title: "Descriptive metadata"
type: concept
aliases: []
tags: [metadata]
related: ["[[application-profile]]", "[[vocabulary-encoding-scheme]]", "[[syntax-encoding-scheme]]", "[[metadata-registry]]", "[[dataset-description]]"]
updated: 2026-08-09
---

# Descriptive metadata

## What it is
Descriptive metadata is structured information that describes a resource — attributes such as its title, creator, subject, date, format, and language — so the resource can be discovered, identified, and interpreted independently of how or where it is physically stored. It is the layer of "data about data" aimed primarily at resource discovery and understanding across heterogeneous systems.

## How sources treat it
- **[[dcmi-terms]]** _(standard · normative)_ — Bundles the fifteen-element Dublin Core plus "several dozen properties, classes, datatypes, and vocabulary encoding schemes," collectively "DCMI metadata terms," and standardizes descriptive metadata for resource discovery across heterogeneous systems ⟨§1 Introduction⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — Terms are expressed in RDF vocabularies for use in Linked Data; non-RDF users may disregard the RDF-specific implications and rely on the natural-language definitions ⟨§1 Introduction⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — The /terms/ namespace defines around 55 properties, including 40+ beyond the core fifteen (e.g. abstract, created, modified, issued, license, provenance, spatial, temporal) ⟨§2 Properties in /terms/⟩.
- **[[dcat-3]]** _(standard · normative)_ — Enables a publisher to describe datasets and data services in a catalog using a standard model and vocabulary, facilitating consumption and aggregation of metadata from multiple catalogs and federated search ⟨Abstract, §1⟩.
- **[[dcat-3]]** _(standard · normative)_ — A conforming catalog MUST organize access to data into datasets, distributions, data services and dataset series, and an RDF description of the catalog, its cataloged resources and distributions MUST be available ⟨§4⟩.
- **[[iso-iec-11179-1]]** _(standard · normative)_ — The standard has two main purposes: definition (semantically precise description of data independent of physical storage) and exchange (making data understandable and shareable) ⟨Wikipedia: ISO/IEC 11179⟩.
- **[[iso-iec-11179-1]]** _(standard · normative)_ — Its constructs are semantic, not physical or technical: the standard does not describe how data is actually stored in physical files, tables, or columns ⟨Wikipedia: ISO/IEC 11179⟩.

## Where sources differ
DCMI Terms and DCAT both express descriptive metadata as RDF vocabularies aimed at Web and Linked Data discovery, while ISO/IEC 11179 frames description as registered, semantically precise data-element definitions in a registry, agnostic to any particular serialization. The three also differ in the unit described: DCMI targets resources of any genre, DCAT scopes description to datasets and data services, and 11179 targets data elements. DCMI treats its RDF domain/range relations as optional for non-RDF users; DCAT requires an RDF description of a conforming catalog ⟨§4⟩.

## See also
[[application-profile]] · [[vocabulary-encoding-scheme]] · [[syntax-encoding-scheme]] · [[metadata-registry]] · [[dataset-description]]
