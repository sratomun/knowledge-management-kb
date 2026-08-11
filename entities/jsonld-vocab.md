---
title: "@vocab"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[iri-identity]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @vocab

## What it is
The keyword that sets a common vocabulary-mapping prefix used to expand properties and types that are not terms, IRIs, or compact IRIs.

## Key facts
- The unaliased @vocab keyword MAY be used as a key in a context definition or as the value of @type in an expanded term definition ⟨§9.16⟩.
- Its value MUST be an IRI reference, a compact IRI, a blank node identifier, a term, or null ⟨§9.16⟩.
- Since JSON-LD 1.1, the vocabulary mapping in a local context can be set to a relative IRI reference, which is concatenated to any vocabulary mapping in the active context ⟨§4.1.2⟩.

## Relations
- Realizes: [[iri-identity]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-base]]
- Related: [[jsonld-context]]

## See also
[[iri-identity]] [[jsonld-base]]
