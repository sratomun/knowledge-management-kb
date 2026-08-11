---
title: "Derivation"
type: concept
aliases: []
tags: [governance]
related: ["[[provenance]]", "[[provenance-influence]]", "[[qualification-pattern]]"]
updated: 2026-08-09
---

# Derivation

## What it is
Derivation is the provenance relation between two entities where one is a transformation, construction, update, or other outcome built from the other. It captures the "made from" link that lets a resource's lineage be traced back through the earlier resources it came from, entity by entity.

## How sources treat it
- **[[prov-o]]** _(standard · normative)_ — A derivation is a transformation of one entity into another; provenance chains comprising only Entities can be formed using `prov:wasDerivedFrom` ⟨§3.1⟩.
- **[[prov-o]]** _(standard · normative)_ — `prov:wasQuotedFrom` cites a potentially larger Entity from which a new Entity was created by repeating some or all of the original ⟨§3.2⟩.
- **[[prov-o]]** _(standard · normative)_ — `prov:wasRevisionOf` indicates the derived Entity contains substantial content from the original, and `prov:hadPrimarySource` cites a preceding Entity produced by an agent with direct experience and knowledge about the topic ⟨§3.2⟩.
- **[[prov-o]]** _(standard · normative)_ — Derivation is distinct from the abstraction links `prov:specializationOf` (a more specific Entity to a more general one) and `prov:alternateOf` (Entities presenting aspects of the same thing), which relate views of a thing rather than one entity produced from another ⟨§3.2⟩.

## Where sources differ
Only PROV-O is sourced for this concept, so there is no cross-source divergence to report. PROV-O itself layers three named derivation subproperties — `prov:wasQuotedFrom`, `prov:wasRevisionOf`, `prov:hadPrimarySource` — beneath the general `prov:wasDerivedFrom`, each carrying a more specific meaning ⟨§3.2⟩.

## See also
[[provenance]] · [[provenance-influence]] · [[qualification-pattern]]
