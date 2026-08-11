---
title: "prov:wasDerivedFrom"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[derivation]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:wasDerivedFrom

## What it is
A Starting Point object property relating one Entity to another Entity from which it was derived.

## Key facts
- "Provenance chains comprising only Entities can be formed using the prov:wasDerivedFrom property. A derivation is a transformation of one entity into another." ⟨§3.1⟩
- Three subproperties are provided for certain kinds of derivation: prov:wasQuotedFrom, prov:wasRevisionOf, and prov:hadPrimarySource. ⟨§3.2⟩
- Can be qualified with prov:qualifiedDerivation and the class prov:Derivation, citing the influencing Entity with prov:entity. ⟨§3.3 Table 2⟩

## Relations
- Realizes: [[derivation]]
- Defined in: [[prov-o]]
- Related: [[prov-derivation]], [[prov-wasrevisionof]], [[prov-wasquotedfrom]], [[prov-hadprimarysource]]

## See also
[[prov-entity]] [[prov-derivation]]
