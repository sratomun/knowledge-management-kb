---
title: "SMW property"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-wiki]
concepts: ["[[semantic-wiki]]", "[[structured-knowledge-base]]"]
sources: ["[[semantic-mediawiki]]"]
updated: 2026-08-10
---

# SMW property

## What it is
In Semantic MediaWiki, a property is the core annotation construct: a typed
relationship that attaches a machine-readable value to a wiki page, giving the wiki
its structured schema. [gen: the property mechanic is described on the Help:Semantic
annotation page, which was unreachable at capture; the homepage confirms only that SMW
lets editors "store and query data within the wiki's pages".]

## Key facts
- SMW lets editors store data within the wiki's pages, and properties are the mechanism that turns in-page values into machine-readable data [gen: property detail from general SMW knowledge; homepage confirms data is stored within wiki pages] ⟨smw: homepage/intro · [gen] property detail not on captured homepage⟩
- Each property carries a datatype that governs how its values are stored, validated, and displayed [gen] ⟨smw: general — not on captured homepage⟩
- Properties collectively form the queryable schema that inline #ask queries retrieve data against [gen] ⟨smw: general — not on captured homepage⟩

## Relations
- Realizes: [[structured-knowledge-base]]
- Defined in: [[semantic-mediawiki]]
- Maintained by: [[org-smw-project]]
- Related: [[smw-datatype]]
- Related: [[smw-ask-query]]

## See also
[[semantic-wiki]]
