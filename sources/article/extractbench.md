---
title: "ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["ExtractBench"]
publisher: "Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li & Simon Suo (runllama.ai / LlamaIndex)"
url: https://arxiv.org/abs/2607.29677
version: "arXiv:2607.29677v2 [cs.AI]"
published: 2026-07
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[schema-guided-extraction]]", "[[agentic-extraction]]", "[[structured-output-generation]]"]
entities: ["[[extractbench-benchmark]]"]
updated: 2026-08-11
---

# ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

## Scope & purpose
A technical report (July 2026) introducing ExtractBench, a benchmark for schema-guided enterprise document extraction: given a document and a user-defined schema, an agent is asked to faithfully follow the schema to produce correct output with source evidence as grounding metadata ⟨Abstract; §2.1⟩. The authors state that, to their knowledge, it is the first evaluation to report value accuracy, record completeness at scale, grounding, and measured cost together ⟨Abstract⟩. Note on affiliation: the authors are from runllama.ai (LlamaIndex), and one of the systems they evaluate — LlamaExtract — is their own product; the comparative rankings below are the paper's own claims and should be read with that in mind (per the KB's descriptive-only stance). The paper also flags a name collision: Contextual AI publishes a separate, unrelated benchmark also called "ExtractBench" ⟨§1 footnote; §4⟩.

## Structure
- §1 Introduction — the schema-guided extraction task, gap in existing benchmarks, contributions
- §2 ExtractBench — task definition (§2.1), taxonomy/coverage across five tag axes (§2.2), schema and ground-truth construction (§2.3), metrics (§2.4)
- §3 Experiments — setup (§3.1), quality–cost frontier (§3.2), results across dimensions (§3.3), the grounding gap (§3.4)
- §4 Related work — fixed-ontology vs schema-guided benchmarks; VLM / coding-agent / specialized-API method families
- §5 Conclusion; appendices A–E (tag definitions, procedures, scoring rules, per-tag tables)

## Key points
- The paper defines schema-guided extraction as a function f : (document, schema) → (structured data, evidence), where the user's JSON Schema lists fields (name, type, natural-language description) and unanswered fields must return `null` ⟨§2.1⟩
- The corpus contains 370 enterprise documents (4,869 pages) across 8 business domains and 67 document types, with each document type sharing exactly one schema ⟨Abstract; §1; §2.2⟩
- Documents are tagged along five independent axes — task challenge, perception challenge, table structure, length, and business domain (22 challenge tags total) — so a low score can be traced to its cause ⟨§2.2⟩
- The three sources of ground truth use different trust bases: cross-model agreement plus human review for real born-digital documents, by-construction values for synthetic long lists, and per-field human verification for scanned forms ⟨§2.3⟩
- Scanned-form verification yields 169 human-verified documents, with 84% of verified fields carrying a human-placed bounding box (the rest mostly blank fields) ⟨§2.3⟩
- Value accuracy is scored with an order-insensitive "unified value F1": outputs are flattened into cells, records in arrays are paired by the Hungarian algorithm, values normalized (dates to ISO, whitespace collapsed) with no numeric tolerance and no LLM judge ⟨§2.4⟩
- Grounding is scored only where box ground truth is verified: word-level grounding F1 requires a correct value and a predicted box overlapping an accepted box at IoU 0.5, and page-level grounding F1 requires only the correct source page ⟨§2.4⟩
- 14 extraction systems are evaluated across three families — commercial/self-hosted VLMs, coding agents (Claude Code Opus 4.8, Codex GPT-5.5), and specialized APIs (Reducto, Extend, Datalab, three LlamaExtract tiers) — without benchmark-specific tuning ⟨§3.1⟩
- The paper reports per-page cost spanning roughly 0.2¢ to 34¢ across systems, and argues cost must be evaluated jointly with accuracy because "greater spending does not necessarily produce greater accuracy" ⟨Figure 1; §3.2⟩
- The authors report that commercial VLMs occupy the low-cost region (≤1.0 ¢/page) but none exceeds 80% overall value F1, while coding agents reach 87.1% (Claude Code Opus 4.8) and 93.6% (Codex GPT-5.5) at 16.2 and 27.8 ¢/page ⟨§3.2⟩
- The authors report that their own LlamaExtract Agentic Plus traces the quality–cost frontier and ranks first on all three metrics, reaching 95.6% overall value F1 at 8.1 ¢/page — described as outperforming both coding agents at no more than half the cost ⟨Abstract; §3.2⟩ (vendor-authored claim; see affiliation note above)
- On document length, the authors report commercial VLMs falling below 40% value F1 on long (>50pp) documents, e.g. Gemini 3.5 Flash dropping from 87.9% (short) to 27.9% (long), while LlamaExtract Agentic Plus scores 96.6/93.3/94.4 across short/medium/long ⟨§3.3, Table 2⟩
- The paper attributes the long-document failure to context limits and truncation of long record lists — a recall problem where entire records are dropped rather than misread ⟨§3.3⟩
- On enormous tables (S4, beyond a thousand rows) the authors report every VLM scoring below 10%, versus LlamaExtract Agentic Plus 95.9%, Reducto Deep Extract 95.3%, and Claude Code Opus 4.8 87.8% ⟨§3.3, Table 2⟩
- On the grounding gap: VLMs and coding agents return no evidence by default and therefore score zero at both grounding levels; even the best word-level grounding F1 is only 46.4% (LlamaExtract Agentic Plus, versus its 84.9% page-level), which the authors call an open problem ⟨§3.4, Table 3⟩
- Stated positioning: the authors claim ExtractBench provides the broadest combined coverage of long-record completeness, real scans/handwriting, word- and page-level grounding, and measured cost, contrasting it with fixed-KIE benchmarks (SROIE, DocILE, RealKIE) and narrower schema-guided ones ⟨§4; Table 1⟩

## Concepts & entities covered
Concepts: [[schema-guided-extraction]] · [[agentic-extraction]] · [[structured-output-generation]]
Entities: [[extractbench-benchmark]]
