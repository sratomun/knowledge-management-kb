---
title: "R2RML Mapping Graph"
type: entity
subtype: specification-construct
aliases: ["R2RML mapping graph"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# R2RML Mapping Graph

## What it is
The RDF graph that represents an R2RML mapping. R2RML uses RDF not only as the target data model but also as the formalism for expressing the mapping itself.

## Key facts
- "An RDF graph that represents an R2RML mapping is called an R2RML mapping graph" ⟨§4.1⟩
- The R2RML vocabulary is the set of IRIs defined in the specification that start with the rr: namespace IRI, http://www.w3.org/ns/r2rml# ⟨§4.1⟩
- A mapping graph SHOULD NOT include IRIs that start with the rr: namespace but are not defined in the R2RML vocabulary, and MAY contain arbitrary additional triples whose terms are not from the R2RML vocabulary ⟨§4.1⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-mapping-document]], [[r2rml-triplesmap]]

## See also
[[r2rml-termmap]] · [[org-w3c]]
