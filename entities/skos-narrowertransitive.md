---
title: "skos:narrowerTransitive"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[semantic-relation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:narrowerTransitive

## What it is
A transitive super-property of skos:narrower, used to infer the transitive closure of the hierarchical links so that direct or indirect narrower ("descendant") links between concepts can be accessed.

## Key facts
- skos:narrowerTransitive is an instance of owl:ObjectProperty ⟨S18⟩ and a sub-property of skos:semanticRelation ⟨S21⟩.
- skos:broaderTransitive and skos:narrowerTransitive are each instances of owl:TransitiveProperty ⟨S24⟩; skos:narrowerTransitive is owl:inverseOf skos:broaderTransitive ⟨S26⟩.
- By convention skos:broaderTransitive and skos:narrowerTransitive are not used to make assertions, but rather to infer the transitive closure of the hierarchical links ⟨§8.1⟩.

## Relations
- Realizes: [[semantic-relation]]
- Defined in: [[skos]]
- Related: [[skos-narrower]] · [[skos-broadertransitive]]

## See also
[[skos-narrower]] · [[skos-semanticrelation]]
