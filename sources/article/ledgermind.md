---
title: "LEDGERMIND: A Structured Evidence Runtime for Auditable Multimodal Agent Trajectories"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["LEDGERMIND"]
publisher: "Enjun Du, Hange Zhou, Chenxu Du, Siyi Liu, Zirong Chen, Ziyu Zheng, Yongqi Zhang (HKUST-GZ)"
url: https://arxiv.org/abs/2607.28374
version: "arXiv:2607.28374v1 [cs.LG]"
published: 2026
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-11
---

# LEDGERMIND: A Structured Evidence Runtime for Auditable Multimodal Agent Trajectories

## Scope & purpose
LedgerMind (Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger) is a training-free runtime that treats a multimodal agent trajectory as a provenance-constrained state machine. Its motivation is that final-answer accuracy cannot tell whether a correct answer was reached through grounded evidence, language priors, or accidental error cancellation, so the framework evaluates the trajectory — not just the final answer. Tool outputs are normalized into a Structured Evidence Ledger that serves as the trajectory state; downstream claims may cite only active ledger entries, grounding is checked at the entity and numeric level, and repair is realized as typed state transitions that cannot introduce content without tool-produced provenance.

## Structure
The paper motivates trajectory faithfulness over aggregate accuracy, defines the Structured Evidence Ledger and its invariants, specifies the grounding protocol (support coverage, ECC, NCC), the Adaptive Dual-Path Dispatcher, and event-triggered typed repair with a non-amplification guarantee, then reports results and a component ablation across multiple multimodal benchmarks and backbone MLLMs.

## Key points
- LedgerMind is a training-free framework that treats a multimodal agent trajectory as a provenance-constrained state machine, normalizing each tool output into a Structured Evidence Ledger entry carrying source, epistemic type, confidence, lifecycle status, and dependencies, so provenance is a structural constraint rather than a prompting preference ⟨arXiv:2607.28374, Abstract / §3.1⟩.
- The motivation is explicitly evaluative: aggregate final-answer accuracy "cannot tell whether a correct answer was obtained through grounded evidence, language priors, or accidental error cancellation," so intermediate reasoning claims should be auditable against the evidence that supports them ⟨arXiv:2607.28374, Abstract / §1⟩.
- Downstream reasoning and decision claims may cite only active ledger entries (citation validity), and grounding is enforced beyond structural coverage by an Entity Consistency Check (ECC) and a type-aware Numeric Coherence Check (NCC), so conclusion-level entities and numeric values must be licensed by the cited evidence pool ⟨arXiv:2607.28374, §3.1 / §3.2⟩.
- The design targets four recurring failure patterns that final-answer accuracy obscures: unsupported intermediate reasoning (F1), citation-backed entity hallucination or "Phantom Grounding" (F2), over-reasoning on simple queries (F3), and repair-time amplification (F4) ⟨arXiv:2607.28374, §1⟩.
- An Adaptive Dual-Path Dispatcher matches reasoning depth to question complexity, routing simple or knowledge-oriented queries to a direct path and complex queries to a full pipeline, both writing through the same ledger interface ⟨arXiv:2607.28374, §3.2⟩.
- Citing that LLMs largely cannot self-correct without external feedback and that free-form repair can itself inject unsupported claims, LedgerMind restricts repair to seven typed operators in three layers — evidence (DROP, REFRESH), action (RETRY, SWITCH, ACQUIRE), and trajectory (STOPANDANSWER, ABSTAIN) — yielding a Provenance Non-Amplification guarantee (Proposition 1) that repair cannot add ledger entries without tool-produced provenance ⟨arXiv:2607.28374, §2.2 / §3.2 / §3.3⟩.
- The authors report LedgerMind improves both answer accuracy and trajectory-level faithfulness across benchmarks: on VTC-Bench, Gemini-3-Flash reaches 58.9% (reported as a new state of the art) and the framework lifts GPT-4o by +23.3 points, while on the Hard-200 stress set it improves every one of six backbones by +11.2 to +19.7 points overall ⟨arXiv:2607.28374, §4.2⟩.
- A component ablation on MMMU-Pro (Gemini-3-Flash) shows removing the Structured Evidence Ledger is the most damaging (−15.39 overall), replacing typed repair with free-form self-reflection second (−8.49), and disabling ECC/NCC hurts the Hard split most, while the dispatcher's value lies in avoiding unnecessary depth on simple queries rather than adding it on hard ones ⟨arXiv:2607.28374, Table 3⟩.

## Concepts & entities covered
Concepts: [[provenance-constrained-extraction]] · [[extraction-self-verification]] · [[agentic-extraction]]
Entities: [[ledgermind-system]]
