---
title: "De Jure (regulatory-rule extraction)"
type: entity
subtype: technique
aliases: ["Document Extraction with Judge-Refined Evaluation"]
tags: [knowledge-processing]
published: 2026
effective_from: 2026-04
effective_to: ongoing
status: current
concepts: ["[[obligation-extraction]]", "[[rules-as-code]]"]
sources: ["[[de-jure-regulatory-rules]]"]
updated: 2026-08-10
---

# De Jure (regulatory-rule extraction)

## What it is
De Jure (Document Extraction with Judge-Refined Evaluation) is a fully automated,
domain-agnostic pipeline that uses iterative LLM self-refinement to extract structured,
machine-readable rules from raw regulatory documents, requiring no human annotation,
domain-specific prompting, or annotated gold data ⟨abstract⟩.

## Key facts
- It operates in four sequential stages: normalization into structured Markdown, LLM-driven
  rule generation into a typed JSON schema, multi-criteria LLM-as-a-judge evaluation across 19
  dimensions, and iterative repair within a bounded regeneration budget ⟨abstract, §3⟩.
- Its extraction schema decomposes each rule unit into a nine-field statement: action, action
  object, method, conditions, constraints, exceptions, penalties, purpose, and verbatim source
  span ⟨§3.2⟩.
- It applies the design principle of hierarchical repair ordering — metadata and definitions
  are verified and repaired before rule units are evaluated — so that rule-level repair always
  operates on reliable upstream context ⟨§3, §3.3⟩.
- Repair regenerates a stage only when its average judge score falls below θ = 0.90, for at
  most r = 3 attempts, retaining the best-scoring output to guarantee monotonically
  non-decreasing quality ⟨§3.4⟩.
- The source paper reports that it generalizes without modification across SEC (finance), HIPAA
  (healthcare), and EU AI Act (governance) corpora, maintaining overall scores above 4.70/5.00
  ⟨§4.3, Table 3⟩.
- In the source paper's downstream compliance-QA-via-RAG comparison against Datla et al. (2025)
  on HIPAA, De Jure-grounded responses are reported as preferred by a judge LLM in 73.8% of
  cases at single-rule retrieval, rising to 84.0% at ten-rule retrieval ⟨§4.4, Table 4⟩.

## Relations
- Realizes / relates to: [[obligation-extraction]] · [[rules-as-code]]
- Defined in: [[de-jure-regulatory-rules]]

## See also
[[de-jure-regulatory-rules]]
