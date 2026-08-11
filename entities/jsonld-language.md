---
title: "@language"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @language

## What it is
The keyword that specifies the language of a string value or the default language of a JSON-LD document.

## Key facts
- The @language keyword MAY be aliased and MAY be used as a key in a value object; its value MUST be a string with the lexical form described in [BCP47] or be null ⟨§9.16⟩.
- The unaliased @language MAY be used as a key in a context definition, or as the value of the @container key within an expanded term definition ⟨§9.16⟩.
- It is used to specify the language for a particular string value or the default language of a JSON-LD document ⟨§4.2.4⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-value]]

## See also
[[rdf-data-model]] [[jsonld-value]]
