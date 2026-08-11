---
title: "CUAD (Contract Understanding Atticus Dataset)"
type: entity
subtype: dataset
aliases: []
tags: [doc-processing]
concepts: ["[[contract-clause-extraction]]"]
sources: ["[[cuad]]"]
updated: 2026-08-10
---

# CUAD (Contract Understanding Atticus Dataset)

## What it is
CUAD is an expert-annotated NLP dataset for legal contract review, built with dozens of legal experts from The Atticus Project. Its task is to highlight the salient clauses of a contract that warrant human review, framed as extractive span identification.

## Key facts
- It is an expert-annotated legal contract-review dataset with over 13,000 annotations across 41 label categories ⟨[[cuad]] Abstract / §3⟩.
- It contains 510 contracts and 13,101 labeled clauses spanning 25 contract types, with contracts collected from the U.S. SEC's EDGAR system ⟨[[cuad]] §3 Dataset Statistics / Contract Sources / Table 3⟩.
- The task is to highlight salient contract clauses for review by extracting relevant text spans (start/end token positions) per label category ⟨[[cuad]] Abstract / §3 Task Definition⟩.
- Labeled clauses make up only about 10% of each contract on average — a "needles in a haystack" extraction problem ⟨[[cuad]] §3 Dataset Statistics⟩.
- A conservative estimate of the dataset's pecuniary value is over $2 million, reflecting the 70-100 hours of annotator training and multi-pass expert verification behind it ⟨[[cuad]] §1⟩.

## Relations
- Realizes: [[contract-clause-extraction]]
- Defined in: [[cuad]]
- Created by: [[org-atticus-project]]

## See also
[[contract-clause-extraction]] · [[document-element-classification]] · [[cuad]]
