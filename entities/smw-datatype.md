---
title: "SMW datatype"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-wiki]
concepts: ["[[semantic-wiki]]", "[[structured-knowledge-base]]"]
sources: ["[[semantic-mediawiki]]"]
updated: 2026-08-10
---

# SMW datatype

## What it is
In Semantic MediaWiki, a datatype is the value type assigned to a property that
governs how the annotated value is stored, validated, sorted, and displayed (for
example page, text, number, date, URL, or geographic coordinate). [gen: datatype
detail is documented on the Help namespace, which was unreachable at capture; the
homepage confirms only that SMW lets editors "store and query data within the wiki's
pages".]

## Key facts
- Every SMW property is associated with a datatype that determines how its values are interpreted and rendered [gen] ⟨smw: general — not on captured homepage⟩
- SMW ships a predefined set of datatypes (e.g. page, text, number, date, URL, coordinates), so annotated values are more than plain strings [gen] ⟨smw: general — not on captured homepage⟩
- Typed values are what make stored data reliably queryable and exportable to the Semantic Web, which the homepage states SMW supports [gen: typing detail from general knowledge; homepage confirms Semantic Web export] ⟨smw: homepage/intro (Semantic Web export) · [gen] datatype detail not on captured homepage⟩

## Relations
- Realizes: [[structured-knowledge-base]]
- Defined in: [[semantic-mediawiki]]
- Maintained by: [[org-smw-project]]
- Related: [[smw-property]]

## See also
[[semantic-wiki]]
