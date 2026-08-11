---
title: "Cube: measure"
type: entity
subtype: metamodel-construct
aliases: []
tags: [semantic-layer]
concepts: ["[[metric-definition]]"]
sources: ["[[cube]]"]
updated: 2026-08-10
---

# Cube: measure

## What it is
A measure is Cube's construct for a quantitative value computed by aggregating across
rows — counts, sums, averages, and more complex calculations. Measures are the metric
definitions of the semantic layer, defined inside a cube and reused by every consumer.

## Key facts
- Measures compute aggregated values across rows such as counts, sums, and averages, and are referred to as quantitative data (number of units sold, unique visits, profit) ⟨cube: measures⟩.
- A measure specifies the SQL expression to aggregate and an aggregation `type` (e.g. `count`, `sum`, `avg`) ⟨cube: measures/defining measures⟩.
- Filtered measures apply `filters` so only matching rows are included, which Cube compiles into SQL with a `CASE` expression ⟨cube: measures/filtered measures⟩.
- Calculated measures reference other measures — within the same cube or, across joined cubes, from other cubes — to decompose complex metrics like ratios and percents ⟨cube: measures/calculated measures⟩.
- Multi-stage measures are calculated in two or more stages (each producing CTEs), enabling rolling windows, period-to-date (YTD/QTD/MTD), time shift, percent/share of total, nested aggregates, and ranking ⟨cube: measures/multi-stage measures⟩.
- A `format` parameter (e.g. `currency`, `percent`) controls how a measure is displayed ⟨cube: measures/formatting⟩.

## Relations
- Realizes: [[metric-definition]]
- Defined in: [[cube]]
- Published by: [[org-cube-dev]]
- Related: [[cube-cube]], [[cube-dimension]]

## See also
[[metric-definition]] · [[semantic-layer]]
