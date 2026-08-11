---
title: "Rules as Code"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[machine-readable-legal-norms]]", "[[eligibility-determination]]"]
updated: 2026-08-10
---

# Rules as Code

## What it is
Rules as Code is the practice of encoding legislation, regulation, or policy as machine-executable specifications — parameters, formulas, or logical constraints — so that the rules can be computed over, simulated, and audited rather than only read. Proponents frame it as giving a common, executable language to law: eligibility and amounts can be calculated for a described situation, reforms simulated at population scale, and formal constraints kept linked to their source provisions. It spans a spectrum from hand-authored country models to LLM-assisted translation of statutory text validated against symbolic checks.

## How sources treat it
- **[[openfisca]]** _(provider-doc · vendor)_ — describes itself as "the most widely adopted free and open-source engine to write rules as code," modelling tax and benefit legislation as parameters (legal values tracked over time) and formulas (computable functions) executable over open APIs ⟨openfisca.org/en — positioning; Model concepts⟩
- **[[openfisca]]** _(provider-doc · vendor)_ — frames Rules as Code as providing algorithmic transparency and pooling IT costs across public bodies, and reports simulation of reforms on a population's income distribution ⟨openfisca.org/en — Audiences⟩
- **[[de-jure-regulatory-rules]]** _(article · informational)_ — transforms raw regulatory documents into a typed JSON rule schema in which each rule unit carries a nine-field statement decomposition (action, object, method, conditions, constraints, exceptions, penalties, purpose, verbatim source span) with SHA-256-fingerprinted traceability ⟨§3.1, §3.2⟩
- **[[neurosymbolic-public-sector-eligibility]]** _(article · informational)_ — situates its work within the Rules as Code movement, which it says advocates encoding legislation as machine-executable specifications at the drafting stage, and prompts an LLM to translate each provision into a solver-ready logical rule stored with a citation to its source ⟨arXiv:2512.12109, §2, §3.4⟩

## Where sources differ
The sources differ on *who authors the rules and how*. [[openfisca]] is a hand-authored, human-curated engine: domain experts encode legislation as parameters and formulas, with no LLM in the loop, positioned as public infrastructure. [[de-jure-regulatory-rules]] and [[neurosymbolic-public-sector-eligibility]] are *LLM-assisted*: a model extracts or translates statutory text into structured/logical rules, with quality assured by judge-based repair or symbolic verification respectively. There is also a normativity difference — OpenFisca and De Jure aim at broad rule sets; the neuro-symbolic paper encodes rules into a formal ontology for SAT/UNSAT checking. Each source's efficacy and adoption claims are attributed to its authors on its own page.

## See also
[[machine-readable-legal-norms]] · [[eligibility-determination]]
