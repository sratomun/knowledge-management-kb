---
title: "Entailment and equivalence"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[blank-node]]", "[[literal-datatyping]]", "[[iri-identity]]"]
updated: 2026-08-09
---

# Entailment and equivalence

## What it is

Entailment and equivalence are the model-theoretic notions that give RDF its meaning as logic rather than mere data. A graph is read as the conjunction of its triples, so one graph entails another when everything the first says makes the second true as well; two graphs are equivalent (isomorphic) when they differ only in the naming of blank nodes; and equality is defined term by term for IRIs and literals. These notions underpin comparison, deduplication, and reasoning over RDF.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — The RDF data model is atemporal: RDF graphs are static snapshots, an RDF graph is the conjunction (logical AND) of its triples, and graph A entails graph B if every arrangement of the world making A true also makes B true ⟨§1.5, §1.7⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two RDF graphs are isomorphic if there is a bijection mapping blank nodes to blank nodes and fixing all literals and IRIs such that triples correspond ⟨§3.6⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two IRIs are equal if and only if they are equivalent under Simple String Comparison per RFC 3987 §5.1 ⟨§3.2⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two literals are term-equal if and only if their lexical forms, datatype IRIs, and language tags (if any) compare equal character by character, and two literals can share a value without being term-equal ⟨§3.3⟩.

## Where sources differ

This concept is covered by a single source, rdf-11-concepts, so there is no divergence to report here.

## See also

[[rdf-data-model]] · [[blank-node]] · [[literal-datatyping]] · [[iri-identity]]
