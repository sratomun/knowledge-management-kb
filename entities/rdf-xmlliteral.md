---
title: "rdf:XMLLiteral"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[literal-datatyping]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# rdf:XMLLiteral

## What it is
rdf:XMLLiteral is a non-normative RDF datatype that allows XML content to be a literal value.

## Key facts
- The IRI denoting this datatype is http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral ⟨§5.3⟩.
- Its lexical space is the set of all strings which are well-balanced, self-contained XML content and which, embedded between an arbitrary XML start and end tag, yield a document conforming to XML Namespaces ⟨§5.3⟩.
- Its value space is a set of DOM DocumentFragment nodes, and its canonical mapping is the exclusive XML canonicalization method (with comments, with empty InclusiveNamespaces PrefixList) ⟨§5.3⟩.
- This datatype is defined as non-normative because it depends on DOM4, a specification that had not yet reached W3C Recommendation status ⟨§5.3⟩.

## Relations
- Realizes: [[literal-datatyping]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-html]], [[rdf-datatype-iri]]

## See also
[[rdf-literal]]
