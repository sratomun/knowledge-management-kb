---
title: "EuroExec: Frontier Language Models Fall Short of Expert Judgment on European Executive Decision Tasks"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["EuroExec"]
publisher: "Pau Arnal, Khaled Denfir, Danylo Smahliuk, Amrut Avhad & Marcus A. Castro (Sovrano AI)"
url: https://arxiv.org/abs/2608.04549
version: "arXiv:2608.04549v1 [cs.CL]"
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[human-baseline]]", "[[human-parity]]", "[[expert-gold-standard]]", "[[realistic-performance-expectations]]"]
entities: ["[[euroexec-benchmark]]"]
updated: 2026-08-10
---

# EuroExec: Frontier Language Models Fall Short of Expert Judgment on European Executive Decision Tasks

## Scope & purpose
A human-expert-based benchmark paper by a Sovrano AI team that evaluates six frontier LLMs on open-ended, long-form European executive decision-making tasks — a class of real-world problems the authors argue differs in nature from the close-ended, gold-answer tasks LLMs are usually measured on ⟨Abstract; §1⟩. The authors dedicate more than 4,000 human-expert hours to manually evaluate model responses through three instruments (a multi-attribute rubric, an item-specific checklist, and a preference rank ordering), and report that all frontier models fall short of the professional standard the human experts meet comfortably ⟨Abstract; §1; §6⟩. The paper's stated secondary conclusion is that, for this class of open-ended tasks with a subjective ground truth, human evaluation remains unmatched by automatic metrics ⟨Abstract; §6⟩. The KB records these as the paper's own comparative claims, not as adjudicated fact.

## Key points
- The study evaluates six frontier LLMs — Fable 5 and Claude Opus 4.8 (Anthropic), GPT-5.5 (OpenAI), Gemini 3.1 Pro (Google), GLM-5.2 (Zhipu AI), and Mistral Large (Mistral AI) — each queried through its provider API with default decoding and no system prompt, tools, or context, consistent with the self-contained task design ⟨§3; Table 3⟩
- The benchmark comprises 413 open-ended long-form tasks authored by 47 vetted domain experts across four domains — Finance (10 experts, 74 questions), Marketing (11, 85), Business (14, 113), and Product (12, 141) — each question drawn from a real case in the author's own professional experience ⟨§2; Table 1⟩
- Every response is manually evaluated by two domain-specific evaluators on three instruments: a common five-attribute rubric (Domain, Localization, Reasoning, Communication, Actionability) scored 1–5, an item-specific checklist of 5–10 verb-first criteria acting as ground truth, and an explicit preference ranking of all responses ⟨§2.1; §4⟩
- The paper introduces an aggregate "Solve Rate" (SR) metric: a task counts as solved when the mean rubric score is ≥ 3.0 and checklist fulfillment is ≥ 60%, which the authors describe as a generous passing grade for a supposedly strict examination ⟨§4⟩
- The authors report that the strongest model (Fable 5) solves only 56.9% of tasks, while blindly-judged expert-written reference answers reach a near-ceiling 92.4% Solve Rate — a gap the paper characterizes as placing frontier generative systems well below the professional standard of work they are already used for ⟨Abstract; Table 4; §5⟩
- The reported Solve Rates by model are: Human Expert 92.4%, Fable 5 56.9%, GPT-5.5 51.3%, Opus 4.8 34.1%, Gemini 3.1 Pro 26.9%, GLM-5.2 21.1%, Mistral Large 18.4% ⟨Table 4⟩
- On the preference ranking, the authors report expert-written reference answers were preferred over every model response in 74.24% of direct rankings (win rate), versus 49.5% for the best model (Fable 5) ⟨Table 4; §5⟩
- The paper reports that even the most capable frontier models only barely surpass a 50% Solve Rate on the easiest question subset, which it reads as evidence they remain far from the standard needed to assist European executive decision-making ⟨§5; Figure 1⟩
- The authors report that "Reasoning" was the weakest rubric attribute across the board while "Localization" and "Communication" had stronger floors, which they interpret as today's frontier LLMs still being measurably better at generating fanciful text than at true intelligent reasoning ⟨§5.1⟩
- For statistical rigor the paper reports paired t-tests between adjacently-ranked models yielding p-values from 1.26e-6 to 9.2e-23, and that experts were preferred over any LLM at p < 0.01 on the 33-question subset ⟨§5.1⟩
- Evaluation was highly time-intensive: responses averaged ~44,000 characters (~7,500 words) and grading the six responses per item across three instruments took roughly 5 hours, with more than 4,000 human-expert hours dedicated overall ⟨§4⟩
- For a 33-question subset, question authors wrote an ideal answer that was blind-evaluated as a seventh "model"; the paper reports the human answers preserved the overall model ranking and were preferred over all LLMs ⟨§4; Appendix A; Table 10⟩
- On automatic metrics, the authors report ROUGE-Lsum and BLEU correlate only weakly with the mean human rubric score at item level (BLEU Pearson r ≈ 0.27, ROUGE-Lsum r ≈ 0.37) and do not translate into the correct ranking, concluding such reference metrics are not useful for assessing frontier models on these tasks ⟨§5.4; Table 7⟩
- On LLM-as-judge, the paper reports a single AI judge (DeepSeek v4-Pro) correlated with human scores better than human evaluators did with each other, but argues this is an artifact: the judge over-estimates the best models and under-estimates the worst, producing "too crisp" evaluations that miss the diversity of human opinion ⟨§5.4; Tables 8–9; §6⟩
- Stated hedges/limitations: only 33 of 413 items had expert-written ideal answers; the evaluation is costly and hard to reproduce or extend to new models; a qualitative failure-mode analysis was left to future work; items assume factual, comprehensive data; and only one LLM judge was tested ⟨Limitations⟩

## Concepts & entities covered
Concepts: [[human-baseline]] · [[human-parity]] · [[expert-gold-standard]] · [[realistic-performance-expectations]]
Entities: [[euroexec-benchmark]]
