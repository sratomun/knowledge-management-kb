---
title: "Ontology-Based Data Access"
type: concept
tags: [obda]
aliases: []
related: ["[[virtual-knowledge-graph]]", "[[query-rewriting]]", "[[query-unfolding]]", "[[first-order-rewritability]]", "[[rdb-to-rdf-mapping]]"]
updated: 2026-08-10
---

# Ontology-Based Data Access

## What it is
A data-access paradigm in which end users query existing data sources through a high-level, conceptual ontology vocabulary instead of the underlying database schema. A declarative specification links the ontology to the sources so that queries posed against the ontology are answered over the live data, typically without materializing the data as RDF.

## How sources treat it
- **[[xiao-obda-survey]]** _(article · informational)_ — OBDA lets end users query data through a conceptual, business-level ontology vocabulary rather than the underlying database schema ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — an OBDA specification is a triple ⟨ontology (TBox), mapping, data source⟩ layered over existing relational sources ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — mappings associate SQL queries over the source with assertions over the ontology vocabulary, and the W3C R2RML standard is a common mapping language ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — user queries are typically SPARQL (or conjunctive queries) posed against the ontology, under certain-answer semantics ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[r2rml]]** _(standard · normative)_ — supplies a language for the mapping component: customized mappings from relational databases to RDF whose processor may offer virtual access through an interface that queries the input database ⟨§4⟩
- **[[rml]]** _(standard · normative)_ — extends the mapping component beyond relational databases, expressing mappings from heterogeneous sources (databases, CSV, TSV, XML, JSON) to RDF while remaining backward-compatible with R2RML ⟨§1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the guiding idea is efficient access to large data through a high-level conceptual interface: the conceptual view is a DL-Lite TBox, the relational data an ABox, and positive existential queries over (T, A) are rewritten into standard first-order queries over the database ⟨§9⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the approach is viable because for a number of DL-Lite logics query answering is in AC0 for data complexity; it has been implemented in QuOnto (over ontology-to-relational mappings against any RDBMS) and Owlgres ⟨§1, §9⟩
- **[[ontop-swj]]** _(article · informational)_ — in OBDA a conceptual ontology layer defines a shared vocabulary, models the domain, hides the structure of the data sources, and enriches incomplete data with background knowledge, so users pose queries over the high-level view without needing to understand the sources or their encodings ⟨§1⟩
- **[[ontop-swj]]** _(article · informational)_ — the ontology is connected to the data sources through a declarative specification of mappings that relate ontology classes and properties to (SQL) views over the data, and the ontology together with the mappings exposes a virtual RDF graph queried with SPARQL ⟨§1⟩
- **[[ontop-swj]]** _(article · informational)_ — the virtual approach avoids materialization and profits from more than 30 years' maturity of relational systems; OBDA systems are set up over existing relational datasources, requiring no ETL process, unlike triplestores ⟨§1⟩⟨§6⟩

## Where sources differ
The survey frames OBDA as a whole paradigm — an ontology/mapping/data-source triple with rewriting-based query answering over relational sources ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩. R2RML and RML describe only the mapping component and do not themselves define the ontology layer or query-rewriting semantics; the survey names R2RML as the common mapping language in that setting ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩, while RML generalizes the mapping component to non-relational sources ⟨rml §1⟩. The DL-Lite family paper approaches OBDA from the logic/complexity side: it models the stored data directly as an ABox and studies exactly which DL-Lite constructs keep query answering first-order rewritable (AC0), rather than detailing the mapping language ⟨dl-lite-short-course §1, §9⟩. The Ontop system paper takes the engineering perspective: it presents OBDA as a concrete, W3C-standards-based system (SPARQL, R2RML, OWL 2 QL, RDFS) with a four-layer architecture, and stresses the contrast with triplestore ETL/materialization ⟨ontop-swj §2⟩⟨ontop-swj §6⟩.

## See also
[[virtual-knowledge-graph]] · [[query-rewriting]] · [[query-unfolding]] · [[rdb-to-rdf-mapping]]
