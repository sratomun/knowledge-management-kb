---
title: "Conceptual domain"
type: concept
aliases: []
tags: [metadata]
related: ["[[value-domain]]", "[[data-element-concept]]", "[[metadata-registry]]"]
updated: 2026-08-09
---

# Conceptual domain

## What it is
A conceptual domain is the representation-independent set of value meanings associated with a data element concept — *what the allowed values mean* rather than how they are written. It is the abstract counterpart to a value domain: one conceptual domain (e.g. the meanings male, female, unknown) can be realized by several value domains that encode those same meanings differently (e.g. "M/F/U" versus "1/2/9").

## How sources treat it
- **[[iso-iec-11179-1]]** _(standard · normative)_ — The core object, the data element concept, defines a concept and ideally describes data independent of its representation in any one system, table, column, or organisation — the representation-independent (conceptual) side of a data element ⟨Wikipedia: ISO/IEC 11179⟩.
- **[[iso-iec-11179-1]]** _(standard · normative)_ — A value domain gives the permitted range of values for a characteristic (e.g. "sex of person" = M/F/U); differing value domains can represent the same underlying meanings across data sets ⟨Wikipedia: ISO/IEC 11179⟩.
- **[[iso-iec-11179-1]]** _(standard · normative)_ — In the 11179 metamodel a data element concept is associated with a conceptual domain (the representation-independent value meanings), which is realized by one or more value domains — stated here from general knowledge of the standard's framework, not quoted from the paywalled primary text ⟨iso.org/standard/78914⟩.

## Where sources differ
Only ISO/IEC 11179 is sourced for this concept, so there is no cross-source divergence to report. An honesty caveat applies: the consulted secondary source (the Wikipedia article) describes value domains and representation-independence but does not name "conceptual domain" explicitly, so the conceptual-domain/value-domain distinction is drawn from general knowledge of the 11179 metamodel rather than quoted from either the secondary or the paywalled primary text ⟨Wikipedia: ISO/IEC 11179⟩.

## See also
[[value-domain]] · [[data-element-concept]] · [[metadata-registry]]
