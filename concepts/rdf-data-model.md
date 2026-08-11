---
title: "RDF data model"
type: concept
tags: [semantic-web]
related: ["[[iri-identity]]", "[[literal-datatyping]]", "[[blank-node]]", "[[rdf-dataset]]", "[[entailment-equivalence]]", "[[rdf-vocabulary-namespace]]", "[[linked-data-serialization]]"]
updated: 2026-08-09
---

# RDF data model

## What it is

The RDF data model is an abstract, graph-based way of representing information as a set of statements. Each statement is a triple of subject, predicate, and object, and the nodes of the resulting graph are drawn from three kinds of term: globally-named things (IRIs), data values (literals), and anonymous nodes (blank nodes). Because the model is abstract, the same graph can be written down in many concrete syntaxes and targeted by many mapping and vocabulary specifications; those other specifications conform to the model rather than to any single serialization.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — Defines the model: an RDF graph is a set of RDF triples, each consisting of a subject, a predicate, and an object, and there can be three kinds of nodes — IRIs, literals, and blank nodes — collectively known as RDF terms, which are distinct and distinguishable ⟨§1.1, §3, §3.1⟩.
- **[[json-ld-11]]** _(standard · normative)_ — A JSON-LD document is both an RDF document and a JSON document; JSON-LD is a concrete RDF syntax and extends the RDF data model to optionally serialize generalized RDF Datasets (properties may be IRIs or blank nodes) ⟨§10⟩.
- **[[r2rml]]** _(standard · normative)_ — Lets a mapping author view existing relational data in the RDF data model using a structure and target vocabulary of their choice; the output is an RDF dataset ⟨§1⟩.
- **[[rml]]** _(standard · normative)_ — Expresses customized mappings from heterogeneous data structures and serializations (databases, CSV, TSV, XML, JSON) into the RDF data model ⟨§1⟩.
- **[[skos]]** _(standard · normative)_ — SKOS data are expressed as RDF triples and may be encoded in any concrete RDF syntax (RDF/XML, Turtle, etc.) ⟨§1.2⟩.
- **[[prov-o]]** _(standard · normative)_ — A `prov:Bundle` of PROV-O assertions is an abstract set of RDF triples, and adding or removing a triple creates a new distinct Bundle ⟨§3.2⟩.
- **[[dcat-3]]** _(standard · normative)_ — DCAT is an RDF vocabulary; it is recommended that instances of the DCAT main classes have a global identifier (IRI), and use of blank nodes is generally discouraged when encoding DCAT in RDF ⟨§5.2⟩.

## Where sources differ

Only rdf-11-concepts defines the model; the other sources consume or target it and vary in how far they lean on it. json-ld-11 and rml both extend the model toward "generalized" RDF (allowing blank nodes or literals in positions standard RDF forbids), whereas rdf-11-concepts marks generalized RDF triples, graphs, and datasets as non-normative and requires no tool to accept them ⟨§7⟩. On blank nodes the sources take different postures: rdf-11-concepts admits them as one of the three node kinds ⟨§3.1⟩, while dcat-3 generally discourages their use when encoding DCAT ⟨§5.2⟩. skos additionally notes that its data are simply RDF triples encodable in any concrete syntax ⟨§1.2⟩. These are descriptions of scope, not rankings.

## See also

[[iri-identity]] · [[literal-datatyping]] · [[blank-node]] · [[rdf-dataset]] · [[entailment-equivalence]] · [[rdf-vocabulary-namespace]] · [[linked-data-serialization]]
