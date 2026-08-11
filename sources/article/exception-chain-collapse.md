---
title: "Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Exception Chain Collapse"]
publisher: "Paul Simpson; John Kozak; Lisa Doake (Aethis)"
url: https://arxiv.org/abs/2607.23386
version: "arXiv:2607.23386v1"
published: 2026-07
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [knowledge-processing]
concepts: ["[[neuro-symbolic-rule-evaluation]]", "[[eligibility-determination]]"]
entities: []
updated: 2026-08-10
---

# Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation

> This paper documents a CAUTION — a reproducible failure class in frontier LLMs used for eligibility evaluation. All failure, drift, and comparative claims below are reported as the paper's findings, not as KB conclusions.

## Scope & purpose
A July 2026 arXiv paper by Paul Simpson, John Kozak, and Lisa Doake (Aethis) that documents **exception chain collapse** — a failure class the authors observe in frontier LLMs during eligibility evaluation under nested conditional rules of the form "A is required UNLESS B applies, UNLESS C overrides B" ⟨arXiv:2607.23386, Abstract, §4.2⟩. The paper's second thrust is architectural: it presents the Aethis Eligibility Module, a neuro-symbolic design that uses LLMs to author rules from authoritative sources and an SMT-based deterministic layer to execute them ⟨arXiv:2607.23386, Abstract, §5⟩.

## Structure
Organised as: §1 Introduction; §2 Contributions; §3 Related Work; §4 the failure problem (high-stakes decisions, two failure patterns, why false negatives matter); §5 the neuro-symbolic architecture (rule authoring, the Eligibility Module, the L1/L2/L3 guarantee split); §6 the 225-scenario benchmark across four domains plus LegalBench external validation; §7–§10 rule-synthesis challenges, generalisation, compliance, and limitations ⟨arXiv:2607.23386, Contents, §1–§10⟩.

## Key points
- The authors define two systematic failure patterns on nested exception-chain tasks: **exemption anchoring** (failing to evaluate alternative routes independently when the primary route fails) and **exception chain collapse** (failing to correctly nest multi-level UNLESS logic) ⟨arXiv:2607.23386, §4.2⟩
- The paper reports the failure is specific to nested (three-level) exception structure: frontier models score 100% on 43 shallow multi-route English-language scenarios but degrade sharply on three-level chains, insensitive to temperature and sample count ⟨arXiv:2607.23386, §1, §6.3, §6.5 Finding 1⟩
- In the March 2026 baseline the authors report Claude Opus 4.6 at 61/68 (89.7%) on the spacecraft section and 0 correct answers across 70 trials on 7 then-failing scenarios (Clopper–Pearson 95% one-sided upper bound 4.19%), which they characterise as systematic rather than stochastic at that snapshot ⟨arXiv:2607.23386, §1, §6.7 R1⟩
- The authors report all observed baseline failures were false negatives — eligible applicants incorrectly rejected — and argue false negatives matter because exemptions exist precisely for the edge-case applicants most likely to be wrongly denied ⟨arXiv:2607.23386, §4.3, §6.5 Finding 2⟩
- The authors identify the veteran exemption (an override independent of age) as the universal failure point, with Claude Opus 4.6 and Sonnet 4.6 marking an age-59 1000-hour veteran ineligible on every run (0/3) while GPT-5.4 answers correctly ⟨arXiv:2607.23386, §4.2, §6.5 Finding 3⟩
- The paper's central caution is "silent drift": between March and April 2026 several reported failure cells closed under the same model alias with no version bump — GPT-5.4 on construction insurance moved 96.6%→100% and Claude Opus 4.6 on spacecraft moved 89.7%→98.5% — which the authors call a "moving compliance boundary" ⟨arXiv:2607.23386, Abstract, §6.5 Finding 4, Finding 6⟩
- The authors report that enhanced prompting does not fix the pattern but trades error types: an exception-aware prompt reduced false negatives from 7 to 4 while introducing 20 false positives, dropping net spacecraft accuracy from 89.7% to 64.7% ⟨arXiv:2607.23386, §6.7 R2⟩
- The proposed Aethis Eligibility Module separates concerns: Phase 1 uses an LLM to read authoritative sources and emit rules as structured code with provenance citations; Phase 2 compiles that code to formal SMT constraints and evaluates it deterministically (<1ms, near-zero marginal cost), never executing the DSL directly ⟨arXiv:2607.23386, §5.1–§5.3⟩
- The architectural claim is that this relocates uncertainty from the inference boundary (silent, continuous) to the specification boundary (deliberate, audited); the engine guarantees only Level 3 (execution) — Level 1 (source retrieval) and Level 2 (rule formalisation) remain fallible and are addressed by SME-defined test suites ⟨arXiv:2607.23386, §5.5⟩
- The authors report the deterministic engine achieves complete consistency with the benchmark's formal rule fixtures across all 225 scenarios by construction, and that exemption-anchoring and exception-chain-collapse errors are excluded by the disjunctive/material-implication compilation semantics ⟨arXiv:2607.23386, §5.4, §6.3⟩
- External validation on nine LegalBench tasks (949 held-out cases) reports the engine as significantly more accurate than each of three frontier models (combined McNemar's p ≤ 0.003), with margins up to +41 percentage points against the Anthropic models on multi-prong rule-application tasks (GPT-5.4's larger margins attributed to a prompt-format sensitivity) ⟨arXiv:2607.23386, Abstract, §6.10⟩
- On a v3.8 20-scenario adversarial construction-insurance extension the engine scores 20/20; GPT-5.4 at low reasoning effort also scores 20/20, while GPT-5.4 default and Claude Sonnet 4.6 score 19/20 and Claude Opus 4.7 scores 18/20 — the authors read the shared E4 "carve-back gap" failure as a structural compositional-evaluation failure mode ⟨arXiv:2607.23386, §6.4.1, Table 8c⟩
- The authors explicitly withdraw an earlier finding (v3.6/v3.7 "GPT-5.4 at low reasoning effort 7/11") in v3.8 after an instrumented replication returned 11/11 and no committed script reproduced the original figure, attributing it to a harness artefact ⟨arXiv:2607.23386, §6.5 Finding 5, §6.7 R5⟩
- The authors frame the drift property as structurally incompatible with benchmark-time accuracy certification under frameworks like the EU AI Act, contrasting it with a rule bundle compiled once and evaluated deterministically thereafter ⟨arXiv:2607.23386, §6.5 Finding 6⟩

## Concepts & entities covered
Concepts: [[neuro-symbolic-rule-evaluation]] · [[eligibility-determination]]
Entities: —
