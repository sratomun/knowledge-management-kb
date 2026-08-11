---
title: "Ontop — Virtual Knowledge Graph System (Guide)"
type: source
kind: provider-doc
authority: vendor
subtype: system-documentation
aliases: ["Ontop guide", "Ontop documentation"]
publisher: Ontop
url: https://ontop-vkg.org/guide/
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [obda]
updated: 2026-08-10
---

# Ontop — Virtual Knowledge Graph System (Guide)

## Scope & purpose
The official Ontop guide documents Ontop, an open-source Virtual Knowledge Graph
(VKG) / Ontology-Based Data Access (OBDA) engine that exposes arbitrary relational
databases as virtual RDF graphs and answers SPARQL queries by translating them into
SQL run on the underlying data source. It is vendor documentation covering the
system's concepts, mapping languages, standards compliance, and deployment model.

## Structure
The guide is a multi-page manual. Core conceptual pages captured here: the
Introduction (what Ontop is, features, versions), Key concepts (VKG, RDF, SPARQL,
mappings, ontology, VKG specification, SPARQL endpoint), Getting started
(deployment, CLI, materialization), the Ontop Mapping Language reference (native
`.obda` syntax), Standards compliance (SPARQL 1.1, GeoSPARQL, R2RML, RDF 1.1,
OWL 2 QL, RDFS), and the Glossary.

## Key points
- Ontop is a Virtual Knowledge Graph system that exposes the content of arbitrary relational databases as RDF knowledge graphs while the data remains in the sources instead of being moved ⟨guide: introduction⟩.
- Ontop translates SPARQL queries expressed over the virtual graph into SQL queries that are executed by the relational data sources ⟨guide: concepts/SPARQL query⟩.
- Ontop supports two mapping languages: the W3C R2RML standard and its own native Ontop mapping language, which is fully interoperable with R2RML ⟨guide: concepts/Mappings⟩.
- A native Ontop (OBDA) mapping is a `.obda` text file with a `PrefixDeclaration` section and a `MappingDeclaration` of assertions, each assertion having three fields — `mappingId`, a `source` SQL query, and a `target` triple template referencing the query's columns ⟨guide: mapping-language⟩.
- The mapping `target` uses an adaptation of Turtle subject-predicate-object syntax, with IRI/blank-node/literal terms as constants, templates with `{column}` placeholders, or bare columns; the special predicate `a` stands for `rdf:type` ⟨guide: mapping-language/Target Triple Structure⟩.
- IRI and blank-node templates apply IRI-safe percent-encoding to their column values following the R2RML standard, whereas IRI columns are passed through untransformed and must already be valid IRIs ⟨guide: mapping-language/IRI or Blank Node Template⟩.
- The native mapping supports Turtle-style compact predicate lists (`;`) and object lists (`,`), named graphs via the `GRAPH` keyword, explicit literal typing (`^^`), constant language tags (`@`), and meta-mappings where class/property names are built dynamically from the database ⟨guide: mapping-language/Compact Form⟩.
- Ontop supports lightweight ontologies expressed in RDFS or in the slightly more expressive OWL 2 QL fragment of OWL, used to enrich the graph (e.g. class hierarchies) ⟨guide: concepts/Ontology⟩.
- A VKG specification is composed of mappings and, optionally, ontologies ⟨guide: concepts/VKG specification⟩.
- Ontop uses RDF 1.1 as its graph data model, typing simple literals as `xsd:string` and language-tagged literals as `rdf:langString` ⟨guide: compliance/RDF 1.1⟩.
- Ontop supports a large fragment of SPARQL 1.1 — including all query forms, aggregates, subqueries, and negation — but does not support SERVICE federated queries and covers only 5 of 8 property-path constructs ⟨guide: compliance/SPARQL 1.1⟩.
- Ontop is almost fully compliant with R2RML but does not support base IRIs, R2RML default-mapping generation, or normalization of binary SQL datatypes ⟨guide: compliance/R2RML⟩.
- Ontop can materialize virtual graphs into RDF files (an alternative to virtual query answering) via its command-line interface ⟨guide: introduction/Main features⟩.
- A VKG specification can be deployed as a standardized HTTP-based SPARQL endpoint (and, since 4.1.0, as a predefined query endpoint) queryable by any HTTP client ⟨guide: concepts/SPARQL endpoint⟩.
- Ontop's SQL parser only parses simple SQL source queries (no unions, aggregations, or order by); non-parsed queries are treated as black-box views sent directly to the database, limiting the optimizations Ontop can apply ⟨guide: mapping-language/Source Query⟩.
- Ontop is backed by the Free University of Bozen-Bolzano and Ontopic s.r.l., is released under the Apache 2.0 license, and its current stable release is 5.5.0 (February 2026) ⟨guide: introduction/Organizations⟩.

## Concepts & entities covered
Concepts: [[ontology-based-data-access]] · [[virtual-knowledge-graph]] · [[rdb-to-rdf-mapping]] · [[query-unfolding]]
Entities: [[ontop]] · [[ontop-native-mapping]]
