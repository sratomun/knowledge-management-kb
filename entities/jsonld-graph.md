---
title: "@graph"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-dataset]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @graph

## What it is
The keyword used to express a graph, including named graphs, within a JSON-LD document.

## Key facts
- The @graph keyword MAY be aliased and MAY be used as a key in a node object or a graph object, where its value MUST be a value object, node object, or an array of either value objects or node objects ⟨§9.16⟩.
- The unaliased @graph MAY be used as the value of the @container key within an expanded term definition ⟨§9.16⟩.
- It is useful at top level with a map to describe disconnected nodes while saving the repetition of @context ⟨§4.9⟩ ⟨§4.1⟩.

## Relations
- Realizes: [[rdf-dataset]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-id]]
- Related: [[jsonld-container]]

## See also
[[rdf-dataset]] [[jsonld-container]]
