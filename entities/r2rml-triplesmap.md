---
title: "rr:TriplesMap"
type: entity
subtype: vocabulary-term
aliases: ["R2RML triples map"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:TriplesMap

## What it is
The R2RML vocabulary class for a triples map: the rule that maps each row of one logical table to RDF triples. It is the top-level building block of an R2RML mapping, which consists of one or more triples maps.

## Key facts
- "A triples map specifies a rule for translating each row of a logical table to zero or more RDF triples" ⟨§6⟩
- All RDF triples generated from one row in the logical table share the same subject ⟨§6⟩
- A triples map MUST have exactly one rr:logicalTable and exactly one subject map (via rr:subjectMap or the constant shortcut rr:subject), and MAY have zero or more rr:predicateObjectMap properties ⟨§6⟩

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[r2rml]]
- Related: [[r2rml-logicaltable]], [[r2rml-subjectmap]], [[r2rml-predicateobjectmap]]

## See also
[[r2rml-mapping-graph]] · [[org-w3c]]
