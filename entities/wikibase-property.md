---
title: "Wikibase Property"
type: entity
subtype: metamodel-construct
aliases: ["wikibase-property"]
tags: [semantic-wiki]
concepts: ["[[entity-data-model]]"]
sources: ["[[wikibase]]"]
updated: 2026-08-10
---

# Wikibase Property

## What it is
A Property is one of the two predefined kinds of Entity in the Wikibase data model.
Properties are described on their own wiki pages and supply the "property" component
used inside the claims of statements, together with a data type that constrains the
values used with them.

## Key facts
- Properties are one of the two predefined Entity kinds in a Wikibase knowledge base (alongside Items) ⟨wikibase: data-model-primer/Summary⟩.
- Each Property has an identifier that is a number prefixed with P ⟨wikibase: data-model-primer/Summary⟩.
- A Property carries a "fingerprint" of a multilingual label, a multilingual description, and multilingual aliases, and is itself described by Statements ⟨wikibase: data-model-primer/Summary⟩.
- Each Property has an associated data type that defines the type of the value used with it ⟨wikibase: data-model-primer/Statements⟩.
- Values used with a property range from simple (another item or a string) to complex (a geographic shape, a measurement with unit and accuracy, or a time period), and the set of data types is mostly predefined ⟨wikibase: data-model-primer/Statements⟩.
- The set of properties is created and maintained by the Wikibase editors ⟨wikibase: data-model-primer/Statements⟩.
- Properties are described on their own wiki pages in Wikibase ⟨wikibase: data-model-primer/Statements⟩.

## Relations
- Realizes: [[entity-data-model]]
- Defined in: [[wikibase]]
- Related: [[wikibase-statement]]
- Related: [[wikibase-item]]

## See also
[[wikibase-item]] · [[wikibase-statement]]
