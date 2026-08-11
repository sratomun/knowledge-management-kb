---
title: "@type"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @type

## What it is
The keyword that sets the type of a node or the datatype of a typed value.

## Key facts
- The @type keyword MAY be aliased and MAY be used as a key in a node object or a value object, where its value MUST be a term, IRI reference, or a compact IRI (including blank node identifiers) ⟨§9.16⟩.
- The unaliased @type MAY be used as a key in an expanded term definition, where its value may also be either @id or @vocab ⟨§9.16⟩.
- In addition to typing nodes, @type can set the type of a value to create a typed value; value objects are restricted to having just a single type ⟨§3.5⟩ ⟨§4.2.1⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-value]]
- Related: [[jsonld-vocab]]

## See also
[[rdf-data-model]] [[jsonld-value]]
