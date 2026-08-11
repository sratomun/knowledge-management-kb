---
title: "dcat:DataService"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-service]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# dcat:DataService

## What it is
The DCAT class for a data service: a collection of operations, accessible through an interface (API), that provide access to one or more datasets or data processing functions. It was added in DCAT 2.

## Key facts
- Definition: "A collection of operations that provides access to one or more datasets or data processing functions." ⟨§6.9⟩
- It is a sub-class of `dcat:Resource`; the class was added in DCAT 2 ⟨§6.9⟩
- The primary endpoint is given by `dcat:endpointURL` and machine-readable operation details by `dcat:endpointDescription` ⟨§6.9.1, §6.9.2⟩
- Datasets that the service can distribute are linked with `dcat:servesDataset` ⟨§6.9.3⟩
- Data service subtypes include data distribution, discovery, transformation and processing services; to extend beyond data distribution services it is recommended to define sub-classes in a profile ⟨§5.1⟩
- A distribution can reference a service via `dcat:accessService`, whose `dcat:accessURL` corresponds with the service's `dcat:endpointURL` ⟨§5.9⟩

## Relations
- Realizes: [[data-service]]
- Defined in: [[dcat-3]]
- Related: [[dcat-endpointurl]], [[dcat-distribution]], [[dcat-dataset]]

## See also
[[data-service]] · [[dcat-endpointurl]]
