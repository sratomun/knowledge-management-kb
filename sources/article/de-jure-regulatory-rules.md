---
title: "De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["De Jure"]
publisher: arXiv
url: https://arxiv.org/abs/2604.02276
published: 2026
effective_from: 2026-04
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

## Scope & purpose

De Jure (Document Extraction with Judge-Refined Evaluation) is a fully automated,
domain-agnostic pipeline, authored by researchers at The Vanguard Group, for transforming
raw regulatory documents into structured, machine-readable rule sets. It aims to remove the
costly, expert-intensive bottleneck of hand-converting dense, hierarchically structured
legal text into machine-actionable rules, requiring no human annotation, domain-specific
prompting, or annotated gold data ⟨abstract⟩. The stated motivation is regulation-grounded
LLM alignment: aligning systems not only with human preferences but with explicit, codified
regulatory obligations such as HIPAA, the SEC Advisers Act, and the EU AI Act ⟨§1⟩.

## Structure

The paper runs: introduction and motivation for regulation-grounded alignment (§1); related
work across regulatory rule extraction, deontic/defeasible logic formalisms, and LLM
self-refinement (§2); the four-stage De Jure pipeline — pre-processing, rule generation,
multi-criteria judgment, and selective repair (§3); experiments covering extraction quality,
cross-domain generalization, and downstream compliance QA via RAG (§4); ablation studies
(§5); and conclusion (§6). Appendices detail ablations, the 19 judgment criteria, algorithm,
a worked repair example, and full prompts and schemas.

## Key points

- The paper presents De Jure as a four-stage pipeline: (1) normalization of source documents
  into structured, section-segmented Markdown; (2) LLM-driven rule generation into a typed
  JSON schema; (3) multi-criteria LLM-as-a-judge evaluation across 19 dimensions in three
  sequential stages; and (4) iterative repair of low-scoring extractions within a bounded
  regeneration budget ⟨abstract, §3⟩.
- Pre-processing converts each document to Markdown using Docling (preserving section
  boundaries, lists, and tables), then splits on regulatory delimiters ("§", "Article",
  "Rule") into section–content pairs, each indexed by regulatory identifier and assigned a
  SHA-256 fingerprint for traceability, so that every downstream extraction traces back to an
  exact source span ⟨§3.1⟩.
- The extraction schema decomposes each section into section metadata (citation, title,
  effective dates, notes), definitions (term, text, scope, cross-references), and rule units;
  each rule unit carries an identifier, rule type, label, citation, and a nine-field
  statement decomposition: action, action object, method, conditions, constraints,
  exceptions, penalties, purpose, and verbatim source span ⟨§3.2⟩.
- The generation prompt is schema-driven with no domain-specific examples or seed rules, and
  returns null for non-actionable sections to suppress non-normative passages (preambles,
  cross-reference tables) and prevent rule-set inflation ⟨§3.2⟩.
- A core design principle the authors call hierarchical decoupling / hierarchical repair
  ordering: the three judgment stages are applied in dependency order (metadata, then
  definitions, then rule units) so upstream components are verified and repaired before rule
  units are evaluated, ensuring rule-level repair always operates on reliable context ⟨§3, §3.3⟩.
- The judge is organized into three stages — Judge 1 (section metadata, 6 criteria), Judge 2
  (definitions, 5 criteria), and Judge 3 (per-rule quality, 8 criteria); each criterion is
  scored 0–5 with a natural-language justification ⟨§3.3, Appendix B, Table 8⟩.
- Selective repair regenerates a stage only if its average score falls below θ = 0.90,
  re-prompting the model with the original text, current extraction, per-criterion scores,
  and critiques for at most r = 3 attempts, retaining the best-scoring output to guarantee
  monotonically non-decreasing quality ⟨§3.4⟩.
- Extraction and judgment are performed by strictly separate models: the backbone model under
  evaluation performs extraction, while a fixed model (Cohere Compass) performs judgment ⟨§4⟩.
- The paper evaluates four backbone models (Llama-3.1-8B, Qwen3-VL-8B, Claude-3.5-Sonnet,
  GPT-5-mini) on the SEC Advisers Act; it reports that overall scores range 4.74–4.85 (scale
  1–5) and that performance degrades monotonically from metadata (~4.96) to definitions
  (~4.82) to per-rule quality (~4.65) ⟨§4.2, Table 2⟩.
- The paper reports that Non-Hallucination is uniformly perfect (5.00) across all models and
  all three judges, which the authors attribute to schema-constrained extraction eliminating
  factual fabrication as a failure mode ⟨§4.2⟩.
- For cross-domain generalization, the authors report that with no changes to prompts, schema,
  or model configuration, De Jure maintains overall scores above 4.70 across three
  structurally distinct corpora (SEC finance, HIPAA healthcare, EU AI Act governance), a
  monotonic decline they say tracks structural regularity ⟨§4.3, Table 3⟩.
- In a downstream compliance-QA-via-RAG comparison against Datla et al. (2025) on HIPAA, the
  paper reports that De Jure-grounded responses are preferred by a judge LLM in 73.8% of cases
  at single-rule retrieval depth (k=1), rising to 84.0% at k=10 ⟨abstract, §4.4, Table 4⟩.
- The authors' ablations report that extraction quality improves monotonically with acceptance
  threshold θ; that the retry budget is the dominant quality lever with a non-linear jump at
  r=2; that their section-aware chunking outperforms the baseline's by +0.16 points overall
  (concentrated in early stages); and that regeneration-trigger granularity is second-order
  ⟨§5, Appendix A⟩.
- The authors position their contribution as demonstrating that explicit, interpretable
  evaluation criteria can substitute for human annotation in regulatory domains, offering a
  scalable and auditable path toward regulation-grounded LLM alignment ⟨abstract, §6⟩.

## Concepts & entities covered
Concepts: [[compliance-checking]] · [[obligation-extraction]] · [[rules-as-code]] · [[machine-readable-legal-norms]]
Entities: [[de-jure-system]]
