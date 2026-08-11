---
title: "Rubric-based evaluation"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[expert-gold-standard]]", "[[llm-as-judge-bias]]"]
updated: 2026-08-10
---

# Rubric-based evaluation

## What it is
Rubric-based evaluation scores open-ended, long-form responses against an explicit set of criteria — a multi-attribute rubric or an item-specific checklist — rather than against a single exact-match gold answer. Each criterion is judged for fulfillment (often Yes/No or on an ordinal scale) and the results are aggregated into a score, making it possible to grade tasks where no unique correct output exists. The design choices — how many criteria, binary vs. ordinal scoring, and who or what applies the rubric — vary across sources and materially shape what the score measures.

## How sources treat it
- **[[profbench]]** _(article · informational)_ — grades 80 professional tasks against 15–60 human-written criteria each (with description, justification, importance, and type), scored Yes/No per criterion, with rubrics dominated by Reasoning (62.9%), then Extraction (34.1%) and Style (3.0%) ⟨§2; §3⟩
- **[[profbench]]** _(article · informational)_ — builds affordable LLM-Judges to grade rubric fulfillment, reporting the best proprietary judge (Gemini-2.5-Pro) at 78.2% Overall and an engineered domain-adaptive GPT-OSS-120B judge matching it at 1.68% of the cost ⟨§4.2⟩
- **[[clexeval]]** _(article · informational)_ — applies a seven-dimensional rubric (Diagnostic Precision, Differential Reasoning Quality, Evidence Integration, Justification Depth, Completeness vs. Overload, Clinical Plausibility, Communication) on a five-point ordinal scale, developed with senior clinicians specifically to separate surface fluency from clinical validity ⟨§3.4⟩
- **[[clexeval]]** _(article · informational)_ — reports rubric dimensions can decouple: it formalizes an Illusion Gap (Communication − Diagnostic Precision) and reports Communication staying at 0.881 while Diagnostic Precision dropped to 0.453 under information masking ⟨§4.1⟩

## Where sources differ
[[profbench]] uses many binary Yes/No criteria aggregated via F1 agreement and foregrounds making the LLM-judge cheap and low-bias; [[clexeval]] uses a smaller set of ordinal dimensions and foregrounds that a well-scored rubric can still be gamed by fluency, motivating human-in-the-loop validation. One treats the rubric as an efficiency lever, the other as a diagnostic that must be guarded against the evaluation illusion. The KB records both uses of rubric scoring without ranking them.

## See also
[[expert-gold-standard]]
[[llm-as-judge-bias]]
[[evaluation-illusion]]
