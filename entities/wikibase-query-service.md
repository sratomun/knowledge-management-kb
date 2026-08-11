---
title: "Wikibase Query Service"
type: entity
subtype: system
aliases: ["wikibase-query-service"]
tags: [semantic-wiki]
concepts: ["[[linked-open-data]]"]
sources: ["[[wikibase]]"]
updated: 2026-08-10
---

# Wikibase Query Service

## What it is
The Wikibase query service is the component that lets users query the data held in a
Wikibase knowledge base. It uses SPARQL and, together with federation, supports
accessing and referencing data across Wikibase instances as part of the Linked Open
Data web.

## Key facts
- Wikibase provides a query service, which uses SPARQL, for querying the data in a Wikibase ⟨wikibase: docs-hub/Managing data⟩.
- In a federated setup data stays where it is created but can still be accessed and referenced from other Wikibases ⟨wikibase: homepage/nutshell — Federation⟩.
- Wikibase is designed to open up structured data as reusable Linked Open Data for both computers and human audiences in their own language ⟨wikibase: docs-hub/overview⟩.
- Showcase deployments expose SPARQL endpoints and use federated queries to link to external resources such as Wikidata (e.g. MiMoTextBase, MARDI's KG Query Service) ⟨wikibase: homepage/Showcases⟩.
- The MediaWiki documentation covers using the query service and running it as part of the Wikibase reference material [gen: presence of run/use query-service docs noted on the docs hub, not detailed on the homepage] ⟨wikibase: docs-hub/Reference⟩.
- Wikibase is free, open-source software made and supported by Wikimedia Deutschland, which also hosts the Wikibase Cloud SaaS offering ⟨wikibase: docs-hub/overview · homepage⟩.

## Relations
- Realizes: [[linked-open-data]]
- Defined in: [[wikibase]]
- Related: [[org-wikimedia-de]]
- Related: [[wikibase-item]]

## See also
[[linked-open-data]] · [[structured-knowledge-base]]
