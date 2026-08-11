---
title: "Compacted Document Form"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# Compacted Document Form

## What it is
A form of a JSON-LD document in which a context is applied to shorten IRIs to terms or compact IRIs and to represent values concisely.

## Key facts
- Compaction applies a context to shorten IRIs, represent values as strings, represent lists as arrays, and normalize the shape of the data ⟨§5.2⟩.
- When compacting, the algorithm compacts a property using a term only when the values match the term's @container, @type, and @language specifications; otherwise it compacts using the absolute IRI of the property ⟨§5.2.8⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-expanded-form]]

## See also
[[linked-data-serialization]] [[jsonld-expanded-form]]
