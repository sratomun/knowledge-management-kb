---
title: "Open Knowledge Format (OKF)"
type: source
kind: provider-doc
authority: vendor
subtype: knowledge-format-spec
aliases: ["OKF", "Open Knowledge Format"]
publisher: Google Cloud
url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
version: "v0.1"
published: 2026-06
effective_from: 2026-06-12
effective_to: ongoing
status: current
tags: [semantic-layer, knowledge-management]
updated: 2026-08-09
---

# Open Knowledge Format (OKF)

## Scope & purpose

OKF is an open specification, announced by Google Cloud on June 12, 2026, that formalizes the LLM-wiki pattern into a portable, interoperable format for representing the metadata, context, and curated knowledge that modern AI systems and agentic systems need. It positions itself as a vendor-neutral, agent- and human-friendly standard whose motivating problem is that internal knowledge (table schemas, metric definitions, runbooks, join paths, deprecation notices) is scattered across fragmented, mutually incompatible systems, forcing every agent builder to solve context assembly from scratch. The stated answer is "a format, not another service."

## Structure

OKF v0.1 represents knowledge as a directory ("bundle") of markdown files with YAML frontmatter. Each markdown file is one "concept" (a table, dataset, metric, playbook, runbook, API, or anything else to capture), and the file path is the concept's identity. Concepts cross-link with normal markdown links, turning the directory into a graph richer than the filesystem's parent/child hierarchy. Frontmatter carries a small set of queryable structured fields — `type`, `title`, `description`, `resource`, `tags`, `timestamp` — while the markdown body holds everything else. Bundles may optionally include `index.md` files (progressive disclosure during navigation) and `log.md` files (chronological change history). The full v0.1 spec, including conformance criteria, cross-linking rules, and reserved filenames, fits on a single page.

## Key points

- OKF is introduced as an open specification that formalizes the LLM-wiki pattern into a portable, interoperable, vendor-neutral, agent- and human-friendly format ⟨Introducing the Open Knowledge Format⟩
- OKF v0.1 represents knowledge as a directory of markdown files with YAML frontmatter plus a small set of agreed-upon conventions, so wikis from different producers can be consumed by different agents without translation ⟨Introducing the Open Knowledge Format⟩
- A bundle is "just markdown, just files, just YAML frontmatter" — no compression scheme, no new runtime, no required SDK — readable in any editor, renderable on GitHub, shippable as a tarball, hostable in any git repo ⟨Introducing the Open Knowledge Format⟩
- The frontmatter carries only the fields that need to be queryable: `type`, `title`, `description`, `resource`, `tags`, and `timestamp` ⟨Introducing the Open Knowledge Format⟩
- The pattern recurs under many names — Obsidian vaults wired to coding agents, the AGENTS.md / CLAUDE.md convention-file family, repos of `index.md` and `log.md` artifacts, and "metadata as code" repositories — but each instance is bespoke and not designed to cooperate ⟨Knowledge as a living wiki⟩
- Andrej Karpathy's LLM Wiki gist articulates the idea: "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass," making the bookkeeping humans abandon exactly what LLMs are good at ⟨Knowledge as a living wiki⟩
- The needed answer is a format anyone can produce without an SDK, anyone can consume without an integration, that survives moving between systems and lives in version control, readable by humans and parseable by agents with no translation layer ⟨What's missing is a format, not another service⟩
- An OKF bundle is a directory of markdown files representing concepts; each concept is one file and the file path is the concept's identity ⟨How OKF works: The design in one screen⟩
- Concepts link to each other with normal markdown links, forming a relationship graph richer than filesystem parent/child links; `index.md` and `log.md` files are optional ⟨How OKF works: The design in one screen⟩
- Principle 1, Minimally opinionated: OKF requires exactly one thing of every concept — a `type` field; everything else is left to the producer, defining the interoperability surface not the content model ⟨Three principles behind the design⟩
- Principle 2, Producer/consumer independence: OKF separates who writes knowledge from who consumes it; the format is the contract and the tooling at each end is independently swappable ⟨Three principles behind the design⟩
- Principle 3, Format, not platform: OKF is not tied to any cloud, database, model provider, or agent framework and will never require a proprietary account or SDK to read, write, or serve ⟨Three principles behind the design⟩
- Reference implementations ship at both ends: an enrichment agent that walks a BigQuery dataset and drafts then enriches an OKF concept doc per table/view, and a static HTML visualizer that renders any bundle as an interactive graph in a single self-contained file ⟨What we're shipping with the spec⟩
- Three ready-to-browse sample bundles (GA4 e-commerce, Stack Overflow, Bitcoin public datasets) are committed to the repo, and Google Cloud's Knowledge Catalog was updated to ingest OKF and serve it to agents; OKF v0.1 is a versioned starting point designed for backward-compatible growth ⟨What we're shipping with the spec⟩

## Concepts & entities covered
Concepts: [[agent-ready-knowledge]] · [[knowledge-interchange-format]] · [[concept-per-file-bundle]]
Entities: [[okf-spec]] · [[okf-bundle]] · [[okf-concept-file]] · [[okf-type-field]] · [[okf-index-log]] · [[okf-visualizer]] · [[okf-enrichment-agent]] · [[okf-knowledge-catalog]] · [[okf-obsidian]] · [[okf-karpathy-llm-wiki]] · [[okf-agents-md]]
