---
title: "SMW Concept"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-wiki]
concepts: ["[[semantic-wiki]]", "[[structured-knowledge-base]]"]
sources: ["[[semantic-mediawiki]]"]
updated: 2026-08-10
---

# SMW Concept

## What it is
In Semantic MediaWiki, a Concept is a special page defining a dynamic collection of
wiki pages via a saved query — effectively a query-defined category that pages join by
matching its criteria rather than by manual tagging. [gen: the Concept construct is
documented on the Help namespace, which was unreachable at capture; the homepage
confirms only SMW's store-and-query model over wiki pages.]

## Key facts
- A Concept bundles pages that satisfy a stored query, acting as a dynamic, query-defined category within the wiki [gen] ⟨smw: general — not on captured homepage⟩
- Concepts build on SMW's inline query capability, reusing the same property-based selection that `#ask` queries use [gen] ⟨smw: general — not on captured homepage⟩
- Because membership is computed from the wiki's structured data, Concepts stay current as underlying page annotations change [gen] ⟨smw: general — not on captured homepage⟩

## Relations
- Realizes: [[structured-knowledge-base]]
- Defined in: [[semantic-mediawiki]]
- Maintained by: [[org-smw-project]]
- Related: [[smw-ask-query]]

## See also
[[semantic-wiki]]
