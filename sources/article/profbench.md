---
title: "ProfBench: Multi-Domain Rubrics Requiring Professional Knowledge to Answer and Judge"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["ProfBench"]
publisher: "Zhilin Wang, Jaehun Jung, Ximing Lu et al. (NVIDIA)"
url: https://arxiv.org/abs/2510.18941
version: "arXiv:2510.18941v2 [cs.CL]; ICLR 2026"
published: 2025
effective_from: 2025
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[rubric-based-evaluation]]", "[[expert-gold-standard]]", "[[human-parity]]"]
entities: ["[[profbench]]"]
updated: 2026-08-10
---

# ProfBench: Multi-Domain Rubrics Requiring Professional Knowledge to Answer and Judge

## Scope & purpose
An NVIDIA benchmark paper (ICLR 2026) that targets tasks needing professional-level knowledge both to answer and to judge — processing professional documents, synthesizing information, and generating comprehensive reports — which the authors argue existing verification-limited benchmarks (math, code, short-form QA) cannot cover ⟨Abstract; §1⟩. ProfBench provides over 7,000 human-written response-criterion pairs across four expert domains (Physics PhD, Chemistry PhD, Finance MBA, Consulting MBA) and builds affordable, low-bias LLM-Judges to grade rubric fulfillment ⟨Abstract; §2⟩. The authors position it as challenging for state-of-the-art LLMs and as a fairer, cheaper rubric-based evaluation than prior work ⟨Abstract; §1⟩. The KB records the paper's comparative claims (challenging, best-performing, human-agreement) descriptively.

## Key points
- ProfBench contains 7,347 human-written response-criterion pairs across 80 tasks equally split among four professional domains — Physics PhD, Chemistry PhD, Finance MBA, Consulting MBA — with rubrics dominated by Reasoning criteria (62.9%), then Extraction (34.1%) and Style (3.0%) ⟨§2; Figure 2⟩
- Tasks were created by 38 recruited expert annotators from 8 countries (44.7% PhD, 18.4% MBA, others with relevant degrees plus experience, averaging 5.24 years post-graduation), each spending ~10–20 hours per task, with LLM use disallowed at every annotation stage ⟨§3⟩
- Each annotator wrote the prompt, 15–60 grading criteria (with description, justification, importance, and type), and scored three model responses (OpenAI o3, Grok4, DeepSeek R1-0528) as Yes/No per criterion; 41.4% of criteria were flagged for improvement in review, reflecting the quality bar ⟨§3⟩
- The paper reports ProfBench is challenging even for state-of-the-art LLMs: as a report-generator, the top model GPT-5-high reaches only 65.9% overall — which the authors contrast with the same model's 94.6% on AIME 25, 87.0% on GPQA-Diamond, and 72.4% on SWE-Bench Verified to underline the difficulty ⟨Abstract; §5.1; Table 3⟩
- Reported domain difficulty for report generation: Physics is hardest (49.3%), then Finance (63.8%), Chemistry (70.6%), and Consulting (80.0%) ⟨§5.1; Table 3⟩
- The authors report notable proprietary-vs-open-weight gaps: top open-weight models GPT-OSS-120b (54.9%) and DeepSeek V3.1-Thinking (53.8%) trail leaders GPT-5 (65.9%), o3 (61.4%), and Gemini 2.5 Pro (60.3%), with the gap small in Physics (<1%) but large in Finance (15.0%) ⟨§5.1⟩
- On judging, the paper reports inter-annotator agreement of Fleiss' κ = 0.912 on a 1,127-pair re-annotation, described as excellent agreement and used as the human gold standard against which LLM-Judges are measured ⟨§4.1⟩
- LLM-Judges are scored by Macro-F1 agreement with human labels minus a Bias-Index (max−min self-enhancement bias across the three response models); the authors report the best proprietary judge Gemini-2.5-Pro at 78.2% Overall and note top open-weight judges are often close behind ⟨§4.1; §4.2; Table 2⟩
- The authors report their engineered GPT-OSS-120B judge (high reasoning effort for Physics/Chemistry/Style criteria, low for others) matches the best proprietary judge at 78.2% Overall while costing only 1.68% as much ($0.70 vs $1,320 for PaperBench JudgeEval) — a claimed 2–3 orders of magnitude cost reduction ⟨§4.2; §1⟩
- The paper reports self-enhancement bias grows with reasoning effort (bias toward OpenAI o3 responses generally increases), which is why higher effort raises human agreement but also bias — informing the domain-adaptive judge design ⟨§4.2⟩
- On "to think or not to think," the authors report enabling thinking gives small gains (0.3–2.3%) for a fixed model, and GPT-5 improves 4.8% from minimal to high reasoning, but a separately-trained thinking model does not always beat its instruct sibling (Qwen3-30B-A3B-Thinking 44.6% vs Instruct 49.3%), partly a response-length effect ⟨§4.2; §5.1⟩
- The paper reports that response length helps up to a point — very short generations underperform (Claude-3.5-Haiku at 27.6%, ~1,784 chars) — but beyond a threshold longer responses do not warrant better scores ⟨§5.1⟩
- The scoring schema is validated against human annotations: judge-predicted performance sits within 0.7–1.3% of human-annotated performance across the three annotated models ⟨§5⟩
- Stated hedges/limitations: only half the dataset is public (half held private to mitigate contamination); documents were truncated to ≤20 pages to ease retrieval; expert judgments exist only for the three July-2025 reference models, so adding models needs the full costly annotation pipeline; the benchmark can be adapted (full-length documents) as models saturate it ⟨§4.1; Appendix / Limitations⟩

## Concepts & entities covered
Concepts: [[rubric-based-evaluation]] · [[expert-gold-standard]] · [[human-parity]]
Entities: [[profbench]]
