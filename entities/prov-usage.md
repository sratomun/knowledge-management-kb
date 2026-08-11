---
title: "prov:Usage"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[qualification-pattern]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:Usage

## What it is
A Qualified term: the influence class used to elaborate a prov:used relation between an Activity and an Entity.

## Key facts
- "to elaborate how an prov:Activity prov:used a particular prov:Entity, one creates an instance of prov:Usage that indicates the influencing entity with the prov:entity property." ⟨§3.3⟩
- The influenced Activity "indicates the prov:Usage with the property prov:qualifiedUsage." ⟨§3.3⟩
- "the time that the Activity used the Entity is provided using the prov:atTime property and a literal xsd:dateTime value." ⟨§3.3⟩

## Relations
- Realizes: [[qualification-pattern]]
- Defined in: [[prov-o]]
- Related: [[prov-used]], [[prov-influence]]

## See also
[[prov-used]] [[prov-influence]]
