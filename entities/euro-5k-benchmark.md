---
title: "EURO-5K benchmark"
type: entity
subtype: benchmark
aliases: []
tags: [knowledge-processing]
published: 2026-06
effective_from: 2026-06
effective_to: ongoing
status: current
concepts: ["[[obligation-extraction]]"]
sources: ["[[euro-5k-obligation-extraction]]"]
updated: 2026-08-10
---

# EURO-5K benchmark

## What it is
EURO-5K (EU-Reporting-Obligations-5K) is a curated, sentence-level benchmark dataset for extracting reporting obligations from EU legislation. It supplies positive and hard-negative examples for training and evaluating discriminative and generative extraction models.

## Key facts
- It is a benchmark for extracting reporting obligations — mandatory requirements to submit information to a regulatory authority — from EU legislation ⟨[[euro-5k-obligation-extraction]] Abstract; §3.1⟩.
- It contains 5,253 sentence-level examples: 1,751 reporting obligations (positives) and 3,502 negatives, including 532 hard negatives (10.3%), at a 1:2 positive:negative ratio ⟨[[euro-5k-obligation-extraction]] §3.2; App. B.5⟩.
- The examples are drawn from 136 EU legislative documents ⟨[[euro-5k-obligation-extraction]] Abstract; §3.2⟩.
- It is curated from the JRC's AROLD corpus (30,432 raw positive annotations) via a multi-stage pipeline of rule-based filtering, legal-aware resegmentation, LLM-assisted review, dual-blind human validation (κ=0.613), and iterative model-driven refinement ⟨[[euro-5k-obligation-extraction]] §3.2; App. B⟩.
- Annotation follows a five-criteria framework — reporting action, mandatory language, target regulatory authority, information submission, and obligation primacy — operationalising Definition 1's notion of a reporting obligation ⟨[[euro-5k-obligation-extraction]] §3.1; App. B.2⟩.
- The authors release EURO-5K together with trained models and an interactive demo that provides explainability visualizations and RRMV-compliant RDF export ⟨[[euro-5k-obligation-extraction]] Abstract; §6⟩.

## Relations
- Realizes: [[obligation-extraction]]
- Defined in: [[euro-5k-obligation-extraction]]

## See also
[[obligation-extraction]] · [[obligation-lookup]] · [[machine-readable-legal-norms]] · [[euro-5k-obligation-extraction]]
