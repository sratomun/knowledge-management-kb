---
title: "@list"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @list

## What it is
The keyword used to express an ordered sequence of values (a list object).

## Key facts
- The @list keyword MAY be aliased and MUST be used as a key in a list object ⟨§9.16⟩.
- The unaliased @list MAY be used as the value of the @container key within an expanded term definition ⟨§9.16⟩.
- It is used to express an ordered set of data, since JSON-LD arrays are unordered by default ⟨§4.3.1⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-set]]
- Related: [[jsonld-container]]

## See also
[[rdf-data-model]] [[jsonld-set]]
