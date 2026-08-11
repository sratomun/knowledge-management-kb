---
title: "Structured Knowledge Base"
type: concept
subtype: system-class
aliases: []
tags: [semantic-wiki]
related: ["[[semantic-wiki]]", "[[entity-data-model]]", "[[linked-open-data]]"]
updated: 2026-08-10
---

# Structured Knowledge Base

## What it is

A structured knowledge base stores knowledge as discrete, machine-readable data — entities with typed properties and statements — rather than as free text, so that both people and software can pool, edit, query, and reuse it. The structure is what distinguishes it from a document store: content is modeled as data with explicit relationships, enabling querying and export instead of only reading.

## How sources treat it

- **[[wikibase]]** _(provider-doc · vendor)_ — Wikibase is a free, open-source software suite for creating collaborative, structured knowledge bases and opening them to the Linked Open Data web ⟨wikibase: homepage⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — A Wikibase knowledge base is a collection of Entities, with two predefined kinds — Items and Properties — and may be extended to support additional entity types ⟨wikibase: data-model-primer/Summary⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Deliberately models statements about items rather than the items themselves — its guiding requirement is that "Wikibase will not be about the truth, but about statements and their references" ⟨wikibase: data-model-primer/Statements⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Used especially by GLAM (galleries, libraries, archives, museums), research, and science groups to pool, edit and curate structured data for both human and machine audiences, publish it as RDF, and query it with SPARQL ⟨wikibase: homepage⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — In a federated setup, data stays where it is created but can be accessed and referenced from other Wikibases, with the query service using SPARQL ⟨wikibase: homepage/nutshell · docs-hub/Managing data⟩

## Where sources differ

Only the Wikibase source is cited here. It characterizes a structured knowledge base as a curated collection of referenced statements — explicitly about statements and their sources rather than about asserting truth — and leaves trust in any individual claim to the reader.

## See also
[[semantic-wiki]] · [[entity-data-model]] · [[linked-open-data]]

<!-- REVIEW: possible J1 near-duplicate between [[structured-knowledge-base]] and [[entity-data-model]] (both sourced only from Wikibase, overlapping lead). Judge confidence low: system-class vs data-model split is defensible. Human to decide merge vs keep. -->
