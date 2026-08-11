---
title: "Concept-Per-File Bundle"
type: concept
aliases: []
tags: [semantic-layer]
related: ["[[agent-ready-knowledge]]", "[[knowledge-interchange-format]]"]
updated: 2026-08-09
---

# Concept-Per-File Bundle

## What it is
A concept-per-file bundle is a way of organizing knowledge as a directory of markdown files where each file captures exactly one concept and the file's path is that concept's identity. Files cross-link with ordinary markdown links, so the directory becomes a relationship graph richer than the filesystem's parent/child hierarchy, with structured frontmatter carrying the fields that need to be queryable and the body holding everything else.

## How sources treat it
- **[[okf]]** _(provider-doc · vendor)_ — an OKF bundle is a directory of markdown files representing concepts; each concept is one file and the file path is the concept's identity ⟨How OKF works: The design in one screen⟩
- **[[okf]]** _(provider-doc · vendor)_ — concepts link to each other with normal markdown links, forming a relationship graph richer than filesystem parent/child links; `index.md` and `log.md` files are optional ⟨How OKF works: The design in one screen⟩
- **[[okf]]** _(provider-doc · vendor)_ — each markdown file is one concept (a table, dataset, metric, playbook, runbook, API, or anything else), with frontmatter carrying a small set of queryable fields and the body holding everything else ⟨Structure⟩
- **[[okf]]** _(provider-doc · vendor)_ — the frontmatter carries only the fields that need to be queryable: `type`, `title`, `description`, `resource`, `tags`, and `timestamp` ⟨Introducing the Open Knowledge Format⟩
- **[[okf]]** _(provider-doc · vendor)_ — bundles may optionally include `index.md` files for progressive disclosure during navigation and `log.md` files for chronological change history ⟨Structure⟩
- **[[okf]]** _(provider-doc · vendor)_ — notes the pattern recurs under many names — Obsidian vaults wired to coding agents, the AGENTS.md / CLAUDE.md convention-file family, and "metadata as code" repos — but each instance is bespoke and not designed to cooperate ⟨Knowledge as a living wiki⟩

## Where sources differ
Only [[okf]] describes the concept-per-file bundle in this KB, as a vendor provider-doc from Google Cloud. It does observe that the underlying pattern appears in several bespoke, non-cooperating forms elsewhere, but those are noted by OKF itself rather than being separate sources here. With a single source, no divergence can be reported.

## See also
[[agent-ready-knowledge]] · [[knowledge-interchange-format]]
