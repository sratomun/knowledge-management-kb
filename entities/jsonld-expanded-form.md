---
title: "Expanded Document Form"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# Expanded Document Form

## What it is
A canonical form of a JSON-LD document in which a context has been applied and removed so that all IRIs, types, and values are fully expressed.

## Key facts
- Expansion is the process of taking a JSON-LD document and applying a context such that all IRIs, types, and values are expanded so that the @context is no longer necessary ⟨§5.1⟩.
- The method for expanding a JSON-LD document is defined by the JSON-LD 1.1 Processing Algorithms and API specification ⟨§5.1⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-compacted-form]]
- Related: [[jsonld-context]]

## See also
[[linked-data-serialization]] [[jsonld-compacted-form]]
