---
title: "Skolem IRI"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[skolemization]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Skolem IRI

## What it is
A Skolem IRI is a globally unique IRI minted to systematically replace a blank node when stronger, sharable identification is needed.

## Key facts
- Systems wishing to replace blank nodes with IRIs SHOULD mint a new, globally unique IRI (a Skolem IRI) for each blank node so replaced ⟨§3.5⟩.
- Systems that want Skolem IRIs to be recognizable outside of the system boundaries SHOULD use a well-known IRI with the registered name genid, whose path component starts with /.well-known/genid/ ⟨§3.5⟩.
- The transformation does not appreciably change the meaning of an RDF graph, provided that the Skolem IRIs do not occur anywhere else; it does however permit other graphs to subsequently use the Skolem IRIs, which is not possible for blank nodes ⟨§3.5⟩.

## Relations
- Realizes: [[skolemization]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-blank-node]], [[rdf-iri]]

## See also
[[rdf-named-graph]]
