---
title: "CLExEval benchmark"
type: entity
subtype: benchmark
aliases: []
tags: [benchmarking]
concepts: ["[[evaluation-illusion]]", "[[human-in-the-loop-verification]]"]
sources: ["[[clexeval]]"]
published: 2026
effective_from: 2026-06
effective_to: ongoing
status: current
updated: 2026-08-10
---

# CLExEval benchmark

## What it is
CLExEval is a human-in-the-loop framework for qualitatively evaluating LLM clinical reasoning
under progressive information masking, built on the clinician-curated RARECASE-200 benchmark
and pairing four masking levels with expert-physician annotation to localize how and why
reasoning fails ⟨abstract, §3⟩.

## Key facts
- It combines 5,600 expert-physician annotations with 200 reasoning traces derived from 40
  rare diagnostic cases, and the source frames it as a depth-oriented mechanistic audit rather
  than a broad model leaderboard ⟨abstract, §3.1⟩.
- Its central construct is the "evaluation illusion," where fluent, well-structured
  explanations appear clinically convincing even when the final diagnosis is incorrect; the
  source formalizes it as an Illusion Gap (∆ = Communication − Diagnostic Precision) ⟨abstract,
  §2.2, §4.1⟩.
- It scores outputs on a seven-dimensional rubric (Diagnostic Precision, Differential
  Reasoning Quality, Evidence Integration/Grounding, Diagnostic Justification Depth,
  Completeness vs. Overload, Clinical Plausibility/Soundness, Communication/Interpretability)
  developed with senior clinicians to separate surface fluency from clinical validity ⟨§3.4,
  App C⟩.
- The source reports three recurring failure patterns using it — verbosity bias (GPT-4o-mini
  accuracy 95.0% → 32.5% under scarcity), a hidden knowledge paradox (specialist reaches 92.5%
  Max Diagnostic Potential but does not retrieve it reliably), and a 68.6% reasoning-to-output
  mismatch ⟨abstract, §4.4–4.5⟩.
- The source applies it to audit the LLM-as-a-Judge paradigm on a human-verified consensus
  failure set (n = 142), reporting Hallucination Approval Rates from 47.9% (GPT-4o-mini) up to
  100% (HuatuoGPT-o1), which it reads as standalone automated judges overestimating clinical
  reliability without expert-grounded validation ⟨abstract, §4.2, Table 2⟩.

## Relations
- Realizes: [[evaluation-illusion]] · [[human-in-the-loop-verification]]
- Defined in: [[clexeval]]

## See also
[[clexeval]]
