---
title: "dcat:downloadURL"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-distribution]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:downloadURL

## What it is
A DCAT property giving the URL of a downloadable file that is a direct link to a distribution in a given format, typically retrieved through an HTTP GET request.

## Key facts
- Definition: "The URL of the downloadable file in a given format. E.g., CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType." ⟨§6.8.11⟩
- Domain is `dcat:Distribution`; range is `rdfs:Resource` ⟨§6.8.11⟩
- "dcat:downloadURL SHOULD be used for the URL at which this distribution is available directly, typically through a HTTP Get request." ⟨§6.8.11⟩
- It is distinct from `dcat:accessURL`, which is used for a service or location giving access when a direct download is not appropriate ⟨§6.8.9, §6.8.11⟩

## Relations
- Realizes: [[data-distribution]]
- Defined in: [[dcat-3]]
- Related: [[dcat-distribution]], [[dcat-accessurl]]

## See also
[[data-distribution]] · [[dcat-accessurl]]
