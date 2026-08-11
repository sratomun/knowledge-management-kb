---
title: "OccuBench"
type: entity
subtype: benchmark
aliases: []
tags: [benchmarking]
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
concepts: ["[[human-parity]]", "[[realistic-performance-expectations]]", "[[llm-failure-modes]]"]
sources: ["[[occubench]]"]
updated: 2026-08-10
---

# OccuBench

## What it is
OccuBench is a benchmark that evaluates AI agents on real-world professional occupational tasks across 100 scenarios, 10 industry categories, and 65 specialized domains, using Language Environment Simulators (LLMs configured to act as stateful, interactive environments) to reach domains where no public environment or API exists. It scores both task completion and robustness under environmental fault injection.

## Key facts
- It covers 100 professional scenarios across 10 industry categories and 65 specialized domains, yielding 382 solvable instances (averaging 5.5 tools and 16.2 tool calls each), every scenario mapped to a real human job role ⟨[[occubench]] Abstract; §5.1; Table 1⟩.
- Its core device is the Language Environment Simulator (LES): an LLM given a system prompt, tool schema, initial state, and state description that simulates domain-specific tool responses, making environment construction a configuration problem ⟨[[occubench]] Abstract; §3⟩.
- Agents are scored on Completion Rate (against a rubric-based verifier) and Environmental Robustness (worst-case retention of completion rate under fault injection) ⟨[[occubench]] §5.3⟩.
- The authors report that no single model dominates all industries: GPT-5.2 leads overall at 79.6%, Gemini 3.1 Pro (72.3%) leads Education (84%), and Claude Opus 4.6 (71.5%) leads Transportation (77%) but is weakest in Commerce (53%) ⟨[[occubench]] Abstract; §6.1; Table 2⟩.
- The authors report open-source models are highly competitive, with Qwen 3.5 Plus (69.9%) and DeepSeek V3.2 (69.6%) outperforming most Claude variants ⟨[[occubench]] §6.1⟩.
- The authors report average completion falls from 67.5% (clean) to 53.4% under implicit faults — with implicit faults (truncated data, missing fields) counter-intuitively harder than explicit or mixed faults because they lack overt error signals ⟨[[occubench]] Abstract; §6.2; Table 3⟩.
- The authors report scaling consistently helps, with GPT-5.2 improving 27.5 points (54.7% → 82.2%) from none to xhigh reasoning effort ⟨[[occubench]] Abstract; §6.5⟩.
- The authors report strong agents are not necessarily strong simulators (GPT-5.2 ranks first as an agent but worst as a simulator), while a capable simulator yields reliable rankings (85.7% pairwise agreement) ⟨[[occubench]] Abstract; §6.6⟩.
- Stated limitations: an LES models domain logic rather than real data, and results are tied to the specific simulator, which is part of the evaluation apparatus ⟨[[occubench]] §8.1⟩.

## Relations
- Realizes: [[human-parity]] · [[realistic-performance-expectations]] · [[llm-failure-modes]]
- Defined in: [[occubench]]

## See also
[[human-parity]] · [[realistic-performance-expectations]] · [[llm-failure-modes]] · [[occubench]]
