---
title: "Wikibase Qualifier"
type: entity
subtype: metamodel-construct
aliases: ["wikibase-qualifier"]
tags: [semantic-wiki]
concepts: ["[[entity-data-model]]"]
sources: ["[[wikibase]]"]
updated: 2026-08-10
---

# Wikibase Qualifier

## What it is
A Qualifier is an optional property-value pair attached to a Wikibase statement that
further describes or refines the value given in that statement. It is an integral
part of the claim.

## Key facts
- Qualifiers are used to further describe or refine the value of a property given in a statement, and consist of a property and a value, the same as for statements ⟨wikibase: data-model-primer/Qualifiers⟩.
- A statement may optionally include one or more qualifiers, which sit inside the claim alongside the property and value ⟨wikibase: data-model-primer/Statements⟩.
- Qualifiers reduce the number of properties needed to a manageable size by further specifying a statement instead of requiring new properties ⟨wikibase: data-model-primer/Qualifiers⟩.
- A qualifier can modify what the item means, modify the property, constrain the validity of the value (e.g. "as of 2011"), or offer further details (e.g. an actor's role) ⟨wikibase: data-model-primer/Qualifiers⟩.
- The qualifier is an integral part of the statement: take away the qualifier and the meaning of the statement is changed — far less true for references ⟨wikibase: data-model-primer/Qualifiers⟩.
- It is open to the Wikibase community to maintain and use qualifiers in a way that makes sense for their use cases ⟨wikibase: data-model-primer/Qualifiers⟩.

## Relations
- Realizes: [[entity-data-model]]
- Defined in: [[wikibase]]
- Related: [[wikibase-statement]]

## See also
[[wikibase-statement]] · [[wikibase-property]]
