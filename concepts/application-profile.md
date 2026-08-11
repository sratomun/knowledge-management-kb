---
title: "Application profile"
type: concept
aliases: []
tags: [metadata]
related: ["[[descriptive-metadata]]", "[[vocabulary-encoding-scheme]]", "[[syntax-encoding-scheme]]", "[[metadata-registry]]"]
updated: 2026-08-09
---

# Application profile

## What it is
An application profile is a specification that selects and combines metadata terms drawn from one or more existing vocabularies — optionally adding local constraints on which terms are used, how, and with what value vocabularies — to fit the needs of a particular application or community, rather than minting an entirely new vocabulary. It lets implementers reuse standard terms in tailored, interoperable combinations.

## How sources treat it
- **[[dcmi-terms]]** _(standard · normative)_ — The terms are intended for use in combination with terms from other compatible vocabularies within application profiles ⟨§1 Introduction⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — For non-RDF uses (XML, JSON, UML, relational databases) implementers may treat the domain, range, subproperty, and subclass relations as usage suggestions rather than binding constraints, relying on the natural-language definitions ⟨§1 Introduction⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — The /terms/ namespace provides `dcterms:conformsTo`, whose recommended practice points to an established standard to which the described resource conforms — a hook by which resources can declare the profile they follow ⟨§2 Properties in /terms/⟩.

## Where sources differ
Among the specifications sourced for this concept, only DCMI Terms defines the application-profile mechanism explicitly, so there is no cross-source divergence to report here. Within DCMI, the notable tension is between the RDF-formal reading of the vocabulary (with binding domain/range semantics) and the non-RDF reading, where those same relations are offered as usage suggestions for profile authors ⟨§1 Introduction⟩.

## See also
[[descriptive-metadata]] · [[vocabulary-encoding-scheme]] · [[syntax-encoding-scheme]] · [[metadata-registry]]
