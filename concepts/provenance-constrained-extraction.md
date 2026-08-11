---
title: "Provenance-Constrained Extraction"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[evidence-grounded-generation]]", "[[extraction-self-verification]]"]
updated: 2026-08-11
---

# Provenance-Constrained Extraction

## What it is
Provenance-constrained extraction makes evidence a structural rule rather than a prompting preference: every downstream claim must cite a tool-produced source recorded in an auditable store, and the system cannot introduce content that lacks such provenance. The motivation is that a correct final answer does not reveal whether it was reached through grounded evidence, language priors, or accidental error cancellation, so the whole trajectory — not just the output — is evaluated and constrained against its supporting evidence.

## How sources treat it
- **[[ledgermind]]** _(article · informational)_ — A training-free runtime treating a multimodal agent trajectory as a provenance-constrained state machine, normalizing each tool output into a Structured Evidence Ledger entry carrying source, epistemic type, confidence, lifecycle status, and dependencies, so provenance is a structural constraint rather than a prompting preference ⟨Abstract / §3.1⟩
- **[[ledgermind]]** _(article · informational)_ — Downstream claims may cite only active ledger entries (citation validity), with grounding enforced beyond structural coverage by an Entity Consistency Check (ECC) and type-aware Numeric Coherence Check (NCC); targets four failure patterns including "Phantom Grounding" — citation-backed entity hallucination ⟨§3.1 / §3.2; §1⟩
- **[[ledgermind]]** _(article · informational)_ — Restricts repair to seven typed operators in three layers (evidence: DROP/REFRESH; action: RETRY/SWITCH/ACQUIRE; trajectory: STOPANDANSWER/ABSTAIN), yielding a Provenance Non-Amplification guarantee (Proposition 1) that repair cannot add ledger entries without tool-produced provenance ⟨§3.2 / §3.3⟩
- **[[ledgermind]]** _(article · informational)_ — Reports improving both answer accuracy and trajectory faithfulness: on VTC-Bench, Gemini-3-Flash reaches 58.9% (reported as a new SOTA) and the framework lifts GPT-4o by +23.3 points, while on the Hard-200 stress set it improves every one of six backbones by +11.2 to +19.7 points ⟨§4.2⟩
- **[[ledgermind]]** _(article · informational)_ — A component ablation on MMMU-Pro (Gemini-3-Flash) reports removing the Structured Evidence Ledger is most damaging (−15.39 overall) and replacing typed repair with free-form self-reflection second (−8.49), with ECC/NCC mattering most on the Hard split ⟨Table 3⟩

## Where sources differ
This concept is grounded in a single source, so there is no cross-source divergence to report. Internally, [[ledgermind]] frames its position against final-answer-accuracy evaluation (arguing it cannot distinguish grounded from ungrounded correct answers) and against free-form self-correction (which it says can inject unsupported claims), and reports its own ablation ranking the ledger and typed repair as the most load-bearing components. It relates to [[evidence-grounded-generation]] and [[extraction-self-verification]] by making grounding and verification enforceable state transitions rather than post-hoc checks.

## See also
[[evidence-grounded-generation]] · [[extraction-self-verification]] · [[agentic-extraction]] · [[extraction-verification]] · [[provenance]]
