---
title: "Obligation extraction"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[machine-readable-legal-norms]]", "[[obligation-lookup]]"]
updated: 2026-08-10
---

# Obligation extraction

## What it is
Obligation extraction is the task of identifying, from legal or regulatory text, the passages that impose obligations and representing them in a structured form. It typically involves detecting mandatory-modality statements, classifying them (e.g. reporting vs. behavioural vs. disclosure; obligation vs. permission vs. prohibition), and decomposing each into components such as the obligated entity, the required action, conditions, and a source citation. The extracted obligations feed machine-readable legal-norm stores, obligation lookup, and compliance checking.

## How sources treat it
- **[[euro-5k-obligation-extraction]]** _(article · informational)_ — frames reporting-obligation extraction as a supervised sentence-level task and, following Marcus and Thomadakis (2025), distinguishes three obligation types — reporting, behavioural, and disclosure — targeting only the reporting subclass ⟨§1; §3.1⟩
- **[[euro-5k-obligation-extraction]]** _(article · informational)_ — compares discriminative token classifiers (BERT-base, Legal-BERT) against generative span extractors (Mistral-7B, Saul-7B, Llama-3.1-8B) under full and parameter-efficient fine-tuning, reporting ~0.89 F1 for fully fine-tuned BERT models and LLMs matching encoder accuracy ⟨§4.1; Abstract, §5.1, Table 3⟩
- **[[de-jure-regulatory-rules]]** _(article · informational)_ — extracts rule units into a typed schema whose nine-field decomposition includes action, conditions, constraints, exceptions, and penalties, using schema-driven generation that returns null for non-actionable sections to suppress non-normative passages ⟨§3.2⟩
- **[[de-jure-regulatory-rules]]** _(article · informational)_ — reports that Non-Hallucination is uniformly perfect (5.00) across all evaluated models and judges, which the authors attribute to schema-constrained extraction eliminating factual fabrication as a failure mode ⟨§4.2⟩

## Where sources differ
The sources scope obligation extraction differently. [[euro-5k-obligation-extraction]] narrows to a *single obligation subtype* (reporting) as a binary sentence-classification task with a five-criteria annotation framework and hard negatives, and its central question is when legal-domain pretraining helps. [[de-jure-regulatory-rules]] is *domain-agnostic and generative*, decomposing whole regulatory documents into a rich multi-field rule schema across finance, healthcare, and AI governance with no domain-specific prompting, and its central mechanism is judge-refined self-repair. One is a focused benchmark of a typed detection task; the other a broad extraction-and-QA pipeline. Their comparative model findings are attributed to their respective authors.

## See also
[[machine-readable-legal-norms]] · [[obligation-lookup]]
