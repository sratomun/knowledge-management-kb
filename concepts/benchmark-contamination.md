---
title: "Benchmark contamination"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[benchmark-validity]]"]
updated: 2026-08-10
---

# Benchmark contamination

## What it is
Benchmark contamination is the leakage of benchmark items or answers into a model's pretraining data, so that high scores reflect memorization of the test rather than generalization to the underlying capability. Because scores can be inflated by recall of seen data, contamination is a direct threat to a benchmark's validity, and it motivates designs — private, dynamic, obfuscated, or cryptographically contamination-resistant — that keep a benchmark usable for evaluation while preventing it from being learned.

## How sources treat it
- **[[contamination-resistant]]** _(article · informational)_ — defines contamination as benchmark samples being ingested into pretraining corpora, which inflates accuracy by rewarding recall of pretraining data and diminishes benchmarks' value as measures of generalization ⟨§1; §2.1⟩
- **[[contamination-resistant]]** _(article · informational)_ — reports contamination as widespread and rising with scale, citing GPT-3 flagging over 90% of examples in some benchmarks, Llama 2 contamination in over 16% of MMLU, and multilingual audits up to 91.8%, and notes a clean non-public GSM8K mirror can reduce accuracy up to 13% ⟨§1; §2.1⟩
- **[[contamination-resistant]]** _(article · informational)_ — proposes a contamination-resistant dataset satisfying irreversibility, equivalence, and interoperability, exploiting the Transformer training-inference asymmetry so a released form supports inference but not training ⟨§2.3; §3⟩
- **[[contamination-resistant]]** _(article · informational)_ — reviews alternatives (private benchmarking, dynamic benchmarking, lexical obfuscation, and decontamination/filtering) and argues each has drawbacks such as cost, short lifespan, or failure to catch paraphrase and translation leakage ⟨§6⟩
- **[[automation-narrative-flaws]]** _(article · informational)_ — treats benchmark contamination as "perhaps most fundamental," citing a contamination-controlled benchmark on which frontier LLMs answered only 10% correctly while human experts answered 90% ⟨§1.1⟩

## Where sources differ
[[contamination-resistant]] proposes a technical construction to make datasets unlearnable while still usable, and reviews private and dynamic benchmarking as weaker alternatives, whereas [[automation-narrative-flaws]] invokes contamination mainly as a reason to distrust human-parity claims drawn from public benchmark scores. One source's remedy (contamination-resistant release) is another's cautionary premise. The KB records both without endorsing a fix.

## See also
[[benchmark-validity]]
[[benchmark-saturation]]
