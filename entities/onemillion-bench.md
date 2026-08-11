---
title: "$OneMillion-Bench"
type: entity
subtype: benchmark
aliases: []
tags: [benchmarking]
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
concepts: ["[[human-parity]]", "[[rubric-based-evaluation]]", "[[realistic-performance-expectations]]", "[[llm-failure-modes]]"]
sources: ["[[onemillion-bench]]"]
updated: 2026-08-10
---

# $OneMillion-Bench

## What it is
$OneMillion-Bench ($1M-Bench) is a benchmark of 400 expert-curated, economically-valued professional tasks across Law, Finance, Industry, Healthcare, and Natural Science, built to measure how far long-horizon LLM agents are from human experts. Each task is priced by senior-professional time and wage, and responses are graded by a rubric-based Expert Score and Pass Rate.

## Key facts
- It contains 400 open-ended tasks across five high-stakes domains (80 each), partitioned into 37 sub-domains and 86 third-level categories, curated over more than 2,000 expert hours ⟨[[onemillion-bench]] §1; §3.2⟩.
- Each task is assigned a real monetary value (expert completion time × market hourly wage); the reported totals exceed $1 million (~$1,008,370 Global; ~¥921,832 CN), giving the benchmark its name ⟨[[onemillion-bench]] §2.1; Table 1⟩.
- It is bilingual — 200 English and 200 Chinese instances — with the Chinese set purpose-built around Mainland-China regulations rather than translated ⟨[[onemillion-bench]] §3.2⟩.
- Responses are scored by a weighted-rubric Expert Score (clipped to [0,1]) and a Pass Rate (fraction of tasks with Expert Score ≥ 0.7), with negative rubric weights from −20 to +10 penalizing violations, unsafe output, and hallucination ⟨[[onemillion-bench]] §2.2; §3.2⟩.
- The authors report CLAUDE-OPUS-4.6 is the clear leader, reaching 55.0 → 63.0 Expert Score and 36.5% → 43.5% Pass Rate on the Global set once web search is enabled, top among the 35 evaluated systems ⟨[[onemillion-bench]] §4.2; Table 3⟩.
- The authors report many models reach ~45–50% Expert Score but Pass Rates often below ~25%, indicating broad-but-shallow rubric satisfaction rather than clearing the professional competence threshold ⟨[[onemillion-bench]] §4.2⟩.
- The authors report web search is not always beneficial — it amplifies strong models but causes regressions for weaker ones (e.g. HUNYUAN-2.0 drops 34.7 → 30.2 Expert Score) — acting as an efficacy amplifier ⟨[[onemillion-bench]] §4.2; §4.3⟩.
- Documented failure modes include outdated/incompatible-guideline retrieval, arithmetic and extraction errors in finance, imprecise mapping of facts to legal provisions, and shallow multi-step reasoning ⟨[[onemillion-bench]] §5.4⟩.
- Stated hedges: rubrics are less objective than a single-expression checker and rely on model-judge capability, and full manual scoring is hard to scale ⟨[[onemillion-bench]] §5.3⟩.

## Relations
- Realizes: [[human-parity]] · [[rubric-based-evaluation]] · [[realistic-performance-expectations]] · [[llm-failure-modes]]
- Defined in: [[onemillion-bench]]

## See also
[[human-parity]] · [[realistic-performance-expectations]] · [[llm-failure-modes]] · [[onemillion-bench]]
