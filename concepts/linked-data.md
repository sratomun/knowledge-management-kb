---
title: "Linked Data"
type: concept
tags: [semantic-web]
related: ["[[linked-data-serialization]]", "[[iri-identity]]", "[[rdf-data-model]]", "[[rdf-vocabulary-namespace]]"]
updated: 2026-08-09
---

# Linked Data

## What it is

Linked Data is the practice of publishing structured data on the Web so that it interlinks: resources are named with globally-scoped IRIs, described using shared RDF vocabularies, and connected to other data through those identifiers. The payoff is that independently published datasets can be joined and traversed like a web of data rather than sitting in isolated silos. Different communities reach Linked Data from different starting points — from plain JSON, from existing metadata vocabularies, or directly from the RDF model.

## How sources treat it

- **[[json-ld-11]]** _(standard · normative)_ — JSON-LD is a lightweight syntax to serialize Linked Data in JSON, designed so that existing JSON can be interpreted as Linked Data with minimal changes and offering a smooth upgrade path from plain JSON ⟨§1⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — DCMI terms are expressed in RDF vocabularies for use in Linked Data, though non-RDF users may disregard the RDF-specific implications and rely on the natural-language definitions ⟨§1 Introduction⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — Each term is identified with a URI serving as a global identifier that resolves to the specification document in a browser or to one of four RDF schemas programmatically ⟨§1 Introduction⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — By design IRIs have global scope, so two different appearances of an IRI denote the same resource — the identifier property that makes cross-dataset linking possible ⟨§1.3, §1.5⟩.

## Where sources differ

The sources frame Linked Data from different vantage points rather than contradicting one another. json-ld-11 treats it as a serialization target, emphasizing an upgrade path so that deployed JSON systems can become Linked Data with minimal change ⟨§1⟩. dcmi-terms treats Linked Data as one deployment of its vocabulary while explicitly accommodating non-RDF users who rely on natural-language definitions ⟨§1 Introduction⟩. rdf-11-concepts does not foreground the term "Linked Data" but supplies the underlying global-identifier model on which the practice rests ⟨§1.3, §1.5⟩.

## See also

[[linked-data-serialization]] · [[iri-identity]] · [[rdf-data-model]] · [[rdf-vocabulary-namespace]]
