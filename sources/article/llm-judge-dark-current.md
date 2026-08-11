---
title: "LLM Judges Have Dark Current: A Psychometric Datasheet for LLM-as-a-Judge Evaluation"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["LLM Judges Have Dark Current"]
publisher: "Usami, Hara, Tsuboi & Matsuda (Chubu University; Mitsubishi Heavy Industries)"
url: https://arxiv.org/abs/2606.15610
version: "arXiv:2606.15610v1 [cs.CL]"
published: 2026
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[llm-as-judge-bias]]", "[[benchmark-validity]]"]
entities: ["[[judge-datasheet]]"]
updated: 2026-08-10
---

# LLM Judges Have Dark Current: A Psychometric Datasheet for LLM-as-a-Judge Evaluation

## Scope & purpose
A metrology paper that argues an LLM-as-a-judge should be reported not as a scalar accuracy, win-rate, or agreement device but as a measurement instrument ⟨Abstract; §1⟩. It introduces a "Judge Datasheet" protocol that characterizes a judge across five axes — dark current under true-vacuum inputs, stable cross-sensitivity to same-quality surface variation, positional false preference, target sensitivity on a controlled quality ladder, and the criterion/operating point induced by tie instructions — and demonstrates it on three open-weight judges ⟨Abstract; §3; §4⟩. The contribution is explicitly narrow: it measures the measuring device before downstream claims are made, and does not confirm the motivating downstream ("orientation") mechanism ⟨Abstract; §1; Table 5⟩.

## Structure
- §1 Introduction — judges as measurement instruments; definitions of dark current, positional false preference, stable cross-sensitivity, target sensitivity, criterion; five contributions
- §2 Related work — IRT diagnosis of judges, evaluation infrastructure (HELM, BIG-Bench, MT-Bench/Chatbot Arena, AlpacaEval), signal-detection framing, judge biases, datasheets/model cards
- §3 Judge Datasheet protocol — notation, metric definitions (Eqs. 1–12), measurement algorithm, A0 vacuum / A1 ladder / ∆0 controls / criterion probe
- §4 Results — three-judge case study (Llama-3.1-8B, Qwen2.5-14B, Qwen2.5-32B) and the direction-stability decomposition
- §5 Criterion shift — strict-tie intervention on Qwen32B
- §6 Discussion; §7 Limitations; §8 Conclusion; Appendix A (protocol, glossary, full CI tables)

## Key points
- The paper's central claim is that LLM judges require multi-axis measurement before being used as evidence-bearing instruments; it deliberately does not claim a universal judge, a size-family trend, or any human-ground-truth result ⟨§1⟩
- Dark current is defined as false preference under true-vacuum inputs (empty answers, whitespace, or identical non-empty answers) — the non-abstaining false-preference rate when no evaluative signal is present ⟨§1; §3.3, Eq. 1⟩
- Positional false preference is defined as an apparent preference driven by the presentation slot rather than candidate content: the judge picks the same slot under both presentation orders, so the canonical content direction flips ⟨§1; §3.3, Eq. 4⟩
- Stable cross-sensitivity is defined as content-stable response to non-target surface-form variation on same-quality ∆0 pairs after order is reversed; the paper stresses it is construct-dependent, not automatically bad, because style/specificity can be part of a target construct ⟨§1; §3.3, Eq. 3; §7⟩
- The direction-stability decomposition is presented as a first-class measurement: raw ∆0 false preference is split into stable cross-sensitivity, positional false preference, one-sided commit, other conflict, and no-preference, related by Eq. 7 ⟨§1; §3.3, Eqs. 2–7⟩
- The paper repeatedly warns that raw ∆0 false preference is a mixture, not a mechanism, and must not be conflated with stable cross-sensitivity ⟨§3.2; §4; App. A.6⟩
- In the three-judge case study the paper reports Llama-3.1-8B as "Class B / Presentation-conflicted": dark current 0.667, raw ∆0 false preference 1.000, but stable cross-sensitivity only 0.033 and positional false preference 0.967 — i.e., its ∆0 response is mostly presentation-driven ⟨§4, Table 3⟩
- It reports Qwen2.5-14B as vacuum-clean (dark current 0.000) and target-sensitive, but with raw ∆0 false preference 0.992 decomposing into mixed stable (0.450) and positional (0.533) components ("Class A-delta0 / Mixed stable-positional") ⟨§4, Table 3⟩
- It reports Qwen2.5-32B as the cleanest observed profile among the three (dark current 0.000, raw ∆0 false preference 0.258, stable cross-sensitivity 0.000, positional false preference 0.083, no-preference 0.567), while stating this is a descriptive result within this stimulus family, not a universal reliability claim ⟨§4, Table 3⟩
- The paper argues a scalar win-rate or agreement score is insufficient because it collapses distinct failure modes (stable nuisance sensitivity, positional preference, one-sided commit, conflict, no-preference) that carry different downstream interpretations ⟨§4⟩
- The headline finding of the criterion-shift probe is that "prompting moves the criterion, not the resolution": a strict tie prompt on Qwen32B eliminates raw ∆0 false preference (0.258→0.000) but absorbs marginal ∆1 target signal into ties (∆1 target sensitivity 0.940→0.500), while preserving ∆5 sensitivity (1.000) ⟨Abstract; §5, Table 4⟩
- The ∆1 loss under the strict criterion is characterized as miss-by-tie rather than wrong-choice error: at ∆1 the wrong-choice rate stays 0.000 and accuracy among non-ties stays 1.000, so the low-strength signal is converted to no-preference, not to error ⟨§5, Table 4; Eq. 12⟩
- Target sensitivity is measured on a constructively controlled prefix-chain checklist ladder yielding Pareto-dominant ∆Q pairs; the detection threshold ∆*75 for Qwen14B and Qwen32B is reported as ≤1 (left-censored by the ladder's integer granularity), while Llama8B requires ∆*75 = 4.0 ⟨§3; §4, Table 3; Eqs. 8–10⟩
- Validity gates are included to prevent syntactic parse success from being treated as scientific validity (parse success, schema validity, semantic validity, hidden-metadata checks) ⟨Table 1; §3⟩
- The paper explicitly maintains a table of non-claims — the downstream mechanism is not confirmed, Qwen32B is not established as a general-purpose evaluator, no broad size-family trend is claimed, and reference/API judges are treated as ceilings/external comparators, not ground truth ⟨Table 5; §7⟩
- Limitations noted include: the stimulus ladder is synthetic (constructive control, not ecological completeness), there is no human ground truth in the reported runs, ∆*75 values are left-censored, and only three open-weight judges are studied ⟨§7⟩

## Concepts & entities covered
Concepts: [[llm-as-judge-bias]] · [[benchmark-validity]]
Entities: [[judge-datasheet]]
