---
title: "Metadata Management"
type: concept
tags: [metadata]
related: ["[[data-management]]", "[[data-catalog]]", "[[data-governance]]"]
updated: 2026-08-09
---

# Metadata Management

## What it is

Metadata management is the practice of planning, creating, storing, and controlling the data that describes other data — definitions, structures, lineage, ownership, and meaning — so that data assets are understandable, discoverable, and usable across systems and organizations. It is what makes data self-explaining and shareable rather than opaque.

## How sources treat it

- **[[dama-dmbok2]]** _(whitepaper · informational)_ — Treats Metadata Management as one of the ten knowledge areas surrounding Data Governance on the DAMA Wheel ⟨DAMA Wheel⟩
- **[[dama-dmbok2]]** _(whitepaper · informational)_ — Metadata Management and Data Quality are treated as distinct knowledge areas underpinning trust and usability across the other functions ⟨DAMA Wheel⟩
- **[[iso-iec-11179-1]]** _(standard · normative)_ — Is the international standard for representing an organization's metadata in a metadata registry (MDR); it documents the standardization and registration of metadata so that data becomes understandable and shareable across systems and organizations ⟨Wikipedia: ISO/IEC 11179⟩
- **[[iso-iec-11179-1]]** _(standard · normative)_ — Serves two main purposes — definition (semantically precise description of data independent of physical storage) and exchange (making data understandable and shareable) ⟨Wikipedia: ISO/IEC 11179⟩
- **[[iso-iec-11179-1]]** _(standard · normative)_ — Its constructs are semantic, not physical/technical: the standard does not describe how data is actually stored (physical files, tables, columns) ⟨Wikipedia: ISO/IEC 11179⟩

## Where sources differ

The two sources sit at different altitudes. DAMA-DMBOK2 treats metadata management as an organizational knowledge area — a management practice, described through goals, activities, roles, and metrics — without specifying a metamodel. ISO/IEC 11179 supplies exactly that missing layer: a normative, semantic metamodel for a metadata registry, focused on precisely defining and registering data elements independent of physical storage. One frames the management discipline; the other specifies the registry mechanics that a discipline might use.

## See also
[[data-management]] · [[data-catalog]] · [[data-governance]]
