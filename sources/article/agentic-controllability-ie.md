---
title: "Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Agentic Controllability IE"]
publisher: "Lujia Zhang, Xingzhou Chen, Hongwei Feng"
url: https://arxiv.org/abs/2607.15715
version: "arXiv:2607.15715v1 [cs.AI]"
published: 2026
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-11
---

# Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents

## Scope & purpose
This paper is a critical, deliberately neutral study of whether agentic components — reflection and memory — actually yield observable and controllable improvements over fixed LLM workflows for information extraction (IE). It is studied through scholarly dataset extraction: given conference-paper PDFs and metadata, output structured JSONL dataset records (name, description, type/domain, paper refs, link, platform). The authors emphasize process-level behavior (tool execution, retries, reflection, memory use, runtime, failure recovery) over extraction coverage, which they treat as a secondary signal.

## Structure
The paper motivates the question of whether agentic mechanisms help IE, specifies four conditions (S0–S2), reports paired output and process metrics (Tables 1–2), presents case studies of reflection behavior, draws design lessons, and closes with limitations.

## Key points
- The study asks whether agentic components such as reflection and memory lead to observable, controllable improvements over fixed LLM workflows, defining "behavioral controllability" as observability + configurability + reproducibility + comparability ⟨arXiv:2607.15715, Abstract / Setup⟩.
- All conditions share one output schema so differences are attributable to system behavior: S0 Workflow (fixed sequence, no reflection/memory/retry); S1a Agent with rule reflection; S1b Agent with LLM reflection; S2 Optimized Agent (twelve atomic tools with state-dependent selection, specified as design only, numerical evaluation reserved for follow-up) ⟨arXiv:2607.15715, Setup⟩.
- The authors report that the agent harness increases coverage only modestly: S0 produces 158 records (42 papers, link rate 0.190), S1a 165, and S1b 168 — so S1b yields only ten more records than S0, and LLM reflection adds only three records over rule reflection ⟨arXiv:2607.15715, Table 1⟩.
- Process signals contrast sharply with those modest output gains: log lines rise from 7,084 (S0) to 50,189 (S1), with 1,967 reflection mentions, 1,388 observations, and 2,222 retries — "substantially more internal activity even when additional records are modest" ⟨arXiv:2607.15715, Table 2⟩.
- The main finding is that the stronger difference is behavioral, not outcome: "the available evidence is stronger for behavioral change than for absolute accuracy improvement," and rule reflection already accounts for much of the measurable output change, so indiscriminate deep LLM reflection "may not be justified for every paper" ⟨arXiv:2607.15715, Key results⟩.
- The authors cite Huang et al. 2024, "Large Language Models Cannot Self-Correct Reasoning Yet," noting intrinsic self-correction without reliable external feedback often fails on reasoning tasks and can degrade performance — consistent with their finding ⟨arXiv:2607.15715, Key results⟩.
- Link grounding (source-URL extraction) is a persistent weakness, staying below 20% across all systems as a bottleneck independent of the agent harness; S2 responds by making URL matching, citation search, and evidence verification first-class tools ⟨arXiv:2607.15715, Key results⟩.
- Design lessons: reflection should be tied to observable deficiencies (empty outputs, low counts despite cues, missing fields); memory needs provenance and quality control or prior experiences become prompt noise; controllability is a property of the whole harness (logging, config, manifests, schemas), and the workflow is attractive for cheap predictable batch extraction while the agent suits heterogeneous corpora and diagnosable failures ⟨arXiv:2607.15715, Design lessons⟩.
- Stated limitations: a single corpus (NeurIPS 2024, ≤50 papers), one model family, no complete human gold standard (so no absolute precision/recall claims), combined architectural and prompt changes, and process metrics that reveal what the harness logs rather than faithful access to the model's internal reasoning ⟨arXiv:2607.15715, Limitations⟩.

## Concepts & entities covered
Concepts: [[agentic-extraction]] · [[agentic-reflection-control]]
Entities: —
