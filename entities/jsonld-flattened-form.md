---
title: "Flattened Document Form"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# Flattened Document Form

## What it is
A form of a JSON-LD document in which every node's properties are collected into a single map and all blank nodes are labeled.

## Key facts
- Flattening collects all properties of a node in a single map and labels all blank nodes with blank node identifiers ⟨§5.3⟩.
- This ensures a shape of the data and consequently may drastically simplify the code required to process JSON-LD in certain applications ⟨§5.3⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-framed-form]]

## See also
[[linked-data-serialization]] [[jsonld-framed-form]]
