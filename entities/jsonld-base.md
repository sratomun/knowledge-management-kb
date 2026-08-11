---
title: "@base"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[iri-identity]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @base

## What it is
The keyword that sets the base IRI against which relative IRI references in the document are resolved.

## Key facts
- The unaliased @base keyword MAY be used as a key in a context definition ⟨§9.16⟩.
- Its value MUST be an IRI reference, or null ⟨§9.16⟩.
- The @base will be ignored if used in external contexts, and setting @base to null prevents relative IRI references from being expanded to IRIs ⟨§4.1.3⟩.

## Relations
- Realizes: [[iri-identity]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-vocab]]

## See also
[[iri-identity]] [[jsonld-vocab]]
