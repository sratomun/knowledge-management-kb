---
title: "The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["Structured Output Benchmark", "SOB"]
publisher: "Abhinav Kumar Singh, Harsha Vardhan Khurdula, Yoeven D Khemlani & Vineet Agarwal (JigsawStack / Interfaze)"
url: https://arxiv.org/abs/2604.25359
version: "arXiv:2604.25359v1 [cs.CL]"
published: 2026-04
effective_from: 2026-04
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[structured-output-generation]]", "[[schema-guided-extraction]]"]
entities: ["[[sob-benchmark]]"]
updated: 2026-08-11
---

# The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models

## Scope & purpose
A preprint introducing SOB (the Structured Output Benchmark), a multi-source benchmark for evaluating whether LLMs can return JSON that both conforms to a target schema and carries values faithfully grounded in the source context ⟨Abstract; §1⟩. The authors argue that existing benchmarks focus on schema compliance alone or evaluate value correctness within a single source domain, and that in deployment the common failure is a model producing valid JSON whose leaf values are wrong ⟨§1; §2.2⟩. Note on affiliation: the authors are from JigsawStack/Interfaze and include their own "Interfaze-Beta" extraction model among the 21 evaluated; the benchmark's central finding, below, is stated neutrally about all models. (This SOB paper's "ExtractBench" reference is a different benchmark — Ferguson et al. 2026 — not the runllama.ai [[extractbench]] page in this KB.)

## Structure
- §1 Introduction — the schema-compliance vs value-accuracy gap and contributions
- §2 Related work — constrained decoding, gaps in existing structured-output benchmarks, multimodal benchmarks, faithfulness/dataset construction
- §3 Methodology — three source modalities, text-normalized input representation, record format
- §4 Evaluation — seven base metrics (§4.1), hardening/coverage gates (§4.2), evaluation categories (§4.3), aggregation (§4.4)
- §5 Experimental setup — 21 models, inference configuration
- §6 Results — unified leaderboard (§6.1), JSON Pass vs Value Accuracy (§6.2), structured-decoding ablation (§6.3), per-modality results (§6.4–6.5), eight key findings (§6.6), error taxonomy (§6.7)
- §7 Limitations; §8 Conclusion; appendices A–H

## Key points
- SOB spans three source modalities — native text, images, and audio conversations — instantiated with HotpotQA (multi-hop text), OCR-processed PDFs (seven document types, from olmOCR-bench), and the AMI meeting corpus (audio) ⟨Abstract; §3⟩
- A deliberate design choice is that all models receive a text-normalized representation of context regardless of source (images as OCR markdown, audio as timestamped transcripts), to isolate structured-output capability from raw vision or speech processing ⟨Abstract; §3⟩
- The evaluation set comprises 5,000 text records (drawn from a 25,091-record corpus), 209 image records, and 115 audio records, each pairing a question, a JSON schema, and a ground-truth answer ⟨Abstract; §3; Table 8⟩
- Seven per-record metrics are reported — JSON Pass Rate, Faithfulness (token-F1 soft match), Path Recall, Structure Coverage, Type Safety, Perfect Response, and Value Accuracy (exact leaf-value match, the primary metric) ⟨§4.1, Table 1⟩
- Value Accuracy is order-sensitive because flattened paths include concrete array indices, so correct values in the wrong order score zero on those leaves ⟨§4.1⟩
- Key neutral finding: models achieve near-perfect schema compliance, yet the best Value Accuracy reaches only 83.0% on text (GLM-4.7), 67.2% on images (Gemma-4-31B), and 23.7% on audio (Gemini-2.5-Flash) ⟨Abstract; §6.4–6.6; Table 8⟩
- The authors characterize a schema-compliance-vs-value-accuracy gap: across the leaderboard the gap between JSON Pass Rate and Value Accuracy is consistently 15–25 percentage points, an error class they say propagates silently because the JSON parses, validates, and "looks correct" ⟨§6.2⟩
- The authors report that reading Value Accuracy independently reshuffles rankings: mid-sized open models such as Qwen3.5-35B (0.801) outrank closed SoTA models including GPT-5.4 (0.798), Gemini-2.5-Flash (0.796), and Claude-Sonnet-4.6 (0.779) in their evaluation ⟨§6.2, Table 2⟩
- The authors report that model size does not predict structured-output quality — e.g. Phi-4 (14B) at 0.798 Value Accuracy above GPT-5 (0.795), and Schematron-8B (0.754) above GPT-OSS-20B (0.693) — echoing LLMStructBench's finding that prompting strategy matters more than size ⟨§6.6⟩
- The authors report that rankings shift across modalities (GLM-4.7 leads text, Gemma-4-31B leads image, Gemini-2.5-Flash leads audio), so a text-only leaderboard would miss divergent image/audio capability ⟨§6.6⟩
- A structured-decoding ablation reports that passing the schema to the provider for enforcement changes Value Accuracy only slightly (−0.007 to +0.033 across three models), so it does not affect the main accuracy conclusions ⟨§6.3, Table 3⟩
- The error taxonomy lists five failure types by severity: parse failures, schema violations, value errors (the dominant gap — 17–31% of leaf values wrong despite valid structure), missing paths, and type mismatches ⟨§6.7⟩
- Stated limitations/hedges: exact-match scoring penalizes semantic equivalents (e.g. "USA" vs "United States") and treats all arrays as ordered; audio numbers use gold AMI transcripts and are therefore an upper bound (a real ASR front-end would likely degrade Value Accuracy further); ground truth is human-authored with a Gemini LLM cross-check (~3% residual error rate estimated on text) ⟨§3; §7⟩

## Concepts & entities covered
Concepts: [[structured-output-generation]] · [[schema-guided-extraction]]
Entities: [[sob-benchmark]]
