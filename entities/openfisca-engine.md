---
title: "OpenFisca engine"
type: entity
subtype: system
aliases: []
tags: [knowledge-processing]
concepts: ["[[rules-as-code]]"]
sources: ["[[openfisca]]"]
updated: 2026-08-10
---

# OpenFisca engine

## What it is
OpenFisca is an open-source engine that models tax and benefit legislation as computable **parameters** (legal values over time) and **formulas** (rule functions), executed over open APIs. It exposes a JSON web API and a vectorial Python API and packages rules per jurisdiction as country packages, supporting simulation from a single person up to whole-population scale.

## Key facts
- OpenFisca describes itself as "the most widely adopted free and open-source engine to write rules as code" ⟨[[openfisca]] — positioning⟩.
- It models legislation as parameters — legal values such as tax rates tracked over time so historical values are retrievable by date — and formulas, the computable functions that model the rules ⟨[[openfisca]] — Model concepts⟩.
- It offers two execution surfaces: a JSON web API that computes eligibility and amounts for a described situation, and a vectorial Python API that computes at population scale ⟨[[openfisca]] — Model concepts / Audiences⟩.
- Rules are organised as per-jurisdiction, open-source country packages that define the jurisdiction and expose its rules model ⟨[[openfisca]] — Model concepts⟩.
- Simulation calculates values on provided situations for one person or millions, and is reused by example eligibility services such as Barcelona's "Les meves ajudes," LexImpact, and Japan's "Support Estimate Hermit Crab" ⟨[[openfisca]] — Model concepts / Example services⟩.

## Relations
- Realizes: [[rules-as-code]]
- Defined in: [[openfisca]]
- Maintained by: [[org-openfisca]]

## See also
[[rules-as-code]] · [[eligibility-determination]] · [[openfisca]]
