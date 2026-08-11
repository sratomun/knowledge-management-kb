---
title: "OKF concept file"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-management]
concepts: ["[[concept-per-file-bundle]]"]
sources: ["[[okf]]"]
updated: 2026-08-09
---

# OKF concept file

## What it is

A concept file is a single markdown document in an OKF bundle representing exactly one concept, whose file path serves as the concept's identity and which links to other concepts to form a graph.

## Key facts

- "Each concept is one file. The file path is the concept's identity" ⟨How OKF works: The design in one screen⟩
- Each document "has a small block of YAML front matter for structured fields and a markdown body for everything else" ⟨How OKF works: The design in one screen⟩
- "Concepts link to each other with normal markdown links, turning the directory into a graph of relationships that is richer than the parent/child links implied by the file system" ⟨How OKF works: The design in one screen⟩

## Relations

- Realizes: [[concept-per-file-bundle]]
- Defined in: [[okf]]
- Related: [[okf-bundle]] · [[okf-type-field]]

## See also
[[okf-bundle]] · [[okf-type-field]]
