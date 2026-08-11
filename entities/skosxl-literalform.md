---
title: "skosxl:literalForm"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skosxl:literalForm

## What it is
The datatype property giving the literal form of a skosxl:Label — an RDF plain literal (a string of UNICODE characters and an optional language tag).

## Key facts
- skosxl:literalForm is an instance of owl:DatatypeProperty ⟨S49⟩.
- The rdfs:domain of skosxl:literalForm is the class skosxl:Label ⟨S50⟩ and its rdfs:range is the class of RDF plain literals ⟨S51⟩.
- An instance of skosxl:Label has a single literal form; the function mapping labels to literals is neither injective nor surjective, so two labels sharing a literal form do not entail owl:sameAs ⟨B.2.4.1⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skosxl-label]]

## See also
[[skosxl-label]]
