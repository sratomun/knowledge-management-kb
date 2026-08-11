---
title: "@value"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @value

## What it is
The keyword that specifies the literal data of a value object.

## Key facts
- The @value keyword MAY be aliased and MUST be used as a key in a value object ⟨§9.16⟩.
- Its value MUST be either a string, a number, true, false or null ⟨§9.16⟩.
- If @value, @list, or @set is set to null in expanded form, then the entire JSON object is ignored ⟨§1.4⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-type]]
- Related: [[jsonld-language]]

## See also
[[rdf-data-model]] [[jsonld-type]]
