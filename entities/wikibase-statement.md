---
title: "Wikibase Statement"
type: entity
subtype: metamodel-construct
aliases: ["wikibase-statement"]
tags: [semantic-wiki]
concepts: ["[[entity-data-model]]"]
sources: ["[[wikibase]]"]
updated: 2026-08-10
---

# Wikibase Statement

## What it is
A Statement is the unit by which Wikibase models information about an entity.
Wikibase deliberately models statements about items rather than the items
themselves, following the guiding requirement that "Wikibase will not be about the
truth, but about statements and their references."

## Key facts
- A statement consists of one property, one value, optionally one or more qualifiers, and optionally one or more references ⟨wikibase: data-model-primer/Statements⟩.
- The property, value, and qualifiers together are called the claim, which together with any source references forms the statement ⟨wikibase: data-model-primer/Statements⟩.
- Wikibase models statements about items rather than the items themselves — its guiding requirement is that "Wikibase will not be about the truth, but about statements and their references" ⟨wikibase: data-model-primer/Statements⟩.
- There can be several statements about the same property (e.g. a person's several children, or diverging population figures) ⟨wikibase: data-model-primer/Statements⟩.
- References offer a source supporting a claim; a claim without references is not necessarily wrong, nor is one with references necessarily true — trust is left to the reader ⟨wikibase: data-model-primer/Statements⟩.
- Every statement carries one of three ranks — preferred, normal, or deprecated — used to select which statements a query returns; only preferred statements are displayed by default ⟨wikibase: data-model-primer/Ranks⟩.
- Two special values may occur regardless of data type: "none" (the property is known to have no value) and "unknown" (the property has a value but it is not known which) ⟨wikibase: data-model-primer/Statements⟩.

## Relations
- Realizes: [[entity-data-model]]
- Defined in: [[wikibase]]
- Related: [[wikibase-qualifier]]
- Related: [[wikibase-property]]

## See also
[[wikibase-qualifier]] · [[wikibase-item]]
