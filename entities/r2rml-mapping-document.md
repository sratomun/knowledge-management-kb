---
title: "R2RML Mapping Document"
type: entity
subtype: specification-construct
aliases: ["R2RML mapping document"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# R2RML Mapping Document

## What it is
The concrete artifact of an R2RML mapping: a Turtle document that encodes an R2RML mapping graph, tailored to a specific database schema and target vocabulary.

## Key facts
- "An R2RML mapping document is any document written in the Turtle RDF syntax that encodes an R2RML mapping graph" ⟨§4.2⟩
- The media type is text/turtle, the content encoding is always UTF-8 and the charset parameter SHOULD always be used (text/turtle;charset=utf-8); the file extension .ttl SHOULD be used ⟨§4.2⟩
- A conforming R2RML processor SHOULD accept R2RML mapping documents in Turtle syntax and MAY accept R2RML mapping graphs encoded in other RDF syntaxes ⟨§4.2⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-mapping-graph]], [[r2rml-triplesmap]]

## See also
[[r2rml-direct-mapping]] · [[org-w3c]]
