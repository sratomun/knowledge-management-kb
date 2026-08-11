---
title: "$OneMillion-Bench: How Far are Language Agents from Human Experts?"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["OneMillion-Bench"]
publisher: "Qianyu Yang, Yang Liu, Jiaqi Li et al. (Humanlaya, BIGAI, xbench, M-A-P)"
url: https://arxiv.org/abs/2603.07980
version: "arXiv:2603.07980v1 [cs.LG]"
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[human-parity]]", "[[realistic-performance-expectations]]", "[[llm-failure-modes]]"]
entities: ["[[onemillion-bench]]"]
updated: 2026-08-10
---

# $OneMillion-Bench: How Far are Language Agents from Human Experts?

## Scope & purpose
A benchmark paper framed around the question in its title — "how far are language agents from human experts?" — that evaluates LLM agents on long-horizon, economically-consequential professional tasks rather than exam-style questions ⟨Abstract; §1⟩. The authors introduce $OneMillion-Bench ($1M-Bench): 400 expert-curated tasks across Law, Finance, Industry, Healthcare, and Natural Science, each assigned a real-world monetary value from senior-professional completion time and prevailing hourly wage, with the total exceeding $1 million ⟨Abstract; §1; §2.1⟩. Correctness is scored by a rubric-based protocol (Expert Score and Pass Rate) covering factual accuracy, logical coherence, practical feasibility, and professional compliance, where the authors emphasize that the reasoning process matters as much as the final answer ⟨Abstract; §2.2⟩. The KB records the paper's comparative and value-of-work claims descriptively.

## Key points
- The benchmark contains 400 open-ended tasks across five high-stakes domains (Finance, Law, Healthcare, Natural Science, Industry, 80 each), further partitioned into 37 sub-domains and 86 third-level categories, curated over more than 2,000 expert hours ⟨Abstract; §1; §3.2⟩
- Each task carries a real monetary value computed as senior-expert completion time × market hourly wage; the reported totals are ~$1,008,370 (Global set) and ~¥921,832 (CN set), giving the benchmark its name ⟨§2.1; Table 1⟩
- The dataset is bilingual and culturally localized — 200 English and 200 Chinese instances — with the Chinese set purpose-built around Mainland-China regulations and standards rather than translated ⟨§3.2⟩
- Tasks are curated through a three-stage multi-expert pipeline (creation with adversarial validation against frontier agents, peer review, and resolution), retaining a task only if several frontier agents fail to reach the experts' passing threshold, plus bidirectional truncation to remove trivially-easy and effectively-impossible items ⟨§3.1⟩
- Scoring uses an Expert Score (weighted rubric fulfillment clipped to [0,1]) and a Pass Rate — the fraction of tasks with Expert Score ≥ 0.7, described as meeting a minimum professional standard ⟨§2.2⟩
- Rubrics include a negative-scoring mechanism with asymmetric weights from −20 to +10, penalizing norm violations, unsafe/harmful output, hallucination, and instruction-following lapses to mirror real professional stakes ⟨§3.2⟩
- The evaluation covers 35 systems in three groups: 17 vanilla models, the same 17 equipped with web search, and 3 dedicated deep-research agents ⟨§4.1⟩
- The authors report a clear leader: CLAUDE-OPUS-4.6 achieves the best overall performance among vanilla models and remains top with search, reaching 55.0 → 63.0 Expert Score and 36.5% → 43.5% Pass Rate on the Global set once web search is enabled ⟨§4.2; Table 3⟩
- The paper reports that many models reach a moderate Expert Score (~45–50%) while their Pass Rates stay much lower (often below ~25%), which it reads as broad-but-shallow rubric satisfaction rather than clearing the competence threshold — i.e. even the best agents leave most economically-valuable tasks below the professional bar ⟨§4.2⟩
- The authors report web search is "not always beneficial": it amplifies strong models but causes regressions for weaker ones (e.g. HUNYUAN-2.0 drops 34.7 → 30.2 Expert Score and 8.5% → 3.0% Pass Rate on Global), acting as an efficacy amplifier rather than a default advantage ⟨§4.2; §4.3⟩
- The paper reports that specialized deep-research agents are competitive at mid-tier but do not dominate the strongest search-enabled generalists on Expert Score, Pass Rate, or Economic Value ⟨§4.2; §4.3⟩
- On LLM-as-judge robustness, the authors report agent rankings stay stable across six judges though absolute scores shift with judge strictness (GPT-5.2-High strictest, GLM-5 most lenient), motivating multi-judge evaluation and reporting judge identity ⟨§4.5⟩
- The paper catalogs failure modes from case studies: web search as a double-edged sword (outdated/incompatible-guideline retrieval), arithmetic and extraction errors in finance, imprecise mapping of facts to legal provisions, and shallow multi-step reasoning that "points in the right direction but falls short on actionable, in-depth details" ⟨§5.4⟩
- On test-time scaling, the authors report pass@k rises logarithmically (Claude-Opus-4.6 plateauing near 30% on the Finance subset) while pass^k decays toward zero, indicating gains in raw capability but degrading output reliability under high uncertainty ⟨§4.7⟩
- Stated hedges: current domains are representative but non-exhaustive; rubrics are less objective than a single-expression checker and rely on model-judge capability; and full manual scoring is hard to scale ⟨§5.2; §5.3⟩

## Concepts & entities covered
Concepts: [[human-parity]] · [[realistic-performance-expectations]] · [[llm-failure-modes]]
Entities: [[onemillion-bench]]
