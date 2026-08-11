---
title: "LEDGERMIND system"
type: entity
subtype: system
aliases: []
tags: [doc-processing]
concepts: ["[[provenance-constrained-extraction]]", "[[extraction-self-verification]]", "[[agentic-extraction]]"]
sources: ["[[ledgermind]]"]
updated: 2026-08-11
---

# LEDGERMIND system

## What it is
LedgerMind is a training-free runtime for provenance-constrained multimodal agentic reasoning. It treats an agent trajectory as a state machine whose central state is a Structured Evidence Ledger: tool outputs are normalized into ledger entries, downstream claims may cite only active entries, grounding is verified at the entity and numeric level, and repair is a set of typed state transitions that cannot introduce content without tool-produced provenance.

## Key facts
- The Structured Evidence Ledger replaces free-form trajectory text with a runtime state in which each tool output is normalized into an entry carrying source, epistemic type, confidence, lifecycle status, and dependencies ⟨[[ledgermind]] §3.1⟩.
- Grounding is enforced by an Entity Consistency Check (ECC) and a type-aware Numeric Coherence Check (NCC), so conclusion-level entities and numeric values must be licensed by the cited evidence pool rather than by citation structure alone ⟨[[ledgermind]] §3.2⟩.
- Repair is restricted to seven typed operators in three layers (evidence, action, trajectory), giving a Provenance Non-Amplification guarantee that repair cannot add ledger entries without tool-produced provenance ⟨[[ledgermind]] §3.3⟩.
- An Adaptive Dual-Path Dispatcher matches reasoning depth to question complexity, routing simple queries to a direct path to avoid over-reasoning ⟨[[ledgermind]] §3.2⟩.
- The framework targets four failure patterns aggregate accuracy obscures: unsupported reasoning (F1), Phantom Grounding (F2), the over-reasoning paradox (F3), and repair-time amplification (F4) ⟨[[ledgermind]] §1⟩.
- The authors report improvements in both accuracy and trajectory-level faithfulness — e.g. lifting GPT-4o by +23.3 points on VTC-Bench and improving every backbone by +11.2 to +19.7 on Hard-200 — with an ablation showing removal of the ledger is the most damaging component (−15.39 overall) ⟨[[ledgermind]] §4.2 / Table 3⟩.

## Relations
- Realizes: [[provenance-constrained-extraction]] · [[extraction-self-verification]] · [[agentic-extraction]]
- Defined in: [[ledgermind]]

## See also
[[provenance-constrained-extraction]] · [[extraction-self-verification]] · [[agentic-extraction]] · [[ledgermind]]
