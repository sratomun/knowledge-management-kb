---
title: "Human parity"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[human-baseline]]", "[[realistic-performance-expectations]]", "[[llm-failure-modes]]"]
updated: 2026-08-10
---

# Human parity

## What it is
Human parity is the claim or condition that an automated system matches human performance on a task. In human-vs-LLM benchmarking it is a contested, highly task-dependent notion: sources report models reaching, exceeding, or falling short of a human benchmark depending on the task type, domain, evaluation instrument, and whether the comparison is against an average human or a top performer. The KB records each parity, sub-parity, or super-parity claim as the reporting source's finding, never as an adjudicated fact about who is better.

## How sources treat it
- **[[euroexec]]** _(article · informational)_ — reports the strongest model (Fable 5) solves 56.9% of European executive decision tasks versus a 92.4% Solve Rate for expert reference answers, with experts preferred in 74.24% of rankings; the authors characterize frontier models as falling well below the professional standard ⟨Abstract; Table 4⟩
- **[[italian-legal-turing]]** _(article · informational)_ — reports some out-of-the-box LLMs match or exceed the top human on the Bar exam (Gemini 2.5 Pro 79 vs human 62) and Judicial exam (Gemini 21/24 vs 18/24), yet all models fell significantly below the human benchmark on the notary exam; the authors stress performance is strongly task- and model-dependent and that a few high performers do not make LLMs capable "as a class" ⟨§VI; §VII⟩
- **[[onemillion-bench]]** _(article · informational)_ — reports the top agent (Claude-Opus-4.6 with search) reaches 63.0 Expert Score and 43.5% Pass Rate on the Global set, and reads the gap between moderate rubric satisfaction and low Pass Rates as leaving most economically-valuable tasks below the professional bar ⟨§4.2⟩
- **[[occubench]]** _(article · informational)_ — reports no single model dominates all industries (GPT-5.2 leads overall at 79.6% but scores 67% in Commerce; Gemini 3.1 Pro leads Education at 84% yet struggles in Healthcare at 62%), arguing each model has a distinct occupational capability profile ⟨§6.1⟩
- **[[profbench]]** _(article · informational)_ — reports the top report-generating model GPT-5-high reaches only 65.9% overall, contrasted against the same model's 94.6% on AIME 25 and 87.0% on GPQA-Diamond to underline how far professional tasks sit from parity ⟨§5.1⟩
- **[[automation-narrative-flaws]]** _(article · informational)_ — critiques the "automation narrative" (citing GDPVal's claim that ChatGPT 5.2 performs at or above human workers 74.9% of the time), arguing benchmark-accuracy metrics overstate expert-equivalence and reporting that ChatGPT Codex 5.2 was not equivalent to their ensemble of PhD experts ⟨§1; §4⟩

## Where sources differ
The sources report divergent parity pictures rather than a single verdict. [[euroexec]], [[profbench]], and [[automation-narrative-flaws]] emphasize consistent shortfall against experts; [[italian-legal-turing]] reports parity or better on some legal tasks and clear failure on others; [[occubench]] reports that "who leads" changes by industry, so an aggregate parity claim obscures per-domain profiles. The divergence is descriptive — different tasks, instruments, and model snapshots — and the KB does not reconcile them into a ranking.

## See also
[[human-baseline]]
[[realistic-performance-expectations]]
[[llm-failure-modes]]
