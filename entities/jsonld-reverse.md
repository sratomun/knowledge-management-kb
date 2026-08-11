---
title: "@reverse"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @reverse

## What it is
The keyword used to express reverse properties, serializing an edge in the reverse direction.

## Key facts
- The @reverse keyword MAY be aliased and MAY be used as a key in a node object ⟨§9.16⟩.
- The value of the @reverse key MUST be an IRI reference, or a compact IRI (including blank node identifiers) ⟨§9.16⟩.
- It is used to express reverse properties, for the case where it is desirable to serialize in the reverse direction ⟨§4.8⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-id]]

## See also
[[rdf-data-model]] [[jsonld-id]]
