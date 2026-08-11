---
title: "Provenance"
type: concept
aliases: []
tags: [governance]
related: ["[[provenance-influence]]", "[[derivation]]", "[[qualification-pattern]]", "[[data-governance]]", "[[metadata-management]]"]
updated: 2026-08-09
---

# Provenance

## What it is
Provenance is the record of where a thing came from and how it came to be: the entities, activities, and agents involved in producing, delivering, or otherwise influencing a resource. In data work it supports trust, reproducibility, attribution, and lineage — answering who made this, from what, when, and how.

## How sources treat it
- **[[prov-o]]** _(standard · normative)_ — PROV-O expresses the PROV Data Model in OWL2, providing classes, properties, and restrictions to represent and interchange provenance information generated in different systems and under different contexts ⟨Abstract⟩.
- **[[prov-o]]** _(standard · normative)_ — Provenance is built on three starting-point classes — `prov:Entity`, `prov:Activity`, `prov:Agent` — where an Agent bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity ⟨§3.1⟩.
- **[[prov-o]]** _(standard · normative)_ — Provenance chains can be formed from Entities alone via `prov:wasDerivedFrom`, or from Activities alone via `prov:wasInformedBy`, which provides dependency information without stating start and end times ⟨§3.1⟩.
- **[[dcat-3]]** _(standard · normative)_ — Qualified attribution (`prov:qualifiedAttribution`) and qualified relations (`dcat:qualifiedRelation` with `dcat:Relationship`/`dcat:hadRole`) let the role of a related agent or resource be characterized where a simple property is insufficient ⟨§6.4.18, §15⟩.
- **[[dama-dmbok2]]** _(whitepaper · informational)_ — DMBOK2 situates lineage and trust within the Metadata Management and Data Quality knowledge areas, which it treats as underpinning trust and usability across the other functions, coordinated by Data Governance at the hub ⟨DAMA Wheel⟩.

## Where sources differ
PROV-O is a formal RDF/OWL ontology that models provenance as a graph of entities, activities, and agents for machine interchange; DCAT reuses PROV terms narrowly, mainly to attribute agents and characterize relationships on catalog resources; and DAMA-DMBOK2 addresses provenance only indirectly, as an organizational concern folded into Metadata Management, Data Quality, and Data Governance rather than a modeled vocabulary. PROV-O and DCAT are normative standards; DMBOK2 is an explicitly non-prescriptive body of knowledge whose points here come from a secondary source ⟨dama.org⟩.

## See also
[[provenance-influence]] · [[derivation]] · [[qualification-pattern]] · [[data-governance]] · [[metadata-management]]
