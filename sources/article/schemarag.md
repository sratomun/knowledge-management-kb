---
title: "SchemaRAG: Dynamic Large Schema Reduction for LLM-driven Structured Information Extraction"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["SchemaRAG"]
publisher: "Sin Yu Bonnie Ho, Arlie Coles, Erik Larsson, Eric Marshall, Nathan Bodenstab & Paul Vozila (Microsoft)"
url: https://arxiv.org/abs/2607.00008
version: "arXiv:2607.00008v1 [cs.IR]"
published: 2026-05
effective_from: 2026-05
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[schema-guided-extraction]]", "[[structured-output-generation]]"]
entities: ["[[schemarag-system]]"]
updated: 2026-08-11
---

# SchemaRAG: Dynamic Large Schema Reduction for LLM-driven Structured Information Extraction

## Scope & purpose
A Microsoft research paper proposing SchemaRAG, a retrieval-augmented generation framework that dynamically prunes a large output schema for schema-conditioned information extraction ⟨Abstract; §1⟩. The authors motivate it by the problems of injecting a full, large schema into the prompt: increased cost and latency, "lost-in-the-middle" performance degradation, and the risk of exceeding context-length limits ⟨Abstract; §1⟩. Rather than retrieving text chunks (as in classic RAG), SchemaRAG applies retrieval to the output schema itself, selecting a relevant subset of schema rows just-in-time for a prompted LLM extraction call ⟨§2; §3⟩.

## Structure
- §1 Introduction — the large-schema extraction problem; contributions
- §2 Related work — LLM IE, text-based RAG, table-centric RAG, and the gap in retrieving over output schemas
- §3 Methodology — schema reduction via row and example embeddings (§3.1); transcript segmentation (§3.2)
- §4 Experiments — Nursing and Amazon datasets (§4.1), models/hyperparameters (§4.2), metrics (§4.3), baselines/oracle (§4.4), accuracy (§4.5), latency/token use (§4.6), ablations (§4.7)
- §5 Conclusion; §6 Limitations; Ethical Considerations; appendices A–H

## Key points
- SchemaRAG reduces a schema S of m rows to a smaller set S_κ of κ ≪ m most-relevant rows by embedding each row's metadata (name, category names, possible values) and, when available, annotated examples, then ranking by cosine similarity to the transcript embedding and taking a top-k ⟨§3.1⟩
- The framework is described as schema-agnostic, supporting arbitrary hierarchy, training-free (no pretraining or fine-tuning), with retrieval embeddings computable offline ⟨§1⟩
- For long inputs, a prompted LLM call segments the transcript into n segments, and SchemaRAG runs per-segment schema reduction and extraction to counter lost-in-the-middle effects ⟨§3.2⟩
- Reported headline results: up to an 8.8% increase in micro-F1, a 47% reduction in latency, and a 48% reduction in token cost, which the authors state "vary by dataset" ⟨Abstract; §1⟩
- Evaluation uses two real-world large-schema datasets: Nursing (four proprietary hospital test sets of de-identified nurse rounding dictations, ~48–50 transcripts each) and Amazon (48 products from the Bright Data Amazon Products sample, schema S_Am of 1906 rows) ⟨§4.1⟩
- Experiments use OpenAI text-embedding-ada-002 as the embedder and GPT-4o (temperature 0) for segmentation and extraction, with the hyperparameter k fixed to 60 and each experiment repeated three times ⟨§4.2⟩
- The authors report micro-F1 gains of 8.8% on Nursing (0.844 → 0.918) and 8.3% on Amazon (0.471 → 0.510) over the full-schema baseline ⟨§4.5, Table 3⟩
- An oracle upper bound (reduced schema built directly from the reference annotated rows) reaches 0.952 (Nursing) and 0.775 (Amazon), which the authors present as a high theoretical ceiling for schema reduction ⟨§4.5, Table 3⟩
- On latency, the authors report SchemaRAG is 47% faster than the baseline on Nursing (6.0s vs 11.3s), while on Amazon latency is slightly higher but not statistically significant, attributed to the O(T) segmentation call dominating for Amazon's ~10× longer transcripts ⟨§4.6, Table 4⟩
- On token cost, the authors report a 48% reduction on Nursing but an increase on Amazon (input tokens exceed the baseline by ~40%), because each per-segment prompt re-includes the full transcript for context ⟨§4.6, Table 4⟩
- Ablations report that combining row and example embeddings yields the best macro-F1 (0.899 vs 0.888 row-only, 0.798 example-only), and that performance rises with k until it saturates and declines as the reduced schema grows too large ⟨§4.7, Table 10; Figure 5⟩
- The paper reports SchemaRAG outperforming both a full-schema baseline and a lightweight row-name-only (table-inspired) baseline (Nursing 0.918 vs 0.800; Amazon 0.510 vs 0.341) ⟨Appendix E, Table 7⟩
- Stated limitation: accuracy is consistently lower on Amazon than Nursing, which the authors attribute to Amazon's noisier, manually constructed schema and labels, longer multi-topic inputs, and lack of in-domain labeled examples ⟨§6⟩
- The authors suggest a human-in-the-loop deployment (clinician review, audit trails) for the clinical setting, noting transcription/labeling errors may propagate ⟨Ethical Considerations⟩

## Concepts & entities covered
Concepts: [[schema-guided-extraction]] · [[structured-output-generation]]
Entities: [[schemarag-system]]
