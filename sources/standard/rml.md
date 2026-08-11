---
title: "RML: RDF Mapping Language"
type: source
kind: standard
authority: normative
subtype: community-group-spec
aliases: ["RML", "RDF Mapping Language"]
publisher: W3C Knowledge Graph Construction Community Group
url: https://rml.io/specs/rml/
version: "1.0 (2015); CG draft"
published: 2015-09
effective_from: 2015-09
effective_to: ongoing
status: current
tags: [semantic-web, obda]
updated: 2026-08-09
---

# RML: RDF Mapping Language

## Scope & purpose

RML is a generic mapping language for expressing customized rules that map heterogeneous data structures and serializations (CSV, TSV, XML, JSON, and relational databases) into the RDF data model ⟨§1⟩. It is defined as a **superset of the W3C-standardized [R2RML]**, generalizing R2RML — which maps only relational databases to RDF — to any structured source, while remaining backward-compatible with it ⟨Abstract, §1⟩. RML uses exactly the same syntax as R2RML, so RML mappings are themselves RDF graphs ⟨Abstract⟩.

This document is a **W3C Community Group product, not a W3C Recommendation**: it is labelled an "Unofficial Draft" that "has no official standing of any kind and does not represent the support or consensus of any standards organization" ⟨Status of This Document⟩. It covers the *original* RML specification (v1.1.2); the Knowledge Graph Construction W3C Community Group is developing a newer version at https://w3id.org/rml/ ⟨Abstract⟩. The RML vocabulary namespace is `http://semweb.mmlab.be/ns/rml#` ⟨§2⟩.

## Structure

- §1 Overview (incl. §1.1 Conformance)
- §2 RML Vocabulary
- §3 RML Overview and Examples (CSV §3.1, XML §3.2, JSON §3.3)
- §4 Defining Logical Sources (§4.1 Base Sources)
- §5 Mapping Logical Sources to RDF with Triples Maps (subject maps §5.2, typing §5.3, predicate-object maps §5.4)
- §6 Creating RDF Terms with Term Maps (constant §6.1, reference §6.2, template §6.3, term type §6.4, language §6.5, datatype §6.6)
- §7 Relationships among Logical Sources (referencing object maps / joins)
- §8 Named Graphs
- §9 Integrated mapping (worked multi-source example)
- §10 Index of RML Vocabulary Terms (classes §10.1, properties §10.2, other terms §10.3)
- §11 Changelog; §A References

## Key points

- RML expresses customized mappings from heterogeneous data structures and serializations to the RDF data model, currently defined for structured formats — databases (as in R2RML), CSV, TSV, XML, and JSON ⟨§1⟩.
- RML **is based on and extends [R2RML]**; whereas R2RML expresses mappings only from relational databases, an RML mapping is not tied to a database schema and can be defined for data in any source format ⟨§1⟩.
- RML keeps R2RML's mapping definitions but **excludes R2RML's database-specific references from the core model**, providing a generic definition transferable to other data structures — "a generic approach combined with case-specific extensions" that "always remains backward compatible with R2RML" ⟨§1⟩.
- An RML mapping consists of one or more **triples maps**; its input is the input data source and its output is an RDF dataset (the output dataset) ⟨§2⟩. A triples map in RML **is defined as a triples map in R2RML** (`rr:TriplesMap`) ⟨§5, §2⟩.
- The RML vocabulary defines RML-specific classes but **also includes all [R2RML] classes**; e.g. R2RML's `rr:BaseTableOrView` is a subclass of `rml:BaseSource` ⟨§2⟩.
- A **logical source** (`rml:LogicalSource`) extends R2RML's logical table; it must be a base source (`rml:BaseSource`) pointing to the data to be mapped ⟨§3, §4, §4.1⟩.
- A base source is a resource with **exactly one** `rml:source`, **exactly one** logical iterator `rml:iterator`, and **zero or one** `rml:referenceFormulation` ⟨§4.1⟩ — this replaces R2RML's database-only table/query addressing.
- The **reference formulation** (`rml:referenceFormulation`) defines how references address elements of the source and **should always be specified** via `rml:referenceFormulation`; for relational databases `rr:sqlVersion` may be used instead to stay backwards-compliant with R2RML ⟨§4.1⟩. Examples: `rr:SQL2008`, `ql:XPath` (XML), `ql:JSONPath` (JSON) ⟨§4.1⟩.
- The **logical iterator** (`rml:iterator`) defines the iteration loop; the default iterator is the "row" for databases/CSV/TSV, an element for XML, and an object for JSON — a generalization not present in R2RML, which iterates rows only ⟨§4.1⟩.
- A term map **must be exactly one of** a constant-valued (`rr:constant`), reference-valued (`rml:reference`), or template-valued (`rr:template`) term map ⟨§6⟩; RML replaces R2RML's column-only `rr:column` with the format-agnostic `rml:reference` ⟨§6.2⟩.
- A reference (`rml:reference`) refers to a column (databases), a record (CSV/TSV), an element (XML), or an object (JSON), and **must be a valid expression** per the specified reference formulation (e.g. a valid XPath or JSONPath expression) ⟨§6.2⟩.
- A **string template** (`rr:template`) builds strings from components by enclosing references in curly braces; there **should be at least one pair of unescaped curly braces**, and if the term type is `rr:IRI` the value is replaced with an IRI-safe version ⟨§6.3⟩.
- RML adds a **language map** (`rml:languageMap`), whose value must be a term map generating a language tag; precedence: a valid language-map value, else `rr:language`, else no language ⟨§6.5⟩ — this extends R2RML's fixed `rr:language` tag.
- A **referencing object map** uses the subjects of another (parent) triples map as objects; if the child and parent logical sources are **not identical, it must have at least one join condition** (`rr:joinCondition` with `rr:child` / `rr:parent`) ⟨§7⟩.
- Named graphs are supported via `rr:graphMap` / `rr:graph`; if a graph map generates `rr:defaultGraph`, the target is the default graph, and **blank nodes are scoped to a single RDF graph** and can never be shared across graphs ⟨§8, §8.2⟩.
- An RML processor may optionally include an **RML data validator** (which **must report any data errors** raised while generating the output) or an **RML default mapping generator** that introspects the source, but neither is required ⟨§2⟩.

## Concepts & entities covered

Concepts: [[rdb-to-rdf-mapping]] · [[logical-source-abstraction]] · [[reference-formulation]] · [[term-map]]
Entities: [[rml-logicalsource]] · [[rml-source]] · [[rml-referenceformulation]] · [[rml-iterator]] · [[rml-reference]] · [[rml-languagemap]] · [[ql-csv]] · [[ql-xpath]] · [[ql-jsonpath]]
