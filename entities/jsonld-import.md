---
title: "@import"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @import

## What it is
The keyword that loads an external context (an imported context) and merges it with the wrapping context prior to processing.

## Key facts
- The unaliased @import keyword MAY be used in a context definition; its value MUST be an IRI reference ⟨§9.16⟩.
- Once an imported context is loaded, the contents of the wrapping context are merged into it, with the wrapping-context key/value pairs taking precedence ⟨§4.1.10⟩.
- It can be useful to add JSON-LD 1.1 features to JSON-LD 1.0 contexts ⟨§1.7⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-context]]

## See also
[[linked-data-serialization]] [[jsonld-context]]
