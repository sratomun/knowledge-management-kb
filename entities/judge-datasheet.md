---
title: "Judge Datasheet"
type: entity
subtype: technique
aliases: []
tags: [benchmarking]
concepts: ["[[llm-as-judge-bias]]"]
sources: ["[[llm-judge-dark-current]]"]
updated: 2026-08-10
---

# Judge Datasheet

## What it is
The Judge Datasheet is a metrological protocol that reports an LLM-as-a-judge as a measurement instrument rather than a scalar scorer, characterizing it across dark current, stable cross-sensitivity, positional false preference, target sensitivity, and prompt-induced criterion. It combines A0 true-vacuum tests, A1 controlled quality ladders, and criterion-shift probing so that downstream evaluation claims do not silently inherit unmeasured judge behavior.

## Key facts
- It is proposed as a structured disclosure whose unit of documentation is the evaluator itself, extending the "Datasheets for Datasets" and "Model Cards" tradition from datasets/models to judges ⟨[[llm-judge-dark-current]] §1; §2⟩.
- Its components are A0 true-vacuum tests (dark current, non-preference, schema validity), A1 quality-ladder tests (target sensitivity, detection threshold, SDT quantities), ∆0 controls (raw false preference vs stable cross-sensitivity vs positional false preference), a criterion probe, and validity gates ⟨[[llm-judge-dark-current]] Table 1; §3⟩.
- It measures dark current as false preference under true-vacuum inputs — empty, whitespace-only, or identical non-empty candidate pairs — i.e., preference manufactured when no evaluative signal is present ⟨[[llm-judge-dark-current]] §3.3, Eq. 1⟩.
- It makes ∆0 direction-stability decomposition a first-class measurement, separating raw same-quality false preference into stable cross-sensitivity, positional false preference, one-sided commit, other conflict, and no-preference (related by Eq. 7) after slot outputs are mapped back to canonical content identity ⟨[[llm-judge-dark-current]] §1; §3.3, Eqs. 2–7⟩.
- It measures target sensitivity on a constructively controlled prefix-chain checklist ladder of Pareto-dominant ∆Q pairs, reporting P_correct(∆Q) and a 75% detection threshold ∆*75 ⟨[[llm-judge-dark-current]] §3; Eqs. 8–10⟩.
- It treats criterion as the prompt-induced tie/preference operating point, and its criterion-shift probe supports the finding that "prompting moves the criterion, not the resolution" — a strict tie prompt can suppress false preference but absorbs marginal target signal into ties rather than adding resolution ⟨[[llm-judge-dark-current]] §3.3, Eq. 11; §5⟩.
- In the paper's three-judge case study it is used to assign descriptive profiles (Llama-3.1-8B "Presentation-conflicted", Qwen2.5-14B "Mixed stable-positional", Qwen2.5-32B "Clean Class A"), stated as descriptive within the controlled stimulus family, not universal reliability claims ⟨[[llm-judge-dark-current]] §4, Table 3⟩.
- It includes validity gates (parse success, schema validity, semantic validity, hidden-metadata checks) to prevent syntactic success from being treated as scientific validity ⟨[[llm-judge-dark-current]] Table 1⟩.

## Relations
- Realizes: [[llm-as-judge-bias]]
- Defined in: [[llm-judge-dark-current]]

## See also
[[llm-as-judge-bias]] · [[benchmark-validity]] · [[llm-judge-dark-current]]
