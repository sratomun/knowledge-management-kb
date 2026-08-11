---
title: "Qualification pattern"
type: concept
aliases: []
tags: [governance]
related: ["[[provenance]]", "[[provenance-influence]]", "[[derivation]]"]
updated: 2026-08-09
---

# Qualification pattern

## What it is
The qualification pattern is a modeling technique for adding detail to an otherwise binary relation: instead of linking two things directly, it introduces an intermediate "influence" object that stands for the relationship itself, which can then be annotated with extra attributes such as time, role, or plan. It trades brevity for expressiveness, letting a simple link be described more richly when needed.

## How sources treat it
- **[[prov-o]]** _(standard · normative)_ — The Qualified Terms are the result of applying the Qualification Pattern to the simple (unqualified) relations; the pattern restates an unqualified influence relation using an intermediate class that represents the influence between two resources, which can then be annotated with additional descriptions ⟨§3.3⟩.
- **[[prov-o]]** _(standard · normative)_ — Seven Starting Point relations and seven Expanded relations can be further described using the Qualification Pattern, per the normative Tables 2 and 3 ⟨§3.3⟩.
- **[[prov-o]]** _(standard · normative)_ — Consuming applications should recognize both qualified and unqualified forms, and treat the qualified form as implying the unqualified form; because the qualified form is more verbose, the unqualified form should be favored where additional properties are not provided ⟨§3.3⟩.
- **[[prov-o]]** _(standard · normative)_ — The `prov:atTime` property can be used to describe any `prov:InstantaneousEvent` (including `prov:Start`, `prov:Generation`, `prov:Usage`, `prov:Invalidation`, and `prov:End`), one kind of annotation the pattern enables ⟨§3.3⟩.

## Where sources differ
Only PROV-O is sourced for this concept, so there is no cross-source divergence to report. PROV-O's own guidance holds the qualified and unqualified forms in tension: the qualified form carries more description, while the unqualified form should be favored when no additional properties are provided ⟨§3.3⟩.

## See also
[[provenance]] · [[provenance-influence]] · [[derivation]]
