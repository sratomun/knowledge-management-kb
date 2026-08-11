---
title: "Time Ontology in OWL (OWL-Time)"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["OWL-Time", "OWL Time"]
publisher: "W3C"
url: https://www.w3.org/TR/owl-time/
version: "W3C Recommendation 2020-11-26"
published: 2020-11
effective_from: 2020-11
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# Time Ontology in OWL (OWL-Time)

> _Authored from general knowledge, not from the primary text. Verify against the primary W3C Recommendation before relying on specifics or term IRIs._

## Scope & purpose
OWL-Time is a W3C vocabulary for describing temporal entities — instants and intervals — and the topological relations among them, plus positional/clock/calendar information. Captured here **lightweight** as a semantic-web vocabulary relevant to modeling valid-time and temporal facts in a knowledge graph.

## Key points
- Core classes are `time:TemporalEntity`, subdivided into `time:Instant` and `time:Interval` (with `time:ProperInterval`) ⟨OWL-Time, §Temporal entities⟩ [gen]
- Defines the **Allen interval relations** (e.g., `time:before`, `time:after`, `time:intervalMeets`, `time:intervalOverlaps`, `time:intervalDuring`) for topological reasoning over intervals ⟨OWL-Time, §Interval relations⟩ [gen]
- Supports temporal **position** via `time:TimePosition` and duration via `time:Duration` / `time:GeneralDurationDescription`, decoupled from any single calendar ⟨OWL-Time, §Temporal position⟩ [gen]
- Provides a **date-time description** vocabulary aligned to the Gregorian calendar while allowing other temporal reference systems ⟨OWL-Time, §Date-time description⟩ [gen]

## Concepts & entities covered
Concepts: [[temporal-ontology]]
Entities: [[org-w3c]]
