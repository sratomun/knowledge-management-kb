---
title: "@container"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @container

## What it is
The keyword that sets the default container type for a term, controlling how its values are indexed or ordered.

## Key facts
- The unaliased @container keyword MAY be used as a key in an expanded term definition ⟨§9.16⟩.
- Its value MUST be either @list, @set, @language, @index, @id, @graph, @type, or be null, or an array containing exactly any one of those keywords, or a combination of @set and any of @index, @id, @graph, @type, @language in any order ⟨§9.16⟩.
- It is used to set the default container type for a term ⟨§1.7⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-list]]
- Related: [[jsonld-set]]
- Related: [[jsonld-graph]]

## See also
[[linked-data-serialization]] [[jsonld-list]]
