---
title: "Entity Data Model"
type: concept
subtype: data-model
aliases: []
tags: [semantic-wiki]
related: ["[[semantic-wiki]]", "[[structured-knowledge-base]]", "[[linked-open-data]]"]
updated: 2026-08-10
---

# Entity Data Model

## What it is

An entity data model organizes a knowledge base around discrete entities — items and the properties used to describe them — each identified, labeled, and described in a consistent way, with assertions about those entities captured as structured, optionally referenced statements. It fixes what the units of the knowledge base are (entities), how they are named and disambiguated, and how facts about them are expressed and sourced.

## How sources treat it

- **[[wikibase]]** _(provider-doc · vendor)_ — A Wikibase knowledge base is a collection of Entities; there are two predefined kinds — Items and Properties — and Wikibase may be extended to support additional entity types ⟨wikibase: data-model-primer/Summary⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Each Item has an identifier prefixed with Q and each Property one prefixed with P; both carry a "fingerprint" of a multilingual label, description, and aliases ⟨wikibase: data-model-primer/Summary⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Within an entity type, an entity's combination of label and description in a given language must be unique unless empty; label plus description together identify meaning while aliases provide alternative names to aid search ⟨wikibase: data-model-primer/Items⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — A statement consists of one property, one value, optionally qualifiers, and optionally references; property, value, and qualifiers form the claim, which with any references forms the statement ⟨wikibase: data-model-primer/Statements⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Properties each carry a data type defining the value used with them; values range from simple (another item or a string) to complex (a geographic shape, a measurement with unit and accuracy, or a time period), and two special values exist regardless of data type — "none" and "unknown" ⟨wikibase: data-model-primer/Statements⟩
- **[[wikibase]]** _(provider-doc · vendor)_ — Qualifiers refine, constrain, or add detail to a statement's value and are integral to it, while statements carry one of three ranks — preferred, normal, or deprecated — used to select which statements a query returns ⟨wikibase: data-model-primer/Qualifiers · Ranks⟩

## Where sources differ

Only the Wikibase source is cited here. Its entity model is oriented to multilingual, reference-backed statements rather than to a single canonical assertion of fact: items are disambiguated by label-plus-description, claims may carry qualifiers and references, and ranks — not deletion — govern which statements surface. The source also notes the "symbol grounding problem," where an item's multiple identifying mechanisms (site links, labels, descriptions) can drift out of sync, and states Wikibase addresses it socio-technically rather than by privileging any language.

## See also
[[semantic-wiki]] · [[structured-knowledge-base]] · [[linked-open-data]]

<!-- REVIEW: possible J1 near-duplicate between [[structured-knowledge-base]] and [[entity-data-model]] (both sourced only from Wikibase, overlapping lead). Judge confidence low: system-class vs data-model split is defensible. Human to decide merge vs keep. -->
