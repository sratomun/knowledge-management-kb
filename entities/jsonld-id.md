---
title: "@id"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[iri-identity]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @id

## What it is
The keyword that assigns a node its identifier, an IRI or blank node identifier, so it can be referenced externally in the graph.

## Key facts
- The @id keyword MAY be aliased and MAY be used as a key in a node object or a graph object ⟨§9.16⟩.
- The value of the @id key MUST be an IRI reference, or a compact IRI (including blank node identifiers) ⟨§9.16⟩.
- It is used to uniquely identify node objects with IRIs or blank node identifiers; a node reference is a node object containing only the @id property ⟨§3.3⟩.

## Relations
- Realizes: [[iri-identity]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-vocab]]

## See also
[[iri-identity]] [[jsonld-type]]
