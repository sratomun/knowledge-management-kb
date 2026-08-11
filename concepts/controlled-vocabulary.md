---
title: "Controlled vocabulary"
type: concept
tags: [knowledge-organization]
related: ["[[concept-scheme]]", "[[vocabulary-encoding-scheme]]", "[[semantic-relation]]"]
updated: 2026-08-09
---

# Controlled vocabulary

## What it is

A controlled vocabulary is a curated, managed set of terms or concepts used to describe, index, or tag resources consistently, in place of uncontrolled free text. The family spans thesauri, taxonomies, classification schemes, and subject heading systems, which share the goal of constraining and standardizing the values used for description so that they can be reused and compared across systems.

## How sources treat it

- **[[skos]]** _(standard · normative)_ — SKOS is "a common data model for sharing and linking knowledge organization systems (KOS)" — thesauri, taxonomies, classification schemes and subject heading systems — via the Web, capturing the structure these families share and providing a "standard, low-cost migration path" for porting existing KOS to the Semantic Web ⟨Abstract⟩
- **[[skos]]** _(standard · normative)_ — SKOS is a data-modeling language for representing KOS "as-is", **not** a formal knowledge representation language: the "concepts" of a thesaurus are modeled as individuals and links between them as facts about those individuals, never as class or property axioms ⟨§1.3⟩
- **[[dcmi-terms]]** _(standard · normative)_ — Vocabulary Encoding Schemes name external controlled vocabularies for values: DCMIType, DDC, IMT, LCC, LCSH, MESH, NLM, TGN, UDC ⟨§4 Vocabulary Encoding Schemes⟩
- **[[dcmi-terms]]** _(standard · normative)_ — Recommended practice repeatedly points to external controlled vocabularies (e.g. Getty TGN for coverage, Internet Media Types for format, ISO 639 / BCP 47 for language, ISO 8601 / W3CDTF / EDTF for dates) ⟨§2 Properties in /terms/⟩

## Where sources differ

SKOS supplies a data model for representing an entire controlled vocabulary "as-is" so it can be published and linked on the Web ⟨§1.3⟩. DCMI Metadata Terms, by contrast, does not model a vocabulary's internal structure; it references external controlled vocabularies as named sources of permitted values for its metadata properties, packaged as Vocabulary Encoding Schemes ⟨§4 Vocabulary Encoding Schemes⟩. The two treat controlled vocabularies at different layers — SKOS as the thing being modeled, DCMI as a value source pointed to from a metadata term.

## See also
[[concept-scheme]] · [[vocabulary-encoding-scheme]] · [[semantic-relation]]
