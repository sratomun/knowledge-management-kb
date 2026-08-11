---
title: "Structured Output Benchmark (SOB)"
type: entity
subtype: benchmark
aliases: []
tags: [doc-processing]
published: 2026-04
effective_from: 2026-04
effective_to: ongoing
status: current
concepts: ["[[structured-output-generation]]", "[[schema-guided-extraction]]"]
sources: ["[[structured-output-benchmark]]"]
updated: 2026-08-11
---

# Structured Output Benchmark (SOB)

## What it is
SOB is a multi-source benchmark for evaluating LLM structured-output quality across three source modalities — native text, images, and audio conversations — where each record pairs a question, a JSON schema, and a ground-truth answer. Its distinguishing focus is per-field value accuracy (exact leaf-value match) rather than schema compliance alone, evaluated after normalizing every source to a text representation so structured-output capability is isolated from vision or speech processing.

## Key facts
- Comprises 5,000 text records (from a 25,091-record corpus built on HotpotQA), 209 image records (OCR-processed PDFs across seven document types), and 115 audio records (AMI meeting corpus) ⟨[[structured-output-benchmark]] Abstract; §3; Table 8⟩.
- Reports seven per-record metrics — JSON Pass Rate, Faithfulness, Path Recall, Structure Coverage, Type Safety, Perfect Response, and Value Accuracy (the primary, exact-match metric) ⟨[[structured-output-benchmark]] §4.1; Table 1⟩.
- Central neutral finding: across 21 evaluated models, schema compliance is near-perfect yet best Value Accuracy reaches only 83.0% on text, 67.2% on images, and 23.7% on audio ⟨[[structured-output-benchmark]] Abstract; §6.6; Table 8⟩.
- Characterizes a schema-compliance-vs-value-accuracy gap of a consistent 15–25 percentage points between JSON Pass Rate and Value Accuracy across the leaderboard ⟨[[structured-output-benchmark]] §6.2⟩.
- The authors report that model size does not predict structured-output quality (e.g. Phi-4 at 14B outscoring GPT-5 on Value Accuracy) and that rankings shift across modalities ⟨[[structured-output-benchmark]] §6.6⟩.
- Value Accuracy is order-sensitive (flattened paths carry array indices), so correct values in the wrong order score zero on those leaves ⟨[[structured-output-benchmark]] §4.1⟩.
- Stated hedges: exact-match scoring penalizes semantic equivalents (e.g. "USA" vs "United States"); audio uses gold AMI transcripts and is therefore an upper bound; ground truth is human-authored with a Gemini LLM cross-check (~3% residual text error rate) ⟨[[structured-output-benchmark]] §3; §7⟩.

## Relations
- Realizes: [[structured-output-generation]] · [[schema-guided-extraction]]
- Defined in: [[structured-output-benchmark]]

## See also
[[structured-output-generation]] · [[schema-guided-extraction]] · [[structured-output-benchmark]]
