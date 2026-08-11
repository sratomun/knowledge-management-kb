---
title: "Lexical labeling"
type: concept
tags: [knowledge-organization]
related: ["[[notation]]", "[[concept-scheme]]", "[[semantic-relation]]"]
updated: 2026-08-09
---

# Lexical labeling

## What it is

Lexical labeling is the practice of attaching human-readable names to a concept: a single preferred label, any number of alternate labels (synonyms, abbreviations, spelling variants), and hidden labels used only for retrieval. Labels are what let people, rather than machines, recognize and search for a concept, distinct from any code or identifier assigned to it.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — Lexical labels (`skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel`) are each `owl:AnnotationProperty` and sub-properties of `rdfs:label` (S10, S11), with range the class of RDF plain literals (S12) ⟨§5⟩
- **[[skos]]** _(standard · normative)_ — Integrity conditions on labels: `skos:prefLabel`, `skos:altLabel` and `skos:hiddenLabel` are pairwise disjoint properties (S13), and "A resource has no more than one value of skos:prefLabel per language tag" (S14) ⟨§5.4⟩
- **[[skos]]** _(standard · normative)_ — The optional SKOS-XL extension reifies labels as instances of `skosxl:Label`, each with exactly one `skosxl:literalForm` (S52); two labels with the same literal form are not necessarily the same individual ⟨App. B⟩

## Where sources differ

Among the ingested sources, only SKOS defines lexical labeling of concepts. No divergence to report.

## See also
[[notation]] · [[concept-scheme]] · [[semantic-relation]]
