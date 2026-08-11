---
title: "Data Service"
type: concept
tags: [metadata]
related: ["[[dataset-description]]", "[[data-distribution]]", "[[data-catalog]]"]
updated: 2026-08-09
---

# Data Service

## What it is

A data service is an operational interface — typically an API or endpoint — through which data can be accessed or processed, as distinct from a static file. It describes a running capability that serves one or more datasets or performs data-processing functions on request.

## How sources treat it

- **[[dcat-3]]** _(standard · normative)_ — `dcat:DataService` represents a collection of operations accessible through an interface (API) providing access to one or more datasets or data processing functions ⟨§5.1, §6.9⟩
- **[[dcat-3]]** _(standard · normative)_ — A data service's root endpoint is given by `dcat:endpointURL`, and `dcat:servesDataset` links it to the datasets it serves ⟨§5.1, §6.9⟩
- **[[dcat-3]]** _(standard · normative)_ — `dcat:Resource` is the parent class of `dcat:Dataset`, `dcat:DataService` and `dcat:Catalog`; it is an extension point for defining a catalog of any kind of resources and is not intended to be used directly ⟨§5.1⟩
- **[[dcat-3]]** _(standard · normative)_ — A conforming catalog MUST organize access to data into datasets, distributions, data services and dataset series ⟨§4⟩

## Where sources differ

Only DCAT-3 is cited here, so no cross-source divergence is recorded. Within DCAT, a data service is distinguished from a distribution: the service is an operational interface (identified by an endpoint that serves datasets), whereas a distribution is a concrete downloadable or accessible serialization of a dataset.

## See also
[[dataset-description]] · [[data-distribution]] · [[data-catalog]]
