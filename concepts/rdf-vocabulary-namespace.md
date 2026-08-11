---
title: "RDF vocabulary and namespace"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[iri-identity]]", "[[literal-datatyping]]"]
updated: 2026-08-09
---

# RDF vocabulary and namespace

## What it is

An RDF vocabulary is a set of IRIs used with a shared meaning — the terms (classes, properties, datatypes) that data authors reuse to say things. Those IRIs are conventionally grouped under a common namespace IRI, so a short local name appended to a namespace yields a full global identifier. Because vocabulary terms are just IRIs, the global-scope and stability rules that govern IRIs also govern how vocabularies denote things over time.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — Introduces RDF vocabularies and namespace IRIs as a core topic of the data model, alongside the referent of an IRI and change over time ⟨§1⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — By design IRIs have global scope, so two different appearances of an IRI denote the same resource, and an IRI once minted SHOULD never change its intended referent ⟨§1.3, §1.5⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Datatypes are denoted by one or more IRIs, and recognized datatype IRIs have fixed referents ⟨§5, §5.4⟩.

## Where sources differ

This concept is covered by a single source, rdf-11-concepts, so there is no divergence to report here.

## See also

[[rdf-data-model]] · [[iri-identity]] · [[literal-datatyping]]
