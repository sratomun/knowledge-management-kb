---
title: "OKF bundle"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-management]
concepts: ["[[concept-per-file-bundle]]"]
sources: ["[[okf]]"]
updated: 2026-08-09
---

# OKF bundle

## What it is

An OKF bundle is the unit of knowledge exchange in the Open Knowledge Format: a directory of markdown files representing concepts, portable across systems, organizations, and tools.

## Key facts

- "An OKF bundle is a directory of markdown files representing concepts: anything you want to capture, including tables, datasets, metrics, playbooks, runbooks, and APIs" ⟨How OKF works: The design in one screen⟩
- A bundle is "just files — shippable as a tarball, hostable in any git repo, mountable on any filesystem" ⟨Introducing the Open Knowledge Format⟩
- Bundles can optionally include index.md files (progressive disclosure) and log.md files (chronological history of changes) ⟨How OKF works: The design in one screen⟩
- Three ready-to-browse sample bundles (GA4 e-commerce, Stack Overflow, Bitcoin public datasets) were produced by the reference agent and committed to the repo as conformant examples ⟨What we're shipping with the spec⟩

## Relations

- Realizes: [[concept-per-file-bundle]]
- Defined in: [[okf]]
- Related: [[okf-concept-file]] · [[okf-index-log]]

## See also
[[okf-concept-file]] · [[concept-per-file-bundle]]
