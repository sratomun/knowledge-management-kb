---
title: "rr:PredicateObjectMap"
type: entity
subtype: vocabulary-term
aliases: ["R2RML predicate-object map"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:PredicateObjectMap

## What it is
The R2RML vocabulary class that pairs predicate maps with object (or referencing object) maps. Combined with a triples map's subject map, it produces the predicate-object pairs of the generated triples.

## Key facts
- "A predicate-object map is a function that creates one or more predicate-object pairs for each logical table row of a logical table"; it is used with a subject map to generate RDF triples in a triples map ⟨§6.3⟩
- It references one or more predicate maps (rr:predicateMap or shortcut rr:predicate) and one or more object maps or referencing object maps (rr:objectMap or shortcut rr:object) ⟨§6.3⟩
- Any predicate-object map MAY have one or more associated graph maps ⟨§9⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-predicatemap]], [[r2rml-objectmap]], [[r2rml-refobjectmap]], [[r2rml-graphmap]]

## See also
[[r2rml-triplesmap]] · [[org-w3c]]
