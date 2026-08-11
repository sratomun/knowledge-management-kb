---
title: "Expert gold standard"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[human-baseline]]", "[[rubric-based-evaluation]]"]
updated: 2026-08-10
---

# Expert gold standard

## What it is
An expert gold standard is a reference — answers, labels, or grading criteria — produced or validated by domain experts rather than crowdworkers, used as ground truth for scoring systems on tasks that require professional-level knowledge both to perform and to judge. Constructing one is costly and slow, and sources differ in what counts as "expert": credentialed practitioners writing from their own casework, recruited annotators with advanced degrees, or trained non-experts whose work is multiply verified.

## How sources treat it
- **[[euroexec]]** _(article · informational)_ — builds 413 open-ended tasks authored by 47 vetted domain experts across four business domains, each response manually evaluated by two domain-specific evaluators, with question authors supplying blind-graded ideal answers on a subset ⟨§2; §4⟩
- **[[profbench]]** _(article · informational)_ — assembles 7,347 human-written response-criterion pairs from 38 expert annotators (44.7% PhD, averaging 5.24 years post-graduation) spending ~10–20 hours per task with LLM use disallowed, and reports Fleiss' κ = 0.912 agreement used as the human gold standard for judging ⟨§3; §4.1⟩
- **[[clexeval]]** _(article · informational)_ — combines 5,600 expert-physician annotations with a seven-dimensional rubric developed iteratively with senior clinicians, and uses a human-verified consensus failure set to audit automated judges ⟨§3.1; §3.4⟩
- **[[italian-legal-turing]]** _(article · informational)_ — adopts the highest-scoring human essay from each real national exam's official final rankings as a top-tier human benchmark, with anonymized papers scored blind by three examiners who had served on national board committees ⟨§II; §IV⟩
- **[[cuad]]** _(article · informational)_ — creates its contract-review gold standard with dozens of legal experts and law-student annotators trained 70–100 hours who followed 100+ pages of rules, with each annotation verified by three additional annotators ⟨§1; §3⟩

## Where sources differ
The sources use different constructions of "expert." [[euroexec]] and [[italian-legal-turing]] draw their gold standard from practicing professionals' own work and official exam rankings, [[profbench]] from recruited credentialed annotators who write both prompts and grading criteria, [[clexeval]] from a physician panel building a clinical rubric, and [[cuad]] from trained law students whose annotations are multiply verified. They also differ on scope — a fixed set of reference model responses ([[profbench]]) versus per-task human answers ([[euroexec]]). The KB records these as distinct expert-grounding designs.

## See also
[[human-baseline]]
[[rubric-based-evaluation]]
[[inter-annotator-agreement]]
