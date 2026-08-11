---
title: "skos:broaderTransitive"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[semantic-relation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:broaderTransitive

## What it is
A transitive super-property of skos:broader, used to infer the transitive closure of the hierarchical links so that direct or indirect broader ("ancestor") links between concepts can be accessed, e.g. for query expansion.

## Key facts
- skos:broaderTransitive is an instance of owl:ObjectProperty ⟨S18⟩ and a sub-property of skos:semanticRelation ⟨S21⟩.
- skos:broaderTransitive and skos:narrowerTransitive are each instances of owl:TransitiveProperty ⟨S24⟩; skos:narrowerTransitive is owl:inverseOf skos:broaderTransitive ⟨S26⟩.
- Integrity condition: skos:related is disjoint with the property skos:broaderTransitive ⟨S27⟩.

## Relations
- Realizes: [[semantic-relation]]
- Defined in: [[skos]]
- Related: [[skos-broader]] · [[skos-narrowertransitive]] · [[skos-related]]

## See also
[[skos-broader]] · [[skos-semanticrelation]]
