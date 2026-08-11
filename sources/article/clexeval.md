---
title: "CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["CLExEval"]
publisher: arXiv
url: https://arxiv.org/abs/2606.31608
published: 2026
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[evaluation-illusion]]", "[[human-in-the-loop-verification]]", "[[rubric-based-evaluation]]", "[[expert-gold-standard]]"]
entities: ["[[clexeval-benchmark]]"]
updated: 2026-08-10
---

# CLExEval: A Human-in-the-Loop Framework for Qualitative Evaluation of LLM Clinical Reasoning

## Scope & purpose

CLExEval, from researchers at MBZUAI, IIT Madras, and Calicut Medical College, is a
human-in-the-loop framework for qualitatively evaluating LLM clinical reasoning under
progressive information masking. The authors motivate it against the observation that LLMs
score well on many medical benchmarks yet their clinical reasoning remains hard to evaluate
reliably, and they warn of a central risk they call the "evaluation illusion": fluent,
well-structured explanations can appear clinically convincing even when the final diagnosis
is incorrect ⟨abstract, §1⟩.

## Structure

The paper runs: abstract and introduction motivating the evaluation illusion and the blind
spots of final-answer accuracy (§1); related work on clinical task design and the judge's
illusion (§2); methodology — the RARECASE-200 dataset, progressive information masking
(Levels 0–3), model evaluation, the seven-dimensional CLExEval rubric, and reasoning metrics
(§3); results on the evaluation illusion, limits of automated judges, human evaluation, and
reasoning-to-output mismatch (§4); discussion and conclusions (§5–6); limitations and ethics;
and appendices with prompt templates, rubric definitions, and metric formulas ⟨§1–6, App A–H⟩.

## Key points

- The framework combines 5,600 expert-physician annotations with 200 clinical reasoning
  traces derived from 40 rare diagnostic cases, and the authors frame it explicitly as a
  depth-oriented mechanistic audit rather than a broad model leaderboard ⟨abstract, §3.1⟩.
- The authors define the evaluation illusion as a case where fluent, well-structured reasoning
  is over-rewarded despite weak clinical validity, and formalize an Illusion Gap
  (∆ = Communication − Diagnostic Precision); they report a Diagnostic Precision drop to 0.453
  at Level 3 while GPT-4o-mini's Communication score stayed at 0.881, with only a modest
  correlation (ρ = 0.482) between the two ⟨§2.2, §4.1⟩.
- The seven-dimensional CLExEval rubric — Diagnostic Precision, Differential Reasoning Quality,
  Evidence Integration/Grounding, Diagnostic Justification Depth, Completeness vs. Overload,
  Clinical Plausibility/Soundness, and Communication/Interpretability — was developed through
  iterative review with senior clinicians specifically to separate surface fluency from
  clinical validity, and is scored on a five-point ordinal scale (0.00–1.00) ⟨§3.4, App C⟩.
- The authors report three recurring failure patterns: (i) verbosity bias, where GPT-4o-mini's
  diagnostic accuracy drops from 95.0% to 32.5% under information scarcity (62.5 pp ISS);
  (ii) a hidden knowledge paradox, where the specialist HuatuoGPT reaches 92.5% Max Diagnostic
  Potential but fails to retrieve that knowledge reliably in verbose contexts; and (iii) a
  68.6% reasoning-to-output mismatch (ROM), where the correct diagnosis appears in the
  reasoning trace but not the final answer ⟨abstract, §4.4–4.5⟩.
- In the expert human evaluation (inter-rater reliability ICC = 0.802), the authors report
  that the generalist GPT-4o-mini significantly outperformed the biomedically fine-tuned
  HuatuoGPT across all seven dimensions (mean overall 0.867 vs. 0.699, d = 0.98), while noting
  that HuatuoGPT nonetheless reached a higher latent Max Diagnostic Potential; they attribute
  the generalist's edge partly to instruction tuning for fluent, structured explanations — a
  "Generalist's Illusion" where articulation can inflate perceived clinical capability ⟨§4.3⟩.
- On a human-verified consensus failure set (n = 142), the authors evaluate the
  LLM-as-a-Judge paradigm and report that automated judges frequently approved clinically
  incorrect outputs: GPT-4o-mini had the lowest Hallucination Approval Rate at 47.9%, while
  the specialized HuatuoGPT-o1 approved all validly scored failures (100% HAR) and showed a
  positive self-preference bias (+0.096) — leading them to state that domain-specific tuning
  did not produce stricter evaluation here ⟨abstract, §4.2, Table 2, App E⟩.
- The authors conclude that standalone automated clinical evaluations can substantially
  overestimate clinical reliability without expert-grounded validation, and that LLM-based
  evaluation should be paired with human-in-the-loop expert validation, especially where
  surface fluency can obscure diagnostic correctness ⟨abstract, §5–6⟩.
- The authors state several limitations as hedges on scope: the depth-for-scale trade-off
  limited the study to two models and 40 source cases (≈1,000 expert hours); the panel
  included two senior clinical interns rather than only licensed physicians; the deliberate
  focus on rare, multisystem cases may not reflect performance on routine scenarios; and while
  the masking-and-rubric method is said to be conceptually generalizable to other domains
  (e.g. law, intelligence analysis), empirical validation remains confined to clinical
  medicine ⟨Limitations⟩.

## Concepts & entities covered
Concepts: [[evaluation-illusion]] · [[human-in-the-loop-verification]] · [[rubric-based-evaluation]] · [[expert-gold-standard]]
Entities: [[clexeval-benchmark]]
