---
title: "dcat:endpointURL"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-service]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:endpointURL

## What it is
A DCAT property giving the root location or primary endpoint of a data service — the Web-resolvable IRI at which the service is reached.

## Key facts
- Definition: "The root location or primary endpoint of the service (a Web-resolvable IRI)." ⟨§6.9.1⟩
- Domain is `dcat:DataService`; range is `rdfs:Resource` ⟨§6.9.1⟩
- It is complemented by `dcat:endpointDescription`, which describes the operations and parameters available via the endpoints ⟨§6.9.2⟩
- For an API-backed distribution, the `dcat:accessURL` corresponds with the `dcat:endpointURL` of the serving service ⟨§5.9⟩

## Relations
- Realizes: [[data-service]]
- Defined in: [[dcat-3]]
- Related: [[dcat-dataservice]]

## See also
[[data-service]] · [[dcat-dataservice]]
