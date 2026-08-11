---
title: "Eligibility determination"
type: concept
subtype: use-case-profile
aliases: []
tags: [knowledge-processing]
related: ["[[rules-as-code]]", "[[neuro-symbolic-rule-evaluation]]"]
updated: 2026-08-10
---

# Eligibility determination

## What it is
Eligibility determination is the use case of deciding whether an applicant or situation qualifies for a benefit, program, or status under codified rules — answering "does this person meet the conditions, and why?" The output is not just a yes/no but a justification traceable to the governing rules. Which processing pattern fits depends on the nature of the source documents: eligibility law is high-normativity, deeply conditional (nested "unless/except" structures), exception-laden, provenance-sensitive (each condition maps to a specific provision), and slow-changing but consequential. Those document-nature attributes — structure, normativity, volatility, sensitivity, provenance, lifecycle — condition how the pattern is realized.

## How sources treat it
- **[[neurosymbolic-public-sector-eligibility]]** _(article · informational)_ — treats determination as an explanation-level accountability problem: an LLM encodes statutory eligibility rules into a formal ontology and an SMT solver checks whether a benefits explanation is legally coherent (SAT) or fails to justify the determination (UNSAT), demonstrated on California's CalFresh ⟨arXiv:2512.12109, Abstract, §3.2⟩
- **[[neurosymbolic-public-sector-eligibility]]** _(article · informational)_ — reports that formal verification reveals violations of statutory requirements even when explanations appear reasonable or complete to human readers ⟨arXiv:2512.12109, Abstract, §4.1⟩
- **[[exception-chain-collapse]]** _(article · informational)_ — documents "exception chain collapse," a reported failure class in which frontier LLMs mis-evaluate nested conditional eligibility rules ("A required UNLESS B, UNLESS C overrides B"), scoring 100% on shallow scenarios but degrading sharply on three-level chains ⟨arXiv:2607.23386, §4.2, §6.5 Finding 1⟩
- **[[openfisca]]** _(provider-doc · vendor)_ — models eligibility as rules-as-code: country packages expose per-jurisdiction rules whose formulas and time-tracked parameters let a web API compute eligibility and amounts for a described situation ⟨openfisca.org/en — Model concepts⟩

## Where sources differ
The sources converge on a neuro-symbolic separation of concerns but frame the risk and the artifact differently. [[neurosymbolic-public-sector-eligibility]] focuses on *post-hoc verification* of a justification against encoded law, stressing that an UNSAT result flags the explanation, not necessarily the decision. [[exception-chain-collapse]] focuses on the *failure mode of direct LLM evaluation* and reports (as the paper's findings) systematic false negatives and "silent drift" of model behaviour over time, motivating deterministic execution. [[openfisca]] presents an *operational engine* for encoding legislation as computable formulas, oriented to governments and simulation at population scale, and makes no LLM-reliability claim. Each source's comparative and reliability claims are attributed to its authors on its own page; the KB does not adjudicate among them.

## See also
[[rules-as-code]] · [[neuro-symbolic-rule-evaluation]]
