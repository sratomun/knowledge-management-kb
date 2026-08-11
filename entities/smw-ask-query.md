---
title: "SMW ask query"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-wiki]
concepts: ["[[semantic-wiki]]", "[[structured-knowledge-base]]"]
sources: ["[[semantic-mediawiki]]"]
updated: 2026-08-10
---

# SMW #ask query

## What it is
The `#ask` parser function is Semantic MediaWiki's inline query mechanism: an editor
embeds a query directly in a wiki page and SMW renders the live results in place,
retrieving data that was annotated via properties. [gen: the `#ask` syntax is
documented on the Help namespace, which was unreachable at capture; the homepage
confirms SMW "lets you store and query data within the wiki's pages".]

## Key facts
- SMW lets editors query the data stored within the wiki's pages, not only store it ⟨smw: homepage/intro (query)⟩
- Inline queries are written with the `#ask` parser function and embed their results directly into wiki pages [gen] ⟨smw: general — not on captured homepage⟩
- Queries select pages by their property values, so the wiki's structured schema is what makes results computable [gen] ⟨smw: general — not on captured homepage⟩

## Relations
- Realizes: [[semantic-wiki]]
- Defined in: [[semantic-mediawiki]]
- Maintained by: [[org-smw-project]]
- Related: [[smw-property]]
- Related: [[smw-concept]]

## See also
[[structured-knowledge-base]]
