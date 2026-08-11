---
title: "LLM-as-judge bias"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[benchmark-validity]]", "[[rubric-based-evaluation]]"]
updated: 2026-08-10
---

# LLM-as-judge bias

## What it is
LLM-as-judge bias refers to systematic distortions that arise when an LLM is used to score or rank other systems' outputs — including positional preference (favoring a presentation slot), self-enhancement (favoring outputs resembling the judge's own), false preference under no evaluative signal, and sensitivity to non-target surface form. These distortions mean a judge's scalar score can misrepresent quality, so sources argue the judge itself must be characterized as a measurement instrument, or replaced by a human, before its verdicts are trusted.

## How sources treat it
- **[[llm-judge-dark-current]]** _(article · informational)_ — proposes a "Judge Datasheet" characterizing a judge across five axes (dark current, stable cross-sensitivity, positional false preference, target sensitivity, and criterion), defining dark current as false preference under true-vacuum inputs such as empty or identical answers ⟨§1; §3.3⟩
- **[[llm-judge-dark-current]]** _(article · informational)_ — in a three-judge study reports Llama-3.1-8B with dark current 0.667 and positional false preference 0.967, versus Qwen2.5-32B as the cleanest profile (dark current 0.000), arguing a scalar win-rate is insufficient because it collapses distinct failure modes ⟨§4⟩
- **[[llm-judge-dark-current]]** _(article · informational)_ — reports that "prompting moves the criterion, not the resolution": a strict-tie prompt eliminates ∆0 false preference but absorbs marginal ∆1 target signal into ties rather than fixing the judge ⟨§5⟩
- **[[profbench]]** _(article · informational)_ — scores LLM-Judges by human-agreement minus a Bias-Index (max−min self-enhancement across response models) and reports self-enhancement bias growing with reasoning effort, so higher effort raises agreement but also bias ⟨§4.2⟩
- **[[euroexec]]** _(article · informational)_ — reports a single AI judge correlated with human scores better than human evaluators did with each other, but argues this is an artifact: the judge over-estimates the best models and under-estimates the worst, producing "too crisp" evaluations that miss the diversity of human opinion ⟨§5.4⟩
- **[[agreement-is-not-quality]]** _(article · informational)_ — deliberately uses a human domain expert rather than an LLM judge to preserve domain authority, citing prior work that LLM judges can show reliability without validity ⟨Related Work⟩

## Where sources differ
[[llm-judge-dark-current]] treats judge bias as a set of measurable instrument properties independent of any human ground truth, [[profbench]] and [[euroexec]] quantify self-enhancement and over-crispness within a working evaluation, and [[agreement-is-not-quality]] responds by avoiding LLM judges altogether. The sources thus split between measuring, correcting for, and side-stepping the bias. The KB records each stance descriptively.

## See also
[[benchmark-validity]]
[[rubric-based-evaluation]]
[[evaluation-illusion]]
