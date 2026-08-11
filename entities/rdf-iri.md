---
title: "IRI"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[iri-identity]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# IRI

## What it is
An IRI (Internationalized Resource Identifier) is one of the three kinds of RDF term. It is a globally-scoped Unicode identifier used as the subject or predicate of a triple, and as an object, to denote a resource.

## Key facts
- An IRI within an RDF graph is a Unicode string that conforms to the syntax defined in RFC 3987 ⟨§3.2⟩.
- IRIs in the RDF abstract syntax MUST be absolute, and MAY contain a fragment identifier ⟨§3.2⟩.
- Two IRIs are equal if and only if they are equivalent under Simple String Comparison according to RFC 3987 section 5.1; further normalization MUST NOT be performed when comparing IRIs for equality ⟨§3.2⟩.
- By design, IRIs have global scope, so two different appearances of an IRI denote the same resource; violating this constitutes an IRI collision ⟨§1.3⟩.

## Relations
- Realizes: [[iri-identity]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-literal]], [[rdf-blank-node]]

## See also
[[rdf-triple]] · [[org-w3c]]
