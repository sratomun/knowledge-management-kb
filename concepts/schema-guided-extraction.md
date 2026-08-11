---
title: "Schema-Guided Extraction"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[structured-output-generation]]", "[[schema-based-vs-schema-free-construction]]"]
updated: 2026-08-11
---

# Schema-Guided Extraction

## What it is
Schema-guided extraction is the task of populating a user-defined output schema from a document: the caller supplies a target structure (fields, types, descriptions), and an LLM or agent returns values conforming to it, ideally with evidence linking each value back to the source. The schema is an input that conditions extraction — as opposed to schema-free construction, where structure is discovered rather than given. Sources treat it as a benchmarking target, a retrieval problem when the schema is large, and a production pattern in agentic document pipelines.

## How sources treat it
- **[[extractbench]]** _(article · informational)_ — Defines schema-guided extraction as a function f : (document, schema) → (structured data, evidence) where the JSON Schema lists fields (name, type, natural-language description) and unanswered fields must return `null`; evaluates 14 systems over 370 enterprise documents (4,869 pages), 8 domains, 67 document types, each type sharing one schema ⟨§2.1; §2.2⟩
- **[[schemarag]]** _(article · informational)_ — Applies retrieval to the output schema itself, pruning a schema of m rows to κ ≪ m most-relevant rows just-in-time, motivated by cost, latency, and "lost-in-the-middle" degradation when a large schema is injected whole; reports micro-F1 gains of 8.8% on Nursing (0.844 → 0.918) and 8.3% on Amazon (0.471 → 0.510) over the full-schema baseline ⟨§3.1; §4.5, Table 3⟩
- **[[structured-output-benchmark]]** _(article · informational)_ — Pairs each record with a JSON schema and ground-truth answer and reports that models achieve near-perfect schema compliance yet the best Value Accuracy is only 83.0% text, 67.2% image, 23.7% audio, exposing a 15–25 point schema-compliance-vs-value-accuracy gap ⟨§6.2; §6.4–6.6, Table 8⟩
- **[[idp-accelerator]]** _(article · informational)_ — Its Extraction Module processes documents as images through multimodal LLMs to generate structured JSON conforming to user-defined schemas, each field localized by bounding box, using few-shot learning without fine-tuning; reports best RealKIE-FCC extraction of 0.7991 (Claude Sonnet 4.5, OCR+Image) ⟨Key technique points; Experimental evaluation⟩
- **[[scair]]** _(article · informational)_ — Conditions an agent on the KG schema, injecting schema-conditioned structural priors and enforcing schema-aware traversal; argues generic agentic designs that do well on public benchmarks "fail to generalize" to dense enterprise KGs and reports SCAIR at 35.14 Accuracy vs 25.27 for the strongest baseline G-Retriever ⟨Abstract / §4; Table 1⟩

## Where sources differ
The sources place the schema at different points in the pipeline. [[extractbench]] and [[structured-output-benchmark]] treat the schema as a fixed evaluation contract and score how faithfully values fill it, with [[structured-output-benchmark]] emphasizing that compliance and value correctness diverge. [[schemarag]] treats a large schema as itself a retrieval problem, pruning it before extraction. [[idp-accelerator]] embeds schema conformance in a multimodal production module, while [[scair]] conditions a graph-traversal agent on a KG schema rather than a document schema. They also differ on where difficulty concentrates: [[extractbench]] locates it in long documents and enormous tables, [[schemarag]] in schema size, and [[scair]] in enterprise-graph density and generalization. Note [[extractbench]] is vendor-authored (runllama.ai, evaluating its own LlamaExtract) and [[idp-accelerator]] is AWS-affiliated; their comparative rankings are the papers' own.

## See also
[[structured-output-generation]] · [[schema-based-vs-schema-free-construction]] · [[agentic-extraction]] · [[entity-relation-extraction]] · [[llm-kg-construction]] · [[document-metadata-extraction]]
