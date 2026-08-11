---
title: "Ontop"
type: entity
subtype: system
aliases: []
tags: [obda]
concepts: ["[[ontology-based-data-access]]", "[[virtual-knowledge-graph]]"]
sources: ["[[xiao-obda-survey]]", "[[ontop-swj]]", "[[ontop-guide]]"]
updated: 2026-08-10
---

# Ontop

## What it is
Ontop is a mature open-source ontology-based data access system, developed at the Free
University of Bozen-Bolzano and released under the Apache license, that answers SPARQL
queries over relational databases as a virtual RDF graph, without materializing the data
as RDF.

## Key facts
- Ontop is one of the mature OBDA systems that implement virtual query answering over relational databases ⟨IJCAI 2018, pp. 5511-5519⟩.
- Ontop exposes relational sources as a virtual knowledge graph, keeping data in the source and accessing it on demand ⟨IJCAI 2018, pp. 5511-5519⟩.
- Ontop answers queries by rewriting them against the ontology and unfolding them into SQL over the source ⟨IJCAI 2018, pp. 5511-5519⟩.
- Ontop exposes relational databases as virtual RDF graphs by linking ontology classes and properties to the sources through mappings, then translating SPARQL into SQL transparently to the user ⟨ontop-swj §2⟩.
- To the authors' knowledge, Ontop is the first OBDA system to support all the W3C recommendations related to OBDA — OWL 2 QL, R2RML, SPARQL, SWRL, and the OWL 2 QL entailment regime in SPARQL — plus all major relational databases via JDBC ⟨ontop-swj §2.1⟩.
- Ontop's architecture has four layers — inputs (ontology, mappings, queries, databases), the core, the API layer (OWL API and Sesame/SAIL), and the application layer (Protégé plugin, Sesame Workbench SPARQL endpoint, Optique Platform) ⟨ontop-swj §2⟩.
- Ontop supports two mapping languages, the W3C R2RML standard and an easier-to-use native Ontop mapping language, and can convert between them ⟨ontop-swj §2.1⟩.
- The core of Ontop is the SPARQL engine Quest, which rewrites SPARQL over the virtual RDF graph into SQL over the relational database ⟨ontop-swj §2.2⟩.
- Query answering splits into an off-line stage (ontology classification, T-mapping construction, and T-mapping optimization) and an online stage that translates SPARQL into optimized SQL exploiting the T-mappings and database integrity constraints ⟨ontop-swj §4⟩⟨ontop-swj §4.1⟩.
- Ontop's performance depends more on the complexity of the ontology and mappings than on the dataset size, consistent with the worst-case exponential SPARQL-to-SQL translation; it outperforms competitors by orders of magnitude on BSBM/FishMark/LUBM but can be beaten by Stardog when the generated SQL is a union of many sub-queries (NPD Benchmark) ⟨ontop-swj §4.2.4⟩.
- Ontop is the core of the Optique Platform and is deployed in industrial use cases at Statoil (the EPDS database of 1500+ tables) and Siemens Energy (~100 TB of timestamped sensor data) ⟨ontop-swj §5⟩.
- The vendor guide states Ontop translates SPARQL queries over the virtual graph into SQL executed by the relational data sources, and supports both the W3C R2RML standard and its native Ontop mapping language, which are fully interoperable ⟨guide: concepts/Mappings⟩.
- The guide states Ontop supports lightweight ontologies expressed in RDFS or in the slightly more expressive OWL 2 QL fragment of OWL ⟨guide: concepts/Ontology⟩.
- Besides virtual query answering, Ontop can materialize the virtual graph into RDF files via its command-line interface ⟨guide: introduction/Main features⟩.
- Per the guide, Ontop uses RDF 1.1 as its graph data model and can be deployed as a standardized HTTP SPARQL endpoint ⟨guide: compliance/RDF 1.1⟩⟨guide: concepts/SPARQL endpoint⟩.
- The guide states Ontop is backed by the Free University of Bozen-Bolzano and Ontopic s.r.l. and is released under the Apache 2.0 license, with current stable release 5.5.0 (February 2026) ⟨guide: introduction/Organizations⟩.

## Relations
- Realizes: [[ontology-based-data-access]]
- Realizes: [[virtual-knowledge-graph]]
- Defined in: [[xiao-obda-survey]]
- Defined in: [[ontop-swj]]
- Uses: [[t-mappings]] · [[tree-witness-rewriting]] · [[ontop-native-mapping]]
- Developed by: [[org-ontopic]]
- Implements W3C standards ([[org-w3c]]): R2RML, SPARQL, RDF 1.1, OWL 2 QL
- Related: [[mastro]] · [[morph]] · [[perfectref]]

## See also
[[mastro]] · [[morph]] · [[r2rml]] · [[t-mappings]] · [[owl2-ql]] · [[ontop-native-mapping]]
