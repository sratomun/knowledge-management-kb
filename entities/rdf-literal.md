---
title: "Literal"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[literal-datatyping]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Literal

## What it is
A literal is one of the three kinds of RDF term, used for values such as strings, numbers, and dates. It pairs a lexical form with a datatype IRI (and optionally a language tag) that determines the value it denotes.

## Key facts
- A literal in an RDF graph consists of a lexical form (a Unicode string, which SHOULD be in Normal Form C), a datatype IRI, and — if and only if the datatype IRI is rdf:langString — a non-empty language tag as defined by BCP47 ⟨§3.3⟩.
- Two literals are term-equal (the same RDF literal) if and only if the two lexical forms, the two datatype IRIs, and the two language tags (if any) compare equal, character by character ⟨§3.3⟩.
- Implementations MUST accept ill-typed literals and produce RDF graphs from them, and MAY produce warnings when encountering ill-typed literals ⟨§3.3⟩.
- Two literals can have the same value without being the same RDF term; e.g. "1"^^xsd:integer and "01"^^xsd:integer denote the same value but are not term-equal ⟨§3.3⟩.

## Relations
- Realizes: [[literal-datatyping]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-datatype-iri]], [[rdf-langstring]]

## See also
[[rdf-triple]] · [[rdf-html]] · [[rdf-xmlliteral]]
