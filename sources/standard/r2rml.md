---
title: "R2RML: RDB to RDF Mapping Language"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: [R2RML, "RDB to RDF Mapping Language"]
publisher: W3C
url: https://www.w3.org/TR/r2rml/
version: "1.0"
published: 2012-09
effective_from: 2012-09-27
effective_to: ongoing
status: current
tags: [semantic-web, obda]
updated: 2026-08-09
---
# R2RML: RDB to RDF Mapping Language

## Scope & purpose
R2RML is a language for expressing customized mappings from relational databases to RDF datasets, letting a mapping author view existing relational data in the RDF data model using a structure and target vocabulary of their choice. Unlike the companion Direct Mapping, which mechanically reflects the database schema, R2RML mappings are highly customizable and are themselves RDF graphs written in Turtle syntax. The mapping is conceptual: a processor may materialize RDF dumps, offer a virtual SPARQL endpoint, or provide a Linked Data interface over the mapped data. It is a W3C Recommendation (27 September 2012) produced by the RDB2RDF Working Group.

## Structure
The specification is organized into eleven numbered sections plus appendices. §1 Introduction and conventions; §2 an informative overview and worked example (simple table, R2RML view, table linking, many-to-many, type-code translation); §3 Conformance (of mapping documents, mapping graphs, processors, data validators, default mapping generators); §4 R2RML processors and mapping documents (mapping graphs and the rr: vocabulary §4.1, Turtle syntax/media type §4.2, data errors §4.3, default mappings §4.4); §5 Defining logical tables (base tables/views §5.1, R2RML views §5.2); §6 Mapping logical tables with triples maps (subject maps §6.1, typing §6.2, predicate-object maps §6.3); §7 Creating RDF terms with term maps (constant §7.1, column §7.2, template §7.3, term type §7.4, language §7.5, datatype §7.6, inverse expressions §7.7); §8 Foreign-key relationships / referencing object maps; §9 Named graphs (blank-node scope §9.1); §10 Datatype conversions (§10.1–§10.5); §11 The output dataset (§11.1–§11.2). Appendix A RDF terminology, B index of vocabulary terms (classes, properties, other), C references, D acknowledgements.

## Key points
- R2RML expresses customized mappings from relational databases to RDF datasets; the mappings are themselves RDF graphs written in Turtle, and the output is an RDF dataset (as defined in SPARQL) using the author's target vocabulary ⟨§1⟩
- The mapping is conceptual: an R2RML processor, given an R2RML mapping and an input database, may materialize the output dataset, offer virtual access through an interface that queries the input database, or offer any other means of access ⟨§4⟩
- The key words must, must not, required, should, should not, recommended, may, and optional are to be interpreted as described in RFC 2119; the spec defines conformance for mapping documents, mapping graphs, processors, data validators, and default mapping generators, and targets databases conforming to Core SQL 2008 ⟨§3⟩
- A term map with term type rr:IRI that generates an invalid IRI, or a datatype-override that produces an ill-typed literal, is a data error; a processor MUST abort any operation that would inspect or return such a term and report an error, though the presence of data errors does not make a mapping non-conforming ⟨§4.3⟩
- A logical table is a SQL base table or view (represented by exactly one rr:tableName) or an R2RML view; every logical table has an effective SQL query, and for a base table that query is SELECT * FROM {table} ⟨§5.1⟩
- An R2RML view has exactly one rr:sqlQuery whose value is a valid SQL SELECT query; the result MUST NOT have duplicate column names, projected-expression columns SHOULD be named, and the view MAY carry one or more rr:sqlVersion identifiers (e.g. rr:SQL2008) ⟨§5.2⟩
- A triples map MUST have exactly one rr:logicalTable and exactly one subject map (via rr:subjectMap or the constant shortcut rr:subject), and MAY have zero or more rr:predicateObjectMap properties ⟨§6⟩
- A subject map MAY have one or more rr:class IRIs; for each generated subject an rdf:type triple with that class IRI as object is generated ⟨§6.2⟩
- A term map is a function generating an RDF term from a logical table row and MUST be exactly one of: a constant-valued term map (rr:constant), a column-valued term map (rr:column), or a template-valued term map (rr:template) ⟨§7⟩
- The constant shortcut properties rr:subject, rr:predicate, rr:object and rr:graph MUST be treated exactly as if the corresponding expanded rr:subjectMap/rr:predicateMap/rr:objectMap/rr:graphMap [ rr:constant … ] triples were present instead ⟨§7.1⟩
- A string template references column names in unescaped curly braces; when the term type is rr:IRI, R2RML always percent-encodes each data value into an IRI-safe version per the iunreserved production of RFC 3987 ⟨§7.3⟩
- rr:termType selects the generated kind (rr:IRI, rr:BlankNode, or rr:Literal); absent an explicit value the term type defaults to rr:Literal for an object map that is column-based or has rr:language or rr:datatype, and to rr:IRI otherwise ⟨§7.4⟩
- A datatypeable term map MAY have one rr:datatype to override the natural datatype; a term map MUST NOT have more than one rr:datatype value, and a term map that is not datatypeable MUST NOT have an rr:datatype property ⟨§7.6⟩
- An optional rr:inverseExpression (there MUST NOT be more than one per term map) lets a generated RDF term be "reversed" into a SQL query that efficiently retrieves the source logical table row, enabling use of indexes ⟨§7.7⟩
- A referencing object map reuses the subjects of a parent triples map (rr:parentTriplesMap) as objects and MAY carry rr:joinCondition values (each with rr:child and rr:parent); if the child and parent queries are not identical, the referencing object map MUST have at least one join condition ⟨§8⟩
- Any subject map or predicate-object map MAY have graph maps (rr:graphMap or the shortcut rr:graph); the special IRI rr:defaultGraph targets the default graph, and by default all triples are placed in the default graph ⟨§9⟩
- The natural mapping converts all predefined Core SQL 2008 datatypes except INTERVAL to corresponding XML Schema datatypes (e.g. INTEGER→xsd:integer, TIMESTAMP→xsd:dateTime), falling back to a cast-to-string plain literal for unsupported types ⟨§10.2⟩

## Concepts & entities covered
Concepts: [[rdb-to-rdf-mapping]] · [[term-map]] · [[iri-templating]] · [[named-graph-assignment]] · [[logical-source-abstraction]]
Entities: [[r2rml-triplesmap]] · [[r2rml-logicaltable]] · [[r2rml-basetableorview]] · [[r2rml-r2rmlview]] · [[r2rml-termmap]] · [[r2rml-subjectmap]] · [[r2rml-predicatemap]] · [[r2rml-objectmap]] · [[r2rml-predicateobjectmap]] · [[r2rml-refobjectmap]] · [[r2rml-join]] · [[r2rml-graphmap]] · [[r2rml-template]] · [[r2rml-column]] · [[r2rml-constant]] · [[r2rml-termtype]] · [[r2rml-inverseexpression]] · [[r2rml-sql2008]] · [[r2rml-defaultgraph]] · [[r2rml-mapping-document]] · [[r2rml-mapping-graph]] · [[r2rml-direct-mapping]]
