---
title: "Temporal ontology"
type: concept
subtype: null
aliases: []
tags: [semantic-web]
related: ["[[rdf-vocabulary-schema]]", "[[linked-data]]"]
updated: 2026-08-10
---

# Temporal ontology

## What it is
A vocabulary for describing temporal entities — instants and intervals — the topological relations among them, and positional/duration information, so that time-bound facts can be represented and reasoned over in a knowledge graph.

## How sources treat it
- **[[owl-time]]** _(standard · normative)_ — defines `time:TemporalEntity`, subdivided into `time:Instant` and `time:Interval`/`time:ProperInterval` ⟨OWL-Time, §Temporal entities⟩ [gen]
- **[[owl-time]]** _(standard · normative)_ — provides the Allen interval relations (before, after, meets, overlaps, during, …) for topological reasoning over intervals ⟨OWL-Time, §Interval relations⟩ [gen]

## Where sources differ
Single normative source; complements the KB's own lightweight valid-time model rather than replacing it.

## See also
[[organization-ontology]] · [[rdf-vocabulary-schema]]
