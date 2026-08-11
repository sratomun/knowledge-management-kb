---
title: "SchemaRAG framework"
type: entity
subtype: technique
aliases: []
tags: [doc-processing]
published: 2026-05
effective_from: 2026-05
effective_to: ongoing
status: current
concepts: ["[[schema-guided-extraction]]", "[[structured-output-generation]]"]
sources: ["[[schemarag]]"]
updated: 2026-08-11
---

# SchemaRAG framework

## What it is
SchemaRAG is a Microsoft retrieval-augmented generation framework for schema-conditioned structured information extraction that dynamically prunes a large output schema, injecting only a relevant subset of schema rows into a just-in-time LLM extraction prompt. It applies retrieval to the output schema itself rather than to text chunks, to avoid the cost, latency, lost-in-the-middle degradation, and context-length problems of placing a full large schema in the prompt.

## Key facts
- Reduces a schema of m rows to a top-k subset of κ ≪ m rows by embedding each row's metadata (name, categories, possible values) and any annotated examples, then ranking by cosine similarity to the transcript embedding ⟨[[schemarag]] §3.1⟩.
- Is described as schema-agnostic, supporting arbitrary hierarchy, and training-free, with retrieval embeddings computable offline ⟨[[schemarag]] §1⟩.
- Segments long transcripts (via a prompted LLM call) and runs per-segment schema reduction and extraction to counter lost-in-the-middle effects ⟨[[schemarag]] §3.2⟩.
- Reported headline results are up to +8.8% micro-F1, −47% latency, and −48% token cost, which the authors note vary by dataset ⟨[[schemarag]] Abstract; §1⟩.
- Evaluated on two large-schema datasets — Nursing (proprietary de-identified nurse dictations across four hospitals) and Amazon (a 1906-row product schema from the Bright Data sample) — using text-embedding-ada-002 and GPT-4o with k=60 ⟨[[schemarag]] §4.1; §4.2⟩.
- The authors report micro-F1 gains of 8.8% on Nursing (0.844 → 0.918) and 8.3% on Amazon (0.471 → 0.510) over a full-schema baseline, with an oracle upper bound of 0.952 / 0.775 ⟨[[schemarag]] §4.5; Table 3⟩.
- The authors report a 47% latency reduction and 48% token-cost reduction on Nursing, but slightly higher (non-significant) latency and increased token cost on Amazon, attributed to its ~10× longer transcripts and the full transcript being re-included per segment ⟨[[schemarag]] §4.6; Table 4⟩.

## Relations
- Realizes: [[schema-guided-extraction]] · [[structured-output-generation]]
- Defined in: [[schemarag]]

## See also
[[schema-guided-extraction]] · [[structured-output-generation]] · [[schemarag]]
