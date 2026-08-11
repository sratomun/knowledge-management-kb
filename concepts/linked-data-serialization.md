---
title: "Linked Data serialization"
type: concept
tags: [semantic-web]
related: ["[[linked-data]]", "[[rdf-dataset]]", "[[rdf-data-model]]", "[[iri-identity]]"]
updated: 2026-08-09
---

# Linked Data serialization

## What it is

A Linked Data serialization is a concrete syntax for writing RDF down so that it can be exchanged, stored, and processed — turning the abstract graph model into bytes on the wire. A single abstract dataset can be serialized in several equivalent forms, and a well-designed serialization aims to fit into tooling that authors already use. JSON-LD is one such serialization, expressing RDF as ordinary JSON.

## How sources treat it

- **[[json-ld-11]]** _(standard · normative)_ — JSON-LD is a lightweight syntax to serialize Linked Data in JSON, and a JSON-LD document is always a valid JSON document so that standard JSON libraries work with it ⟨§1⟩ ⟨§1.5⟩.
- **[[json-ld-11]]** _(standard · normative)_ — JSON-LD is a concrete RDF syntax: a JSON-LD document is both an RDF document and a JSON document ⟨§10⟩.
- **[[json-ld-11]]** _(standard · normative)_ — It defines four forms of a document — expanded, compacted, flattened, and framed — for different processing needs ⟨§5.1⟩ ⟨§5.3⟩ ⟨§5.4⟩.
- **[[json-ld-11]]** _(standard · normative)_ — Setting the processing mode explicitly to `json-ld-1.1` is RECOMMENDED to prevent a 1.0 processor from producing different results ⟨§4.1.1⟩.
- **[[json-ld-11]]** _(standard · normative)_ — JSON-LD can be embedded in HTML by placing it in a `script` element with the `type` attribute set to `application/ld+json`, creating a data block ⟨§7⟩.

## Where sources differ

This concept is covered by a single source, json-ld-11. Within that document, JSON-LD situates itself among other Linked Data serializations (Turtle, RDFa, Microdata) in its appendix on relationships to other formats ⟨§B⟩, but the KB records no second source's treatment here.

## See also

[[linked-data]] · [[rdf-dataset]] · [[rdf-data-model]] · [[iri-identity]]
