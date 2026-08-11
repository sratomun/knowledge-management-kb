---
title: "What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Italian legal Turing test"]
publisher: arXiv
url: https://arxiv.org/abs/2608.06166
published: 2026
effective_from: 2026-08
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[human-parity]]", "[[llm-failure-modes]]", "[[expert-gold-standard]]"]
updated: 2026-08-10
---

# What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries

## Scope & purpose

This article, by researchers affiliated with the Turin Bar, the University of Naples Suor
Orsola Benincasa, and the University of Bologna (CIRSFID-Alma AI), reports a blind "Turing
Test" experiment assessing out-of-the-box leading LLMs on three Italian legal professional
exams — the Bar, Judges, and Notary exams. Leading LLMs were asked to generate full written
exam papers, which were made indistinguishable from human submissions and anonymously
evaluated by expert examiners using the same criteria applied in real examinations. The
authors stress the results are qualitative evidence limited to out-of-the-box systems
⟨abstract, §I⟩.

## Structure

The paper runs: introduction on the rule-recall vs. rule-application gap in legal AI (§I);
background and related work on legal-exam benchmarking (§II); an overview of the three Italian
professional exams (§III); methodology and experimental setting — model selection, minimal
uniform prompts, anonymization (§IV); evaluation criteria and scoring grids per exam (§V);
results and discussion per exam (§VI); a comparison across legal tasks (§VII); a dedicated
analysis of notary-exam failure patterns (§VIII); speculations on the underlying causes (§IX);
limitations (§X); and conclusion with future work (§XI), followed by the scoring-grid tables
⟨§I–XI⟩.

## Key points

- The experiment evaluated four models the authors describe as state of the art at the time
  (Claude 4 Opus, GPT-5, DeepSeek R1, and Gemini 2.5 Pro), each generating full exam papers
  under minimal uniform prompts, with case-law references removed so LLM outputs were visually
  indistinguishable from the human papers; three examiners who had served on national board
  committees scored the anonymized papers blind ⟨§IV, §V⟩.
- The human gold standard was the highest-scoring human essay obtained from the official final
  rankings of each real national exam (Bar Dec 2024, Judicial Jan 2024, Notary May 2023),
  which the authors adopt as a top-tier human benchmark ⟨§II, §IV⟩.
- The authors report that some LLMs match or exceed top human performance in adversarial legal
  argumentation (Bar) and doctrinal analysis (Judicial): on the Bar exam Gemini 2.5 Pro scored
  79 and ChatGPT-5 scored 65 versus the human candidate's 62 (Gemini said to exceed the human
  across all macro-criteria), and on the Judicial exam Gemini scored 21/24 versus the human's
  18/24 ⟨abstract, §VI.1, §VI.2⟩.
- The authors report that all models failed the notary exam, which they characterize as
  requiring goal-directed legal planning under strict formal and substantive constraints:
  across both the inter vivos and mortis causa assignments every LLM fell significantly below
  the human benchmark, and none produced a notarial deed that simultaneously satisfied the
  mandatory formal requirements and an adequate level of substantive legal quality ⟨abstract,
  §VI.3, §VII⟩.
- From the notary results the authors derive a purpose-built taxonomy of recurring "legal
  failures" in five categories: (1) legal-source failure (inapplicable, incorrect, or
  fictitious rules); (2) reasoning failure (internal inconsistency); (3) pertinence failure
  (eluding a central legal question); (4) lexical failure (imprecise technical terminology);
  and (5) formal failure (structural or drafting defects of the deed) ⟨§VIII⟩.
- The authors report a "gullibility" pattern: in the inter vivos assignment all models,
  including those that correctly identified the legal sources, incorrectly stated that a
  sign-language interpreter was not needed for a deaf-mute purchaser — an omission that under
  notarial law carries nullity — which they read as a risk that LLMs may be deceived or
  manipulated in legal tasks ⟨§IX⟩.
- The authors argue performance is strongly task-dependent and highly model-dependent: they
  say frontier LLMs can approximate or exceed the human benchmark on knowledge-organization
  tasks but not on long-horizon legal planning, and caution that a few high-performing systems
  do not make LLMs "as a class" uniformly capable ⟨§VII⟩.
- As speculation on causes, the authors suggest performance may track the accessibility of
  relevant knowledge (notarial deeds are largely not publicly available, unlike Bar/Judicial
  materials) and that current LLMs excel at selecting and organizing knowledge but are less
  proficient at goal-driven problem solving ⟨§IX⟩.
- The authors state explicit hedges on scope: models were used out-of-the-box only, with no
  legal fine-tuning or dedicated RAG; each exam used a single simple prompt; only three
  examiners were used (though with relatively strong agreement); LLMs had internet access
  whereas human candidates did not; the models reflect a September 2025 snapshot; and passing
  a professional exam does not entail the ability to exercise the profession ⟨§X, §XI⟩.

## Concepts & entities covered
Concepts: [[human-parity]] · [[llm-failure-modes]] · [[expert-gold-standard]]
Entities: —
