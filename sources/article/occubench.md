---
title: "OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["OccuBench"]
publisher: "Xiaomeng Hu, Yinger Zhang, Fei Huang et al. (Qwen Team, Alibaba Group; CUHK)"
url: https://arxiv.org/abs/2604.10866
version: "arXiv:2604.10866v2 [cs.CL]"
published: 2026
effective_from: 2026
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[human-parity]]", "[[realistic-performance-expectations]]", "[[llm-failure-modes]]"]
entities: ["[[occubench]]"]
updated: 2026-08-10
---

# OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation

## Scope & purpose
A benchmark paper from the Qwen Team (Alibaba) and CUHK that evaluates AI agents on real-world professional tasks across many occupations, addressing what it calls the "untestable majority" — the high-value professional domains where no public environment or API exists ⟨Abstract; §1⟩. Its central device is the Language Environment Simulator (LES): an LLM configured with a system prompt, tool schema, initial state, and state description that acts as a stateful, interactive environment, turning environment construction from an engineering problem into a configuration problem ⟨Abstract; §3⟩. OccuBench covers 100 professional task scenarios across 10 industry categories and 65 specialized domains (382 solvable instances), each mapped to a real human job role, and evaluates both task completion and robustness under fault injection ⟨Abstract; §5.1⟩. The KB records the paper's cross-model comparative findings descriptively.

## Key points
- The benchmark spans 100 real-world professional scenarios across 10 industry categories and 65 specialized domains, yielding 382 solvable instances (averaging 5.5 tools and 16.2 tool calls per task), each scenario mapped to an actual job role such as emergency triage nurse, customs officer, or production scheduler ⟨Abstract; §5.1; Table 1⟩
- Instances are produced by a multi-agent synthesis pipeline (powered by Gemini-3-Flash-Preview as the LES) that guarantees solvability, calibrates difficulty for discriminative power, and grounds diversity in per-scenario reference documents; trivially-easy (100% success) and unsolvable (0% success) items are filtered out ⟨§4; §5.1⟩
- Agents are scored along two dimensions: Task Completion (Completion Rate against a rubric-based verifier) and Environmental Robustness (worst-case retention of completion rate under fault injection) ⟨§5.2; §5.3⟩
- The study evaluates 15 frontier models across 8 model families (OpenAI, Anthropic, Google, DeepSeek, Moonshot, MiniMax, Zhipu, Alibaba), all in thinking/reasoning mode ⟨Abstract; §6⟩
- The authors report that no single model dominates all industries: GPT-5.2 leads overall at 79.6% but scores only 67% in Commerce, while Gemini 3.1 Pro (72.3%) leads Education (84%) and Science (81%) yet struggles in Healthcare (62%), and Claude Opus 4.6 (71.5%) is strongest in Transportation (77%) but weakest in Commerce (53%) ⟨Abstract; §6.1; Table 2⟩
- The paper reports each model has a distinct "occupational capability profile," and argues organizations should select agents by their specific industry rather than by aggregate ranking ⟨§6.1; §7.2⟩
- The authors report open-source models are highly competitive — Qwen 3.5 Plus (69.9%) and DeepSeek V3.2 (69.6%) rank 4th–5th, outperforming most Claude variants — challenging the assumption that closed models uniformly lead on professional tasks ⟨§6.1⟩
- On robustness, the paper reports average completion falls from 67.5% (clean, E0) to 53.4% under implicit faults (E2), a 14.1-point decline, with even strong models hit hard (Claude Opus 4.6 drops 17.6 points, 71.5% → 53.9%) — a gap the authors read as separating clean-environment capability from deployment readiness ⟨§6.2; Table 3⟩
- The authors report implicit faults (E2: truncated data, missing fields) are counter-intuitively harder than explicit (E1: timeouts, HTTP 500) or mixed (E3) faults, because implicit faults lack overt error signals and require the agent to independently detect data degradation, a capability most models lack ⟨Abstract; §6.2⟩
- The paper reports scaling consistently improves performance — larger models, newer generations, and higher reasoning effort all help; GPT-5.2 improves 27.5 points (54.7% → 82.2%) from none to xhigh reasoning effort ⟨Abstract; §6.3; §6.5⟩
- On the LES device itself, the authors report that strong agents are not necessarily strong simulators: GPT-5.2 ranks first as an agent (79.6%) but produces the worst simulation quality (agents average only 29.3% under a GPT-5.2 simulator vs 67.9% under Gemini Flash), attributed to state fabrication, entity omission, and rule invention ⟨Abstract; §6.6; Table 4⟩
- The paper reports that with a sufficiently capable simulator, LES-based evaluation is reliable: the Qwen 3.5 Plus simulator agrees with Gemini Flash on 85.7% of pairwise model orderings (top-3 agents matching exactly) ⟨§6.6; Figure 8⟩
- Documented failure modes from case studies include skipped safety-critical verification, procedural-ordering errors, missing proactive constraint monitoring, and (for weaker simulators) violation of the environment contract ⟨§7.3–7.5; Figures 9–14⟩
- Stated hedges/limitations: an LES models domain logic rather than real domain data, so exact-value-critical tasks need real-environment testing; and results are tied to the specific simulator used, which is part of the evaluation apparatus, not a neutral observer ⟨§8.1⟩

## Concepts & entities covered
Concepts: [[human-parity]] · [[realistic-performance-expectations]] · [[llm-failure-modes]]
Entities: [[occubench]]
