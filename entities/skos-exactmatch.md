---
title: "skos:exactMatch"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[scheme-mapping]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:exactMatch

## What it is
A mapping property linking two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications.

## Key facts
- skos:exactMatch is a sub-property of skos:closeMatch ⟨S42⟩ and is an instance of owl:SymmetricProperty ⟨S44⟩ and owl:TransitiveProperty ⟨S45⟩.
- Integrity condition: skos:exactMatch is disjoint with each of the properties skos:broadMatch and skos:relatedMatch (and, being symmetric, also with skos:narrowMatch) ⟨S46⟩.
- skos:exactMatch is a transitive property, whereas skos:closeMatch is deliberately not declared transitive to avoid "compound errors" when combining mappings across more than two concept schemes ⟨§10.1⟩.

## Relations
- Realizes: [[scheme-mapping]]
- Defined in: [[skos]]
- Related: [[skos-closematch]] · [[skos-mappingrelation]]

## See also
[[skos-closematch]]
