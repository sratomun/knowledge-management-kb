---
title: "rdf:HTML"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[literal-datatyping]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# rdf:HTML

## What it is
rdf:HTML is a non-normative RDF datatype that allows HTML content to be a literal value, enabling markup in literal values.

## Key facts
- The IRI denoting this datatype is http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML ⟨§5.2⟩.
- Its lexical space is the set of Unicode strings, and its value space is a set of DOM DocumentFragment nodes; two DocumentFragment nodes are equal if and only if the DOM method A.isEqualNode(B) returns true ⟨§5.2⟩.
- The lexical-to-value mapping applies the HTML fragment parsing algorithm (without a context element) to the input string and returns the normalized DocumentFragment ⟨§5.2⟩.
- This datatype is defined as non-normative because it depends on DOM4, a specification that had not yet reached W3C Recommendation status ⟨§5.2⟩.

## Relations
- Realizes: [[literal-datatyping]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-xmlliteral]], [[rdf-datatype-iri]]

## See also
[[rdf-literal]]
