---
title: "Semantic Wiki"
type: concept
subtype: system-class
aliases: []
tags: [semantic-wiki]
related: ["[[structured-knowledge-base]]", "[[entity-data-model]]", "[[linked-open-data]]", "[[knowledge-management-system]]"]
updated: 2026-08-10
---

# Semantic Wiki

## What it is

A semantic wiki is a wiki whose pages carry machine-readable structured data — not just prose — so that the content can be stored, queried, and exported as data while retaining the wiki's collaborative editing, versioning, and page model. It sits between a document wiki and a knowledge base: editors add structure (properties, statements, typed values) to ordinary pages, and the system can answer queries over that structure and publish it for other systems to reuse.

## How sources treat it

- **[[semantic-mediawiki]]** _(provider-doc · vendor)_ — Semantic MediaWiki (SMW) is a free, open-source extension to MediaWiki — the software that powers Wikipedia — that lets editors store and query data within the wiki's own pages ⟨smw: homepage/intro⟩
- **[[semantic-mediawiki]]** _(provider-doc · vendor)_ — SMW is also a full-fledged framework that, with many spin-off extensions, can turn a wiki into a powerful and flexible knowledge management system ⟨smw: homepage/intro⟩
- **[[semantic-mediawiki]]** _(provider-doc · vendor)_ — Builds on MediaWiki rather than replacing it, so its data lives in normal wiki pages and inherits collaborative editing, versioning, and the page model ⟨smw: homepage/intro⟩
- **[[semantic-mediawiki]]** _(provider-doc · vendor)_ — [gen] Works by letting editors add semantic annotations to wiki pages, expressed through properties (typed relationships attaching a value to a page), each with a datatype; stored annotations are retrieved with inline #ask queries embedded in pages ⟨smw: general — annotation/properties/#ask not on captured homepage⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Wikibase is an open-source software suite for building collaborative, structured knowledge bases that can be opened up as Linked Open Data; it is built on and requires MediaWiki (with an Extension:Wikibase) ⟨wikibase: homepage · docs-hub/overview⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Powers Wikidata and is offered as Wikibase Cloud (SaaS) and self-hosted Wikibase Suite Docker images / Wikibase Deploy ⟨wikibase: homepage/Showcases · docs-hub/overview⟩

## Where sources differ

Both sources are MediaWiki-based structured-data extensions, but they frame the structure differently. SMW attaches typed properties and values directly to article pages and queries them in-page with #ask, keeping the article as the primary unit; several of its mechanics (annotation syntax, properties, datatypes, #ask) are marked [gen] because the Help pages were unreachable at capture. Wikibase instead models discrete Items and Properties with referenced statements as first-class entities, oriented toward publishing Linked Open Data and querying with SPARQL. Neither source is ranked against the other.

## See also
[[structured-knowledge-base]] · [[entity-data-model]] · [[linked-open-data]] · [[knowledge-management-system]]
