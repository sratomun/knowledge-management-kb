---
title: "Cube: join"
type: entity
subtype: metamodel-construct
aliases: []
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[cube]]"]
updated: 2026-08-10
---

# Cube: join

## What it is
A join is Cube's construct that defines a relationship between two cubes, letting the
semantic layer automatically generate multi-table SQL when a view or query combines data
from more than one cube.

## Key facts
- Joins define relationships between cubes, allowing Cube to automatically generate multi-table SQL JOIN clauses when a view combines members from multiple cubes ⟨cube: joins⟩.
- Cube supports three relationship types — `one_to_one`, `one_to_many`, and `many_to_one` — and the relationship type determines which table becomes the left side of the generated `LEFT JOIN` ⟨cube: joins/relationship types⟩.
- All joins are directed, flowing from the source cube (where the join is defined) to the target cube; the source is placed on the left of the LEFT JOIN so its rows are preserved while the target contributes matching rows or NULL ⟨cube: joins/direction of joins⟩.
- As a rule of thumb, joins are defined on the fact table pointing toward the dimension table using `many_to_one`, ensuring the fact table is the base of the query and all its rows are preserved ⟨cube: joins/relationship types⟩.
- Many-to-many relationships are modeled with an associative (junction) cube that chains joins so they flow in one direction ⟨cube: joins/many-to-many relationships⟩.
- Views control which join path is followed via the `join_path` parameter, which also resolves diamond subgraphs where more than one path exists between two cubes ⟨cube: joins/using views to control direction⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[cube]]
- Published by: [[org-cube-dev]]
- Related: [[cube-cube]], [[cube-view]]

## See also
[[semantic-model]] · [[semantic-layer]]
