---
title: "Wikibase"
type: source
kind: provider-doc
authority: vendor
subtype: system-documentation
aliases: ["Wikibase"]
publisher: Wikimedia Deutschland
url: https://wikiba.se/
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [semantic-wiki]
updated: 2026-08-10
---

# Wikibase

## Scope & purpose
Wikibase is an open-source software suite, made and supported by Wikimedia
Deutschland and a community of contributors, for building collaborative,
structured knowledge bases that can be opened up as Linked Open Data. It is the
software toolbox that powers Wikidata, and organizations — especially GLAM
(galleries, libraries, archives, museums), research, and science groups — use it
to pool, edit and curate structured data for both human and machine audiences,
publish it as RDF, and query it with SPARQL. This page summarizes the vendor and
community documentation: the wikiba.se marketing site, the MediaWiki-hosted
documentation hub, and the Wikibase data model primer.

## Structure
Wikibase is distributed as Wikibase Cloud (a SaaS instance hosted by Wikimedia
Deutschland, simpler feature set, for novices) and Wikibase Suite / Wikibase
Deploy (self-hosted Docker container images, for intermediate-to-expert users
wanting high customisation); it is built on and requires MediaWiki (there is also
an Extension:Wikibase). The captured documentation covers three layers: the
homepage's positioning (federation, linked open data, community, ontology,
ecosystem, and showcase deployments such as Wikidata, FactGrid, Enslaved.org, and
MARDI); the MediaWiki documentation hub (managing data, federation, the SPARQL
query service, administration, customization, community, and reference); and the
data model primer, which specifies entities as items and properties, each with a
fingerprint, statements, claims, qualifiers, references, and ranks.

## Key points
- Wikibase is a free, open-source software suite made and supported by Wikimedia Deutschland and a community of contributors for creating collaborative, structured knowledge bases and opening them to the Linked Open Data web ⟨wikibase: homepage⟩.
- Wikibase was originally developed specifically to power Wikidata, the free and open knowledge graph launched in 2012 that stores structured data as statements backed by references ⟨wikibase: homepage/Showcases — Wikidata⟩.
- A Wikibase knowledge base is a collection of Entities; there are two predefined kinds of Entities — Items and Properties — and Wikibase may be extended to support additional entity types ⟨wikibase: data-model-primer/Summary⟩.
- Each Item has an identifier prefixed with Q and each Property an identifier prefixed with P; both carry a "fingerprint" of a multilingual label, a multilingual description, and multilingual aliases ⟨wikibase: data-model-primer/Summary⟩.
- Within an entity type, an entity's combination of label and description in a given language must be unique (unless empty); labels alone may be ambiguous, so label plus description together identify an item's meaning, while aliases provide alternative names (including popular misspellings) to aid search, much like Wikipedia redirects ⟨wikibase: data-model-primer/Items⟩.
- Wikibase deliberately models statements about items rather than the items themselves — its guiding requirement is that "Wikibase will not be about the truth, but about statements and their references" ⟨wikibase: data-model-primer/Statements⟩.
- A statement consists of one property, one value, optionally one or more qualifiers, and optionally one or more references; the property, value, and qualifiers together form the claim, which with any references forms the statement ⟨wikibase: data-model-primer/Statements⟩.
- Properties are described on their own wiki pages and each carries a data type that defines the type of value used with it; values range from simple (another item or a string) to complex (a geographic shape, a measurement with unit and accuracy, or a time period), the set of data types is mostly predefined, and two special values exist regardless of data type — "none" (known to have no value) and "unknown" (has a value but it is not known which) ⟨wikibase: data-model-primer/Statements⟩.
- Qualifiers are property-value pairs that refine, constrain, or add detail to a statement's value; a qualifier is an integral part of the statement — removing it changes the statement's meaning ⟨wikibase: data-model-primer/Qualifiers⟩.
- References point to a source (itself a Wikibase item, e.g. a book or website) supporting a claim; a claim without references is not necessarily wrong, nor is one with references necessarily true — trust is left to the reader ⟨wikibase: data-model-primer/Statements⟩.
- Statements carry one of three ranks — preferred, normal, or deprecated — used to select which statements a query returns and to keep the display clean (only preferred statements display by default) ⟨wikibase: data-model-primer/Ranks⟩.
- Items also have site links (links to Wikipedia/wiki pages), and multiple identifying mechanisms (site links plus label-and-description across languages) can get out of sync — the "symbol grounding problem" Wikibase addresses socio-technically rather than by giving any language precedence ⟨wikibase: data-model-primer/Items · The symbol grounding problem⟩.
- In a federated setup data stays where it is created but can be accessed and referenced from other Wikibases, and the query service uses SPARQL to query the data ⟨wikibase: homepage/nutshell · docs-hub/Managing data⟩.
- Wikibase is offered as Wikibase Cloud (SaaS hosted by Wikimedia Deutschland) and as self-hosted Wikibase Suite Docker container images / Wikibase Deploy, and it runs on top of MediaWiki [gen: MediaWiki dependency stated on the docs hub, not the homepage] ⟨wikibase: docs-hub/overview⟩.

## Concepts & entities covered
Concepts: [[entity-data-model]] · [[structured-knowledge-base]] · [[linked-open-data]] · [[semantic-wiki]]
Entities: [[wikibase-item]] · [[wikibase-property]] · [[wikibase-statement]] · [[wikibase-qualifier]] · [[wikibase-query-service]] · [[org-wikimedia-de]]
