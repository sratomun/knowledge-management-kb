---
title: "@nest"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @nest

## What it is
The keyword that groups together properties of a node object without creating an edge in the graph.

## Key facts
- The @nest keyword MAY be aliased and MAY be used as a key in a node object, where its value must be a map ⟨§9.16⟩.
- The unaliased @nest MAY be used as the value of a simple term definition, or as a key in an expanded term definition, where its value MUST be a string expanding to @nest ⟨§9.16⟩.
- It defines a property of a node object that groups together properties of that node, but is not an edge in the graph ⟨§1.7⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]

## See also
[[linked-data-serialization]] [[jsonld-context]]
