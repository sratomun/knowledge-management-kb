---
title: "skos:broader"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[semantic-relation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:broader

## What it is
A property asserting a direct (immediate) hierarchical link between two concepts: the triple `<A> skos:broader <B>` asserts that B is a broader concept than A.

## Key facts
- By convention skos:broader and skos:narrower are used only to assert a direct hierarchical link, and to support this convention they "are not declared as transitive properties" ⟨§8.1⟩.
- skos:broader is a sub-property of skos:broaderTransitive ⟨S22⟩.
- skos:narrower is owl:inverseOf the property skos:broader ⟨S25⟩.

## Relations
- Realizes: [[semantic-relation]]
- Defined in: [[skos]]
- Related: [[skos-narrower]] · [[skos-broadertransitive]] · [[skos-broadmatch]]

## See also
[[skos-narrower]] · [[skos-broadertransitive]]
