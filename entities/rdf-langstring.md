---
title: "rdf:langString"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[literal-datatyping]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# rdf:langString

## What it is
rdf:langString is the datatype IRI carried by language-tagged string literals. It is special-cased in the abstract syntax because such literals also carry a language tag.

## Key facts
- Language-tagged strings have the datatype IRI http://www.w3.org/1999/02/22-rdf-syntax-ns#langString ⟨§5⟩.
- A literal is a language-tagged string if and only if its datatype IRI is rdf:langString; in that case a non-empty language tag, well-formed per BCP47 section 2.2.9, must be present ⟨§3.3⟩.
- No datatype is formally defined for this IRI, because the definition of datatypes does not accommodate language tags in the lexical space; the value space associated with it is the set of all pairs of strings and language tags ⟨§5⟩.
- Most concrete syntaxes represent language-tagged strings without the datatype IRI because it always equals rdf:langString ⟨§3.3⟩.

## Relations
- Realizes: [[literal-datatyping]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-literal]], [[rdf-datatype-iri]]

## See also
[[rdf-literal]]
