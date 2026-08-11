---
title: "RDF triple"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[rdf-data-model]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# RDF triple

## What it is
An RDF triple is the atomic statement of the RDF data model: a subject-predicate-object structure asserting that a relationship holds between two resources.

## Key facts
- An RDF triple consists of three components: the subject, which is an IRI or a blank node; the predicate, which is an IRI; and the object, which is an IRI, a literal, or a blank node ⟨§3.1⟩.
- An RDF triple is conventionally written in the order subject, predicate, object ⟨§3.1⟩.
- Asserting an RDF triple says that some relationship, indicated by the predicate, holds between the resources denoted by the subject and object; this statement is known as an RDF statement ⟨§1.2⟩.
- An RDF graph is the conjunction (logical AND) of its triples ⟨§1.7⟩.

## Relations
- Realizes: [[rdf-data-model]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-graph]], [[rdf-iri]], [[rdf-literal]], [[rdf-blank-node]]

## See also
[[rdf-graph]]
