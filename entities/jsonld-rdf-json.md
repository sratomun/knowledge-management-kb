---
title: "rdf:JSON"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# rdf:JSON

## What it is
The RDF datatype used to carry native JSON content as a literal value, associated in JSON-LD with the @json type keyword.

## Key facts
- The IRI denoting the rdf:JSON datatype is http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON ⟨§10.2⟩.
- Its lexical space is the set of UNICODE strings which conform to the JSON Grammar as described in Section 2 JSON Grammar of [RFC8259] ⟨§10.2⟩.
- A JSON literal is a literal whose associated datatype IRI is rdf:JSON, represented in a value object with @type set to @json ⟨§4.2.2⟩ ⟨§10.2⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-json]]

## See also
[[jsonld-json]] [[rdf-data-model]]
