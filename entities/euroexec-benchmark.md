---
title: "EuroExec benchmark"
type: entity
subtype: benchmark
aliases: []
tags: [benchmarking]
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
concepts: ["[[human-baseline]]", "[[human-parity]]", "[[expert-gold-standard]]", "[[realistic-performance-expectations]]"]
sources: ["[[euroexec]]"]
updated: 2026-08-10
---

# EuroExec benchmark

## What it is
EuroExec is a human-expert-based benchmark of 413 open-ended, long-form European executive decision-making tasks, authored by 47 vetted domain experts and used to evaluate frontier LLMs against expert judgment. Its authors report that frontier models fall short of the professional standard the experts meet, and that human evaluation outperforms automatic metrics on this class of subjective, open-ended tasks.

## Key facts
- It comprises 413 open-ended long-form tasks authored by 47 vetted domain experts across four domains — Finance, Marketing, Business, and Product — each drawn from a real case in the author's professional experience ⟨[[euroexec]] §2; Table 1⟩.
- It evaluates six frontier LLMs (Fable 5, Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, GLM-5.2, Mistral Large) via three human-scored instruments: a five-attribute rubric, an item-specific checklist, and a preference ranking ⟨[[euroexec]] §3; §4; Table 3⟩.
- Its aggregate "Solve Rate" counts a task solved when the mean rubric score is ≥ 3.0 and checklist fulfillment is ≥ 60%, described by the authors as a generous passing grade ⟨[[euroexec]] §4⟩.
- The authors report the strongest model (Fable 5) solves only 56.9% of tasks while blindly-judged expert reference answers reach a near-ceiling 92.4% Solve Rate ⟨[[euroexec]] Abstract; Table 4⟩.
- The authors report expert-written reference answers were preferred over every model response in 74.24% of direct rankings, versus 49.5% for the best model ⟨[[euroexec]] Table 4; §5⟩.
- More than 4,000 human-expert hours were dedicated to the evaluation, with responses averaging ~44,000 characters and roughly 5 hours to grade the six responses per item ⟨[[euroexec]] §4⟩.
- The authors report that automatic metrics fall short: ROUGE-Lsum and BLEU correlate only weakly with human rubric scores and do not reproduce the ranking, and a single LLM judge inflates the correlation as an artifact by over-estimating the best models and under-estimating the worst ⟨[[euroexec]] §5.4⟩.
- Stated limitations include only 33 of 413 items having expert-written ideal answers, high evaluation cost, poor reproducibility to new models, and a deferred qualitative failure-mode analysis ⟨[[euroexec]] Limitations⟩.

## Relations
- Realizes: [[human-baseline]] · [[human-parity]] · [[expert-gold-standard]] · [[realistic-performance-expectations]]
- Defined in: [[euroexec]]

## See also
[[human-baseline]] · [[expert-gold-standard]] · [[realistic-performance-expectations]] · [[euroexec]]
