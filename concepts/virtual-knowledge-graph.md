---
title: "Virtual Knowledge Graph"
type: concept
tags: [obda]
related: ["[[ontology-based-data-access]]", "[[query-rewriting]]", "[[query-unfolding]]"]
updated: 2026-08-10
---

# Virtual Knowledge Graph

## What it is
An integrated graph view over one or more data sources that is not physically materialized: the graph exists only as a mapping and ontology over data that stays in its original store and is accessed on demand at query time. Users see and query a knowledge graph, but the triples are computed from the underlying source rather than stored.

## How sources treat it
- **[[xiao-obda-survey]]** _(article · informational)_ — the ontology is a virtual, integrated view: data is not materialized as RDF but stays in the relational source and is accessed on demand — a "virtual knowledge graph" ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — mature OBDA systems include Ontop, Mastro, and Morph, which implement virtual query answering over relational databases ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — OBDA has been applied in data integration and industrial settings (e.g. energy and manufacturing use cases) where users query heterogeneous relational data through a shared ontology ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[ontop-swj]]** _(article · informational)_ — the ontology together with the mappings exposes a virtual RDF graph, which can be materialized to RDF triples for a triplestore or kept virtual and queried only during query execution; Ontop takes the virtual approach ⟨§1⟩
- **[[ontop-swj]]** _(article · informational)_ — Ontop exposes relational databases as virtual RDF graphs by linking ontology classes and properties to the sources through mappings, then translating SPARQL over the virtual graph into SQL over the database ⟨§2⟩
- **[[ontop-swj]]** _(article · informational)_ — exposing the database as a virtual RDF graph queried with SPARQL avoids the intermediate ETL process that triplestores require to load triples generated from external relational sources ⟨§6⟩

## Where sources differ
Both the OBDA survey and the Ontop system paper present the virtual knowledge graph as the on-demand, non-materialized face of the OBDA triple, realized by systems such as Ontop, Mastro, and Morph ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩⟨ontop-swj §2⟩. The survey states the idea at the paradigm level, whereas the Ontop paper frames it concretely against triplestores: keeping the graph virtual avoids the ETL/materialization step, while a materialized alternative is explicitly available ⟨ontop-swj §1, §6⟩.

## See also
[[ontology-based-data-access]] · [[query-rewriting]] · [[query-unfolding]]
