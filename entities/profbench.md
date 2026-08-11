---
title: "ProfBench"
type: entity
subtype: benchmark
aliases: []
tags: [benchmarking]
published: 2025
effective_from: 2025
effective_to: ongoing
status: current
concepts: ["[[rubric-based-evaluation]]", "[[expert-gold-standard]]", "[[human-parity]]"]
sources: ["[[profbench]]"]
updated: 2026-08-10
---

# ProfBench

## What it is
ProfBench is an NVIDIA benchmark of over 7,000 human-written response-criterion pairs across four professional domains (Physics PhD, Chemistry PhD, Finance MBA, Consulting MBA), designed for tasks that require professional knowledge both to answer and to judge. It pairs expert-created rubrics with affordable, low-bias LLM-Judges to grade open-ended report-generation.

## Key facts
- It contains 7,347 human-written response-criterion pairs across 80 tasks equally split among Physics PhD, Chemistry PhD, Finance MBA, and Consulting MBA, with rubrics dominated by Reasoning criteria (62.9%), then Extraction (34.1%) and Style (3.0%) ⟨[[profbench]] §2; Figure 2⟩.
- Tasks were built by 38 expert annotators from 8 countries (each ~10–20 hours per task, LLM use disallowed), who wrote the prompt, 15–60 grading criteria, and Yes/No scores for three reference-model responses (o3, Grok4, DeepSeek R1-0528) ⟨[[profbench]] §3⟩.
- The authors report it is challenging even for state-of-the-art LLMs: top report-generator GPT-5-high reaches only 65.9% overall, contrasted with the same model's 94.6% on AIME 25 and 87.0% on GPQA-Diamond ⟨[[profbench]] Abstract; §5.1; Table 3⟩.
- Reported per-domain difficulty for report generation: Physics hardest (49.3%), then Finance (63.8%), Chemistry (70.6%), and Consulting (80.0%) ⟨[[profbench]] §5.1; Table 3⟩.
- The authors report proprietary-vs-open-weight gaps: top open-weight GPT-OSS-120b (54.9%) trails leaders GPT-5 (65.9%) and o3 (61.4%), with the gap small in Physics (<1%) but large in Finance (15.0%) ⟨[[profbench]] §5.1⟩.
- Human inter-annotator agreement is reported as Fleiss' κ = 0.912 on a 1,127-pair re-annotation, used as the gold standard against which LLM-Judges are measured by Macro-F1 minus a Bias-Index ⟨[[profbench]] §4.1⟩.
- The authors report their engineered GPT-OSS-120B judge matches the best proprietary judge (Gemini-2.5-Pro) at 78.2% Overall while costing only 1.68% as much, a claimed 2–3 orders of magnitude cost reduction ⟨[[profbench]] §4.2; §1⟩.
- The judge-based scoring schema is validated to within 0.7–1.3% of human-annotated performance across the three annotated models ⟨[[profbench]] §5⟩.
- Stated hedges: only half the dataset is public (half held private against contamination), documents were truncated to ≤20 pages, and expert judgments exist only for the three July-2025 reference models ⟨[[profbench]] §4.1; Limitations⟩.

## Relations
- Realizes: [[rubric-based-evaluation]] · [[expert-gold-standard]] · [[human-parity]]
- Defined in: [[profbench]]

## See also
[[rubric-based-evaluation]] · [[expert-gold-standard]] · [[human-parity]] · [[profbench]]
