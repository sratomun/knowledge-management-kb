---
title: "dcat:accessURL"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-distribution]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:accessURL

## What it is
A DCAT property giving a URL of a resource that provides access to a distribution of a dataset — for example a landing page, feed, SPARQL endpoint, or other service or location, typically reached through a Web form, query or API call.

## Key facts
- Definition: "A URL of the resource that gives access to a distribution of the dataset. E.g., landing page, feed, SPARQL endpoint." ⟨§6.8.9⟩
- Domain is `dcat:Distribution`; range is `rdfs:Resource` ⟨§6.8.9⟩
- "dcat:accessURL SHOULD be used for the URL of a service or location that can provide access to this distribution, typically through a Web form, query or API call." ⟨§6.8.9⟩
- Where the access URL is a direct download, `dcat:downloadURL` SHOULD also be provided ⟨§6.8.9, §6.8.11⟩

## Relations
- Realizes: [[data-distribution]]
- Defined in: [[dcat-3]]
- Related: [[dcat-distribution]], [[dcat-downloadurl]]

## See also
[[data-distribution]] · [[dcat-downloadurl]]
