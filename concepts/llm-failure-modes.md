---
title: "LLM failure modes"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[human-parity]]", "[[neuro-symbolic-rule-evaluation]]"]
updated: 2026-08-10
---

# LLM failure modes

## What it is
LLM failure modes are the characteristic, recurring ways in which LLM and agent systems produce wrong outputs on professional tasks — distinct from random error in that they form identifiable patterns, sometimes systematic enough to reproduce. Benchmark and audit papers catalog these modes (retrieval mishandling, arithmetic slips, procedural-ordering errors, brittle multi-step or nested-rule reasoning) both to explain aggregate scores and to warn where deployment is riskiest. The KB records each documented failure pattern as the reporting source's finding.

## How sources treat it
- **[[occubench]]** _(article · informational)_ — documents skipped safety-critical verification, procedural-ordering errors, and missing proactive constraint monitoring, and reports robustness falling from 67.5% (clean) to 53.4% under implicit faults (truncated data, missing fields), which it finds counter-intuitively harder than explicit faults because they lack overt error signals ⟨§6.2; §7.3–7.5⟩
- **[[onemillion-bench]]** _(article · informational)_ — catalogs web search as a double-edged sword (outdated or incompatible-guideline retrieval), arithmetic and extraction errors in finance, imprecise mapping of facts to legal provisions, and shallow multi-step reasoning that "points in the right direction but falls short on actionable, in-depth details" ⟨§5.4⟩
- **[[italian-legal-turing]]** _(article · informational)_ — derives a purpose-built taxonomy of five legal failures (legal-source, reasoning, pertinence, lexical, and formal), and reports a "gullibility" pattern where all models wrongly stated a sign-language interpreter was unneeded for a deaf-mute purchaser — an omission carrying nullity under notarial law ⟨§VIII; §IX⟩
- **[[exception-chain-collapse]]** _(article · informational)_ — defines exemption anchoring and exception chain collapse on nested "A unless B unless C" rules, reporting frontier models scoring 100% on shallow multi-route scenarios but degrading sharply on three-level chains, with all observed baseline failures being false negatives ⟨§4.3; §6.5⟩

## Where sources differ
The sources capture failure at different granularities. [[occubench]] and [[onemillion-bench]] report broad failure categories drawn from case studies across many occupations; [[italian-legal-turing]] abstracts a domain-specific taxonomy from notary-exam errors; [[exception-chain-collapse]] isolates a single reproducible structural failure class and tracks its "silent drift" across model snapshots. They also differ on whether the failure is stochastic or systematic at a given snapshot. The KB records these as complementary catalogs, not a unified failure theory.

## See also
[[human-parity]]
[[neuro-symbolic-rule-evaluation]]
[[realistic-performance-expectations]]
