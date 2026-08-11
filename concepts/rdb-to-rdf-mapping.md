---
title: "RDB-to-RDF Mapping"
type: concept
tags: [semantic-web]
related: ["[[term-map]]", "[[iri-templating]]", "[[named-graph-assignment]]", "[[logical-source-abstraction]]", "[[reference-formulation]]", "[[ontology-based-data-access]]"]
updated: 2026-08-10
---

# RDB-to-RDF Mapping

## What it is
The activity of expressing rules that transform data held in a source (classically a relational database) into RDF, so that existing tabular data can be viewed and queried in the RDF data model under a vocabulary chosen by the mapping author. A mapping is a declarative artifact — often itself an RDF graph — that a processor can use either to materialize an RDF dump or to offer virtual access over the source without copying the data.

## How sources treat it
- **[[r2rml]]** _(standard · normative)_ — expresses customized mappings from relational databases to RDF datasets; the mappings are themselves RDF graphs written in Turtle, and the output is an RDF dataset using the author's target vocabulary ⟨§1⟩
- **[[r2rml]]** _(standard · normative)_ — the mapping is conceptual: a processor, given a mapping and an input database, may materialize the output dataset, offer virtual access through an interface that queries the input database, or offer any other means of access ⟨§4⟩
- **[[rml]]** _(standard · normative)_ — expresses customized mappings from heterogeneous data structures and serializations to the RDF data model, currently defined for databases (as in R2RML), CSV, TSV, XML, and JSON ⟨§1⟩
- **[[rml]]** _(standard · normative)_ — is based on and extends R2RML; whereas R2RML expresses mappings only from relational databases, an RML mapping is not tied to a database schema and can be defined for data in any source format ⟨§1⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — mappings associate SQL queries over the source with assertions over the ontology vocabulary, and the W3C R2RML standard is a common mapping language for this ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[ontop-swj]]** _(article · informational)_ — a mapping assertion consists of a source (an SQL query retrieving values from the database) and a target (RDF triples built from those values, with IRI templates such as :db1/{pid} filled from source attributes) ⟨§2.1⟩
- **[[ontop-swj]]** _(article · informational)_ — Ontop supports two mapping languages, the W3C R2RML standard and an easier-to-learn native Ontop mapping language, and can convert native mappings into R2RML and vice versa ⟨§2.1⟩
- **[[ontop-swj]]** _(article · informational)_ — mapping bootstrappers (Ontop's own, plus MIRROR, BootOX, Karma) automatically generate mappings from database schemas, most following the W3C Direct Mapping, which is a default recipe for RDF triples from SQL rather than a mapping in itself ⟨§3.1⟩

## Where sources differ
R2RML scopes the source to relational databases only, addressing data via SQL base tables, views, and SQL queries ⟨r2rml §5.1⟩. RML keeps R2RML's mapping definitions but excludes R2RML's database-specific references from the core model, generalizing the same syntax to heterogeneous sources (CSV, TSV, XML, JSON, and databases) while remaining backward-compatible with R2RML ⟨rml §1⟩. The OBDA survey treats such mappings as one ingredient of a larger access paradigm over relational sources, rather than as a standalone materialization language ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩. The Ontop system paper treats the mapping component as an engineering surface — offering both R2RML and a native syntax, bootstrapping tools, and the Direct Mapping — and compiles the ontology hierarchy into the mappings as T-mappings for query answering ⟨ontop-swj §2.1, §3.1, §4.1⟩.

## See also
[[logical-source-abstraction]] · [[term-map]] · [[ontology-based-data-access]]
