---
title: "ComplianceNLP: Knowledge-Graph-Augmented RAG for Multi-Framework Regulatory Gap Detection"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["ComplianceNLP paper"]
publisher: arXiv
url: https://arxiv.org/abs/2604.23585
published: 2026
effective_from: 2026-04
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# ComplianceNLP: Knowledge-Graph-Augmented RAG for Multi-Framework Regulatory Gap Detection

## Scope & purpose

ComplianceNLP, authored by researchers at The University of Hong Kong and Stellaris AI, is an
end-to-end system that automatically monitors regulatory changes, extracts structured
obligations, and identifies compliance gaps against institutional policies. It targets the
scale problem the authors describe for financial institutions — tracking over 60,000
regulatory events annually across fragmented jurisdictions, a volume said to overwhelm manual
compliance teams — and covers three frameworks (SEC, MiFID II, Basel III), which the paper
states represent roughly half of annual regulatory update volume ⟨abstract, §1⟩.

## Structure

The paper runs: introduction and problem framing (§1); related work in legal/regulatory NLP,
financial LMs, RAG, and efficient inference (§2); the ComplianceNLP system — RAG pipeline,
multi-task obligation extraction, and compliance gap analysis (§3); production optimization
via distillation and speculative decoding (§4); experiments and datasets (§5); results and
analysis including grounding validation (§6); deployment and five lessons learned (§7); and
conclusion (§8). Appendices cover GRC comparison, algorithm, datasets, and deployment detail.

## Key points

- The paper integrates three components: (1) a knowledge-graph-augmented RAG pipeline
  grounding generation in a Regulatory Knowledge Graph (RKG) of 12,847 provisions across SEC,
  MiFID II, and Basel III; (2) multi-task obligation extraction combining NER, deontic
  classification, and cross-reference resolution over a shared LEGAL-BERT encoder; and (3)
  compliance gap analysis mapping obligations to internal policies with severity-aware scoring
  ⟨abstract, §3⟩.
- Retrieval is hybrid dense+BM25 (weight α=0.7), with the top-k passages re-ranked by KG
  proximity (β=0.3, measuring graph distance between the query's source provision and
  retrieved passages' linked provisions) ⟨§3.1⟩.
- The RKG is built via three format-specific parsers (SEC EDGAR XML, EUR-Lex HTML, BIS PDF);
  it contains 12,847 provision nodes and 34,219 edges, updated nightly with 18-hour median
  incorporation latency; the paper reports 94.7% edge precision and 87.3% estimated recall
  ⟨§3.1, contributions⟩.
- Obligation extraction is a multi-task problem with three jointly trained heads over a shared
  LEGAL-BERT encoder: a CRF layer for regulatory NER across 23 entity types, sentence-level
  deontic modality classification into OBLIGATION / PERMISSION / PROHIBITION / RECOMMENDATION,
  and a span-pair classifier for cross-reference resolution ⟨§3.2⟩.
- Each extracted obligation is represented as ⟨entity, action, modality, condition,
  source_provision⟩; obligations and internal policy clauses are embedded and aligned, and
  clauses below threshold δ (0.6 evaluation / 0.45 recall-optimized deployment) are flagged
  and classified as COMPLIANT, PARTIAL GAP, or FULL GAP by a generator LLM ⟨§3.3⟩.
- For production latency, the authors distill a LLaMA-3-70B teacher into an 8B student
  (reverse-KL, MiniLLM) and add 3 Medusa speculative-decoding heads; they report a combined
  2.8× speedup (1,847→659 ms p50) ⟨§4, Table 1⟩.
- The paper reports an empirical finding that regulatory text's low entropy (H=2.31 bits vs.
  3.87 on general text) yields 91.3% Medusa draft-token acceptance vs. 82.7% for general-text
  heads, which the authors suggest may extend to other low-entropy domains ⟨abstract, §4, §7.1⟩.
- On the authors' benchmark, the paper reports ComplianceNLP reaching 87.7 gap-detection F1 at
  δ=0.6, which it states outperforms GPT-4o+RAG by +3.5 F1, with 94.2% grounding accuracy
  (r=0.83 vs. human) and 83.4 F1 under realistic end-to-end error propagation ⟨abstract, §6, Table 2⟩.
- The authors' ablations report that removing KG re-ranking causes the largest drop (−4.6 gap
  F1), which they present as confirming that structural regulatory knowledge is critical for
  cross-reference-heavy tasks; removing multi-task training reduces NER by 2.2 F1, and removing
  MiniCheck degrades grounding accuracy from 94.2% to 86.7% ⟨abstract, §6⟩.
- The paper reports grounding accuracy degrading with cross-reference complexity (97.1% at 0
  references down to 84.6% at 3+, and ~79% on nested conditional obligations), motivating a
  deployment policy of mandatory analyst review for findings whose source obligation involves
  ≥3 cross-references ⟨§6.1⟩.
- The authors report four months of parallel-run deployment at a financial institution
  processing 9,847 updates, achieving an estimated 96.0% production recall and 90.7% precision
  at δ=0.45, with a 3.1× sustained analyst efficiency gain ⟨abstract, §7, Table 4⟩.
- Five deployment lessons are reported: structural knowledge outperforms embeddings for
  cross-references; formulaic language enables efficient speculative decoding; analysts trust
  recall more than F1; GRC integration is harder than model development; and organizational
  adoption requires staged trust-building ⟨§7.1⟩.
- The paper frames the system as a decision-support tool that augments human professionals,
  with all high-severity findings requiring human review and full audit trails, and states it
  should not be the sole basis for compliance decisions ⟨Ethical Considerations⟩.

## Concepts & entities covered
Concepts: [[compliance-checking]] · [[regulatory-gap-detection]] · [[graphrag]] · [[retrieval-augmented-generation]]
Entities: [[compliancenlp]]
