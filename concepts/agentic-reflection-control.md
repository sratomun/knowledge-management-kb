---
title: "Agentic Reflection Control"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[agentic-extraction]]", "[[extraction-self-verification]]"]
updated: 2026-08-11
---

# Agentic Reflection Control

## What it is
Agentic reflection control is the question of whether, and how, an extraction agent's reflection and memory mechanisms should be governed — when to reflect, on what signal, and how to make the behavior observable, configurable, and comparable rather than an opaque source of extra activity. It treats reflection not as an unconditional good but as a mechanism whose benefit must be measured at the process level (retries, reflection mentions, runtime, failure recovery) against its effect on outcomes.

## How sources treat it
- **[[agentic-controllability-ie]]** _(article · informational)_ — Defines "behavioral controllability" as observability + configurability + reproducibility + comparability, and compares four conditions sharing one output schema: S0 Workflow (no reflection/memory/retry), S1a rule reflection, S1b LLM reflection, S2 optimized agent ⟨Abstract / Setup⟩
- **[[agentic-controllability-ie]]** _(article · informational)_ — Reports the agent harness increases coverage only modestly (S0 158 records → S1a 165 → S1b 168), so LLM reflection adds only three records over rule reflection, while process signals rise sharply (7,084 → 50,189 log lines, 1,967 reflection mentions, 2,222 retries) ⟨Table 1; Table 2⟩
- **[[agentic-controllability-ie]]** _(article · informational)_ — Its main finding is that the stronger difference is behavioral, not outcome — "evidence is stronger for behavioral change than for absolute accuracy improvement" — and that rule reflection already accounts for much of the measurable output change, so indiscriminate deep LLM reflection "may not be justified for every paper" ⟨Key results⟩
- **[[agentic-controllability-ie]]** _(article · informational)_ — Cites Huang et al. 2024 ("LLMs Cannot Self-Correct Reasoning Yet") that intrinsic self-correction without reliable external feedback often fails and can degrade performance, and draws the design lesson that reflection should be tied to observable deficiencies (empty outputs, low counts despite cues, missing fields) and memory needs provenance and quality control ⟨Key results; Design lessons⟩

## Where sources differ
This concept is grounded in a single source, so there is no cross-source divergence to report. Internally, [[agentic-controllability-ie]] draws a contrast between rule-based and LLM-based reflection (finding the former captures most of the measurable gain) and between process metrics and outcome metrics (finding the two diverge). It states its own hedges: a single corpus (NeurIPS 2024, ≤50 papers), one model family, no complete human gold standard so no absolute precision/recall claims, and process metrics that reveal what the harness logs rather than the model's internal reasoning.

## See also
[[agentic-extraction]] · [[extraction-self-verification]] · [[extraction-verification]] · [[human-in-the-loop-verification]]
