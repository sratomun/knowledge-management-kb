---
title: "skos:narrower"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[semantic-relation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:narrower

## What it is
A property asserting a direct (immediate) hierarchical link between two concepts: the triple `<C> skos:narrower <D>` asserts that D is a narrower concept than C.

## Key facts
- By convention skos:broader and skos:narrower are used only to assert a direct hierarchical link and "are not declared as transitive properties" ⟨§8.1⟩.
- skos:narrower is a sub-property of skos:narrowerTransitive ⟨S22⟩.
- skos:narrower is owl:inverseOf the property skos:broader ⟨S25⟩.

## Relations
- Realizes: [[semantic-relation]]
- Defined in: [[skos]]
- Related: [[skos-broader]] · [[skos-narrowertransitive]] · [[skos-narrowmatch]]

## See also
[[skos-broader]] · [[skos-narrowertransitive]]
