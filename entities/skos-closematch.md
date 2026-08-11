---
title: "skos:closeMatch"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[scheme-mapping]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:closeMatch

## What it is
A mapping property linking two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.

## Key facts
- skos:closeMatch is a sub-property of skos:mappingRelation ⟨S40⟩ and is an instance of owl:SymmetricProperty ⟨S44⟩.
- In order to avoid the possibility of "compound errors" when combining mappings across more than two concept schemes, skos:closeMatch is not declared to be a transitive property ⟨§10.1⟩.
- skos:exactMatch is a sub-property of skos:closeMatch ⟨S42⟩.

## Relations
- Realizes: [[scheme-mapping]]
- Defined in: [[skos]]
- Related: [[skos-exactmatch]] · [[skos-mappingrelation]]

## See also
[[skos-exactmatch]]
