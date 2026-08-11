---
title: "Contract Clause Extraction"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-element-classification]]"]
updated: 2026-08-10
---

# Contract Clause Extraction

## What it is
Contract clause extraction is the identification and extraction of the legally salient portions of a contract — the specific clauses a reviewer must attend to — usually framed as locating spans of text belonging to defined clause categories. It is a specialized form of document element classification and span extraction applied to legal agreements, supporting automated or assisted contract review.

## How sources treat it
- **[[cuad]]** _(article · informational)_ — CUAD is a dataset for legal contract review with over 13,000 annotations whose task is to highlight the salient portions of a contract important for a human to review ⟨arXiv:2103.06268, Abstract⟩
- **[[cuad]]** _(article · informational)_ — Contains 510 contracts and 13,101 labeled clauses spanning 41 label categories across 25 different contract types, with models extracting the relevant clause spans by predicting start and end token positions ⟨arXiv:2103.06268, §3 Dataset Statistics / Table 3⟩
- **[[cuad]]** _(article · informational)_ — Frames the problem as a "needles in a haystack" task, since labeled clauses make up only about 10% of each contract on average and about 0.25% per individual label category ⟨arXiv:2103.06268, §3 Dataset Statistics⟩

## Where sources differ
Only one source treats this concept directly, so there is no divergence to report. [[cuad]] consistently frames contract clause extraction as extractive span identification over predefined clause categories, formatted like SQuAD 2.0 question answering with a no-answer option and evaluated with AUPR and Precision at fixed recall ⟨arXiv:2103.06268, §4.1 Metrics⟩.

## See also
[[document-element-classification]] · [[document-metadata-extraction]]
