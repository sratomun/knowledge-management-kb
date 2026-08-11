---
title: "Wikibase Item"
type: entity
subtype: metamodel-construct
aliases: ["wikibase-item"]
tags: [semantic-wiki]
concepts: ["[[entity-data-model]]", "[[structured-knowledge-base]]"]
sources: ["[[wikibase]]"]
updated: 2026-08-10
---

# Wikibase Item

## What it is
An Item is one of the two predefined kinds of Entity in the Wikibase data model: it
is how Wikibase refers to anything of interest (typically the topic a set of
Wikipedia articles is about). One page in Wikibase describes one item.

## Key facts
- A Wikibase knowledge base is a collection of Entities, and Items are one of the two predefined Entity kinds (the other being Properties) ⟨wikibase: data-model-primer/Summary⟩.
- Each Item has an identifier that is a number prefixed with Q ⟨wikibase: data-model-primer/Summary⟩.
- An Item carries a "fingerprint" consisting of a multilingual label, a multilingual description, and multilingual aliases ⟨wikibase: data-model-primer/Summary⟩.
- Within an entity type, an item's combination of label and description in a given language must be unique (unless label and/or description are empty) ⟨wikibase: data-model-primer/Summary⟩.
- Aliases provide alternative names (including popular misspellings) to aid search, functioning much like Wikipedia redirects ⟨wikibase: data-model-primer/Items⟩.
- An Item is described by Statements and also carries site links to wiki pages ⟨wikibase: data-model-primer/Summary⟩.
- Multiple identifying mechanisms (site links plus label-and-description across languages) can get out of sync — the "symbol grounding problem" Wikibase addresses socio-technically rather than by giving any language precedence ⟨wikibase: data-model-primer/The symbol grounding problem⟩.

## Relations
- Realizes: [[entity-data-model]]
- Defined in: [[wikibase]]
- Related: [[wikibase-statement]]
- Related: [[wikibase-property]]

## See also
[[wikibase-property]] · [[structured-knowledge-base]]
