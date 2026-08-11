---
title: "SCAIR: Schema-Conditioned Agentic Iterative Reasoning for Enterprise Knowledge Graphs"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["SCAIR"]
publisher: "Chaturvedi, Zhu, Zhou, Zhou, He, Staab, Du, Tang, Kharlamov (Stuttgart / Bosch Center for AI)"
url: https://arxiv.org/abs/2607.22571
version: "arXiv:2607.22571v1 [cs.AI]"
published: 2026
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-11
---

# SCAIR: Schema-Conditioned Agentic Iterative Reasoning for Enterprise Knowledge Graphs

## Scope & purpose
SCAIR (Schema-Conditioned Agentic Iterative Reasoning) is a training-free KG-RAG framework for question answering over enterprise knowledge graphs. Its central, neutral claim is that generic agentic designs that perform well on public benchmarks often fail to generalize to real enterprise KGs, which are dense, schema-driven, and operationally constrained; reliable enterprise graph reasoning requires encoding the domain's structural and operational constraints into the agent design. The method injects schema-conditioned structural priors and enforces schema-aware traversal during multi-hop reasoning, evaluated on a benchmark built from a real-world manufacturing Configuration Management Database (CMDB).

## Structure
The paper reviews KGQA and agentic KG-RAG paradigms, introduces an enterprise-oriented CMDB benchmark and the failure modes of existing paradigms on it, specifies SCAIR's three design principles, reports overall and per-query-type results with an ablation and inference-cost analysis, and draws deployment principles.

## Key points
- SCAIR is a training-free hybrid framework that unifies structured planning with controlled iterative reasoning by injecting schema-conditioned structural priors, enforcing schema-aware traversal, and controlling topic-entity propagation to balance exploration and exploitation ⟨arXiv:2607.22571, Abstract / §4⟩.
- The central claim is neutral and cautionary: existing agentic KG-RAG methods that do well on public benchmarks "fail to generalize" to enterprise KGs, and "reliable enterprise graph reasoning cannot rely on generic agentic designs" but must explicitly incorporate the domain's structural and operational constraints ⟨arXiv:2607.22571, Abstract / §1⟩.
- The enterprise benchmark is derived from a real manufacturing CMDB: CMDB-KG contains 116,369 triples, and template-based generation over the schema produces 9 representative query types totaling 19,080 questions (including 7,080 compositional queries excluding single-hop) ⟨arXiv:2607.22571, §3.2⟩.
- The authors identify systematic failure modes of existing paradigms on this benchmark: ReAct-style exploration suffers uncontrolled search expansion through high-degree attribute nodes and semantic drift in dense subgraphs, while plan-and-execute methods depend on distribution-specific training and overfit to seen query templates ⟨arXiv:2607.22571, §3.3⟩.
- The authors report SCAIR outperforms all evaluated baselines (Accuracy 35.14, Hits@Any 47.56, F1 31.72) versus the strongest baseline G-Retriever (25.27 Accuracy, 24.28 F1), with training-free ToG and PoG consistently underperforming ⟨arXiv:2607.22571, Table 1⟩.
- SCAIR requires more LLM calls (42.36) and tokens (22.5k input / 5.9k output) than ToG (13.95) and PoG (5.60), reflecting deeper average traversal (depth 2.54); the authors describe this cost as "functional" and amenable to prompt caching, suiting workloads where answer correctness is prioritized over single-query latency ⟨arXiv:2607.22571, Table 2⟩.
- The authors draw three deployment principles: structural validity must gate semantic relevance (prune the search space by schema before semantic scoring); traversal control is the primary bottleneck, an architectural rather than parametric failure (a stronger backbone does not prevent search explosion); and inference-time adaptation outperforms retraining for frequently evolving enterprise schemas ⟨arXiv:2607.22571, §6.1⟩.
- An ablation shows that removing schema-aware relation filtering and entity-centric constraints degrades performance consistently across query categories, indicating explicit structural constraints are central to robustness ⟨arXiv:2607.22571, §5.2 / Figure 4⟩.

## Concepts & entities covered
Concepts: [[agentic-extraction]] · [[schema-guided-extraction]]
Entities: [[scair-system]]
