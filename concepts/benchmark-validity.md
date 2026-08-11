---
title: "Benchmark validity"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[benchmark-saturation]]", "[[benchmark-contamination]]", "[[llm-as-judge-bias]]", "[[human-parity]]"]
updated: 2026-08-10
---

# Benchmark validity

## What it is
Benchmark validity is the degree to which a benchmark actually measures the capability it claims to measure, and thereby supports the conclusions drawn from its scores. It is threatened from several directions at once: contamination (memorized answers), saturation (lost discriminative power), judge bias (a distorted scoring instrument), variance and error-magnitude blindness (accuracy hiding unreliability), and mistaking human agreement for correctness. Sources in this domain each attack a different validity threat and argue that headline accuracy alone is an insufficient warrant for real-world capability claims.

## How sources treat it
- **[[automation-narrative-flaws]]** _(article · informational)_ — argues average-accuracy benchmarks are an invalid basis for expert-equivalence claims because they ignore contamination, response stochasticity, and error magnitude, and calls for measuring variance and catastrophic-error size rather than accuracy alone ⟨§1.1; §4⟩
- **[[agreement-is-not-quality]]** _(article · informational)_ — argues that agreement with human coders is not a valid quality measure when no ground truth exists, framing consistent-but-biased outputs as reliability without validity ⟨Introduction; Related Work⟩
- **[[llm-judge-dark-current]]** _(article · informational)_ — argues an LLM judge must be characterized as a measurement instrument (across dark current, positional preference, and criterion) before its scores count as evidence, because a scalar score collapses distinct failure modes ⟨§1; §4⟩
- **[[benchmark-saturation]]** _(article · informational)_ — frames saturation as eroding a benchmark's discriminative validity, while noting a valid saturated benchmark may simply mean the task is solved and only becomes a problem when it reflects lost resolution ⟨§2.1; §5.4⟩
- **[[contamination-resistant]]** _(article · informational)_ — argues contamination diminishes benchmarks' value as reliable measures of generalization, so datasets should be released in a form that stays useful for evaluation while being unlearnable ⟨§2.1; §1⟩

## Where sources differ
Each source targets a different threat to validity: [[automation-narrative-flaws]] the metrics (variance and error magnitude), [[agreement-is-not-quality]] the ground-truth assumption, [[llm-judge-dark-current]] the scoring instrument, [[benchmark-saturation]] the benchmark's lifecycle resolution, and [[contamination-resistant]] the data's leakage into training. They agree that accuracy is not self-validating but propose non-overlapping remedies. The KB surfaces all five threats side by side without prioritizing them.

## See also
[[benchmark-saturation]]
[[benchmark-contamination]]
[[llm-as-judge-bias]]
[[human-parity]]
[[evaluation-illusion]]
