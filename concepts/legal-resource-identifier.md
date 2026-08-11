---
title: "Legal Resource Identifier"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[descriptive-metadata]]"]
updated: 2026-08-10
---

# Legal Resource Identifier

## What it is
A legal resource identifier is a standardized, persistent, location-independent scheme for naming legal resources — a piece of legislation or a court decision — usually paired with a minimum set of uniform metadata so the resource can be referenced, retrieved, and described consistently across systems and jurisdictions. Such identifiers commonly name resources at an abstract (work) level rather than a specific document file.

## How sources treat it
- **[[eli]]** _(standard · normative)_ — Pillar 1 (Identification): every legal text is assigned a universal resource identifier (URI) that lets users identify and access legislation consistently, usable in documents or published online ⟨Pillar 1⟩
- **[[eli]]** _(standard · normative)_ — Uses a common vocabulary to represent metadata about national and EU legislation and is designed for cross-border compatibility so legislation is interoperable across countries ⟨Key features⟩
- **[[ecli]]** _(standard · normative)_ — An identifier for court decisions in EU member states plus a minimum uniform metadata set; it identifies the court decision at an abstract level — in FRBR terminology a work-level identifier — and consists of five colon-separated parts (ECLI, country code, court code, year, unique code) ⟨Wikipedia, Identifier construction⟩
- **[[eli-akn-mapping]]** _(article · informational)_ — Frames ELI as an identifier + metadata ontology layer that can be mapped to the Akoma Ntoso document model, both anchored on FRBR-style abstraction, as a contribution to legal-ontology interoperability and Linked Open Data reuse ⟨general knowledge⟩

## Where sources differ
The sources cover identifiers for different legal resource kinds and are complementary. [[eli]] identifies and describes legislation via a four-pillar scheme (identification, description, publication, synchronisation); [[ecli]] identifies court decisions with a fixed five-part structure and a Dublin Core-based metadata set. Both name resources at an abstract FRBR work level. [[eli-akn-mapping]] positions the identifier layer as mappable to a document model, and is authored lightweight-from-knowledge with a note to verify specifics; [[ecli]] itself is drawn from a secondary Wikipedia summary whose primary source is the EU Council Conclusions.

## See also
[[descriptive-metadata]] · [[document-metadata-extraction]] · [[legislative-document-model]]
