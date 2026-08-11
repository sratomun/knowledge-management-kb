---
title: "Skolemization"
type: concept
tags: [semantic-web]
related: ["[[blank-node]]", "[[iri-identity]]", "[[rdf-data-model]]"]
updated: 2026-08-09
---

# Skolemization

## What it is

Skolemization is the practice of replacing blank nodes with fresh, globally unique IRIs so that the resources they stand for gain stable, referenceable names. Because blank node identifiers are local to a serialization or store and cannot be reliably referred to from outside, minting a "Skolem IRI" for each blank node is how a system publishes those nodes as first-class, addressable resources without changing what the graph asserts.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — Blank node identifiers are local to a concrete syntax or store and are not part of the abstract syntax, which motivates replacing them with stable IRIs ⟨§3.4⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Systems replacing blank nodes with IRIs SHOULD mint a new globally unique Skolem IRI per blank node ⟨§3.5⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Systems wanting Skolem IRIs to be recognizable as such externally SHOULD use a well-known IRI whose path component starts with `/.well-known/genid/` ⟨§3.5⟩.

## Where sources differ

This concept is covered by a single source, rdf-11-concepts, so there is no divergence to report here.

## See also

[[blank-node]] · [[iri-identity]] · [[rdf-data-model]]
