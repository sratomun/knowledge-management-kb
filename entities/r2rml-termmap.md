---
title: "rr:TermMap"
type: entity
subtype: vocabulary-term
aliases: ["R2RML term map"]
tags: [obda]
concepts: ["[[term-map]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:TermMap

## What it is
The R2RML vocabulary class for a term map: a function that generates an RDF term (IRI, blank node, or literal) from a logical table row. Subject, predicate, object, and graph maps are all kinds of term map.

## Key facts
- "A term map is a function that generates an RDF term from a logical table row"; the result is known as the term map's generated RDF term ⟨§7⟩
- A term map MUST be exactly one of the following: a constant-valued term map, a column-valued term map, or a template-valued term map ⟨§7⟩
- There are several kinds of term map depending on where they occur: subject maps, predicate maps, object maps and graph maps ⟨§7⟩

## Relations
- Realizes: [[term-map]]
- Defined in: [[r2rml]]
- Related: [[r2rml-subjectmap]], [[r2rml-predicatemap]], [[r2rml-objectmap]], [[r2rml-graphmap]], [[r2rml-constant]], [[r2rml-column]], [[r2rml-template]]

## See also
[[r2rml-termtype]] · [[org-w3c]]
