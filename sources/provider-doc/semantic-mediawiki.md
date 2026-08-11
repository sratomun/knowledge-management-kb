---
title: "Semantic MediaWiki (SMW)"
type: source
kind: provider-doc
authority: vendor
subtype: system-documentation
aliases: ["SMW", "Semantic MediaWiki"]
publisher: Semantic MediaWiki project
url: https://www.semantic-mediawiki.org/
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [semantic-wiki]
updated: 2026-08-10
---

# Semantic MediaWiki (SMW)

## Scope & purpose
Semantic MediaWiki (SMW) is a free, open-source extension to MediaWiki — the wiki
software that powers Wikipedia — that lets editors store and query data within the
wiki's own pages, turning ordinary wiki articles into a structured knowledge base.
Beyond the core extension it is a full-fledged framework that, together with a large
family of spin-off extensions, can turn a wiki into a flexible knowledge management
system whose data can be exported or published on the Semantic Web for other systems
to reuse. This page summarizes the vendor/community documentation as presented on the
project homepage at semantic-mediawiki.org; the linked Help-namespace pages
(Introduction, Semantic annotation, Getting started) were unreachable at capture time
(connection timeouts through the proxy), so the deeper mechanics are noted here only
at the level the homepage states them.

## Structure
The homepage frames SMW along three axes. First, positioning: SMW is an extension to
MediaWiki, a framework extended by many spin-off extensions, and a knowledge
management system whose contents export to the Semantic Web. Second, release cadence:
a prominent version banner (SMW 7.2.0 at capture) and a News feed record a rapid
series of releases (7.0.0 in June 2026, 7.1.0 and 7.2.0 in July 2026) alongside
community events such as the Semantic MediaWiki Conference (SMWCon / MUDCon). Third, a
documentation map organized as Installation (Administrator manual — installation,
configuration, maintenance, related extensions), Usage (User manual — getting started,
testing and sharing tips, support, bug reporting), and The Project (about,
contributing, translating, development roadmap, programmer's guide). The project is
community-run and sponsor-supported (KM-A, Professional Wiki, gesinn.it, HMS
Analytical Software).

## Key points
- Semantic MediaWiki (SMW) is a free, open-source extension to MediaWiki — the wiki software that powers Wikipedia — that lets you store and query data within the wiki's pages ⟨smw: homepage/intro⟩.
- SMW is also a full-fledged framework that, in conjunction with many spin-off extensions, can turn a wiki into a powerful and flexible knowledge management system ⟨smw: homepage/intro⟩.
- All data created within Semantic MediaWiki can easily be exported or published via the Semantic Web, allowing other systems to use this data seamlessly ⟨smw: homepage/intro⟩.
- SMW builds on MediaWiki rather than replacing it, so its data lives in normal wiki pages and inherits the wiki's collaborative editing, versioning, and page model ⟨smw: homepage/intro⟩.
- The current release at capture is SMW 7.2.0, part of a rapid 2026 release series (7.0.0 released June 4, 2026; 7.1.0 released July 9, 2026; 7.2.0 released July 17, 2026) ⟨smw: homepage/News⟩.
- SMW's capabilities are extended by a family of related spin-off extensions, listed under the Administrator manual's "Related extensions" section ⟨smw: homepage/Installation · Related extensions⟩.
- Documentation is split into an Administrator manual (installation, configuration, maintenance, related extensions) and a User manual (getting started, testing and sharing tips, support, reporting bugs and wishes) ⟨smw: homepage/Installation · Usage⟩.
- The project is community-driven and sponsor-supported — sponsors include KM-A (Knowledge Management Associates), Professional Wiki, gesinn.it, and HMS Analytical Software — and it runs an annual Semantic MediaWiki Conference (SMWCon) ⟨smw: homepage/Sponsors · Talks and publications⟩.
- SMW works by letting editors add semantic annotations to wiki pages, marking up in-page values as machine-readable data rather than plain text [gen: standard SMW mechanic; the homepage states data is "stored" in wiki pages but the annotation-syntax detail was on the unreachable Help:Semantic annotation page] ⟨smw: general — annotation not on captured homepage⟩.
- Annotations are expressed through properties, typed relationships that attach a value to a page and give the wiki its structured schema [gen: standard SMW mechanic; not detailed on the captured homepage] ⟨smw: general — properties not on captured homepage⟩.
- Each property has a datatype (e.g. page, text, number, date, URL, coordinates) that governs how its values are stored, validated, and displayed [gen: standard SMW mechanic; not detailed on the captured homepage] ⟨smw: general — datatypes not on captured homepage⟩.
- Stored annotations are retrieved with inline queries — the #ask parser function — which embed live query results directly into wiki pages; the homepage confirms SMW "lets you store and query data within the wiki's pages" ⟨smw: homepage/intro (query) · [gen] #ask syntax not on captured homepage⟩.
- Data can be exported and published as Semantic Web formats (RDF/OWL), letting external systems consume the wiki's knowledge; the homepage confirms export/publication "via the Semantic Web" ⟨smw: homepage/intro (Semantic Web export) · [gen] RDF/OWL specifics not on captured homepage⟩.
- Positioned as a knowledge management platform, SMW targets organizations that want a collaboratively edited, queryable, and machine-exportable knowledge base rather than a static document wiki ⟨smw: homepage/intro⟩.

## Concepts & entities covered
Concepts: [[semantic-wiki]] · [[structured-knowledge-base]]
Entities: [[smw-property]] · [[smw-datatype]] · [[smw-ask-query]] · [[smw-concept]] · [[smw-rdf-export]]
