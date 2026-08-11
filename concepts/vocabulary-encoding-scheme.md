---
title: "Vocabulary encoding scheme"
type: concept
aliases: []
tags: [metadata]
related: ["[[syntax-encoding-scheme]]", "[[controlled-vocabulary]]", "[[descriptive-metadata]]", "[[value-domain]]"]
updated: 2026-08-09
---

# Vocabulary encoding scheme

## What it is
A vocabulary encoding scheme (VES) names an external controlled vocabulary — a thesaurus, classification, or subject-heading list — from which the value of a metadata property is drawn. Rather than carrying a free-text value, a property tagged with a VES points into a known, managed set of concepts, so that the value's meaning is fixed and shareable across systems.

## How sources treat it
- **[[dcmi-terms]]** _(standard · normative)_ — Vocabulary Encoding Schemes name external controlled vocabularies for values: DCMIType, DDC, IMT, LCC, LCSH, MESH, NLM, TGN, UDC ⟨§4 Vocabulary Encoding Schemes⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — Recommended practice repeatedly points to external controlled vocabularies — e.g. Getty TGN for coverage and Library of Congress schemes for subject — as the source of property values ⟨§2 Properties in /terms/⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — The /dcam/ namespace supplies the meta-vocabulary used to describe the terms themselves, including the `VocabularyEncodingScheme` class ⟨§8 Terms for vocabulary description⟩.

## Where sources differ
Only DCMI Terms, among the specifications sourced for this concept, defines the vocabulary-encoding-scheme construct by name, so there is no cross-source divergence to report. DCMI itself distinguishes a vocabulary encoding scheme (which names the controlled value list) from a syntax encoding scheme (which specifies a value's datatype or string syntax) ⟨§4 Vocabulary Encoding Schemes⟩⟨§5 Syntax Encoding Schemes⟩.

## See also
[[syntax-encoding-scheme]] · [[controlled-vocabulary]] · [[value-domain]] · [[descriptive-metadata]]
