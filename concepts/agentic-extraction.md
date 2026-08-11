---
title: "Agentic Extraction"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[agentic-reflection-control]]", "[[extraction-verification]]", "[[intelligent-document-processing]]"]
updated: 2026-08-11
---

# Agentic Extraction

## What it is
Agentic extraction wraps information extraction in an agent loop rather than a single fixed prompt: the system plans, calls tools, inspects intermediate results, retries, reflects, and maintains memory across steps. The aim is to handle heterogeneous documents, long inputs, complex tables, and multi-hop queries that overwhelm a one-shot call. Sources span a spectrum from full agent harnesses to critical studies asking whether the added agentic machinery actually improves extraction outcomes, and they report both gains and their costs.

## How sources treat it
- **[[st-raptor]]** _(article · informational)_ — An Orchestration Agent tracks query history, resolves ambiguous references (e.g. "this product" → "Product A"), routes queries to retrieval/aggregation modules, maintains a dynamic memory loop across files/tables/turns, and invokes VLMs for extraction; the full agentic system reportedly surpasses the best baseline by 11.2% ⟨Core approach; Evaluation⟩
- **[[deep-tabular-research]]** _(article · informational)_ — Drives an agent with accumulated execution experience (a siamese structured memory recording parameterized signals and abstracted textual patterns) and majority-vote across paths; reports its 4.78-call operating point outperforming a CodeLoop baseline that reaches only 27.5% accuracy despite 8.8 calls ⟨§3.4; §4.3, Figure 3⟩
- **[[scair]]** _(article · informational)_ — A training-free agentic KG-RAG framework that requires more LLM calls (42.36) and tokens (22.5k in / 5.9k out) than ToG (13.95) and PoG (5.60) for deeper traversal (depth 2.54), a cost the authors call "functional"; warns generic agentic designs "fail to generalize" to enterprise KGs ⟨Table 2; Abstract / §1⟩
- **[[idp-accelerator]]** _(article · informational)_ — An AWS-affiliated open-source framework for agentic end-to-end document intelligence (classification, extraction, MCP-compliant analytics, rule validation); reports a healthcare deployment improving classification accuracy from 94% to 98% with 77% lower cost and 80% lower latency ⟨Key technique points; Abstract / Real-world⟩
- **[[extractbench]]** _(article · informational)_ — Evaluates coding agents (Claude Code Opus 4.8, Codex GPT-5.5) as one of three extraction families, reporting them reaching 87.1% and 93.6% overall value F1 at 16.2 and 27.8 ¢/page — higher accuracy but higher cost than commercial VLMs ⟨§3.1; §3.2⟩
- **[[agentic-controllability-ie]]** _(article · informational)_ — A deliberately neutral study finding the agent harness increases coverage only modestly (S0 158 → S1b 168 records) while internal activity explodes (log lines 7,084 → 50,189; 2,222 retries), concluding "evidence is stronger for behavioral change than for absolute accuracy improvement" ⟨Table 1; Table 2; Key results⟩

## Where sources differ
The sources disagree on whether agentic machinery pays off. [[st-raptor]], [[deep-tabular-research]], [[idp-accelerator]], and [[scair]] report agentic designs winning on their benchmarks, though [[scair]] stresses that only domain-constrained agents generalize and that cost rises sharply. [[extractbench]] positions coding agents as accurate-but-expensive relative to VLMs and specialized APIs. [[agentic-controllability-ie]] is the skeptical voice: it finds reflection and memory produce far more internal activity than output improvement and that "indiscriminate deep LLM reflection may not be justified for every paper," while explicitly hedging on a single corpus and no gold standard. The KB leaves these standing side by side rather than adjudicating whether agents help; note [[extractbench]] and [[idp-accelerator]] evaluate their own or affiliated systems.

## See also
[[agentic-reflection-control]] · [[extraction-verification]] · [[extraction-self-verification]] · [[intelligent-document-processing]] · [[complex-table-understanding]] · [[schema-guided-extraction]] · [[provenance-constrained-extraction]]
