---
title: "CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review"
type: source
kind: article
authority: informational
subtype: dataset
aliases: ["CUAD"]
publisher: "Hendrycks, Burns, Chen, Ball (UC Berkeley; The Atticus Project)"
url: https://arxiv.org/abs/2103.06268
version: "arXiv:2103.06268v2; NeurIPS 2021 Datasets and Benchmarks Track"
published: 2021-11
effective_from: 2021-11
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review

## Scope & purpose
CUAD (Contract Understanding Atticus Dataset) is a large, expert-annotated NLP dataset for legal contract review. It was created with dozens of legal experts from The Atticus Project to address the lack of a public large-scale dataset in a costly specialized domain. The task is to highlight the salient portions of a contract that a human should review, framed as extractive span identification. The paper (NeurIPS 2021 Datasets and Benchmarks Track) evaluates several Transformer models and finds performance promising but with substantial room for improvement.

## Structure
The paper covers: (1) introduction motivating automated contract review and its societal costs; (2) related work in legal NLP and NLP for specialized domains; (3) the dataset — definition of contract review, the 41 label categories, task definition, dataset statistics, contract sources, and labeling process; (4) experiments — task structure, metrics, models (BERT, RoBERTa, ALBERT, DeBERTa), training, and results including analyses by category, model size, and training-data size; (5) conclusion; and an appendix with special cases, contract-type breakdown, full label-category descriptions, and SQuAD 2.0 conversion details.

## Key points
- CUAD is a dataset for legal contract review created with dozens of legal experts from The Atticus Project, consisting of over 13,000 annotations; the task is to highlight salient portions of a contract important for a human to review ⟨arXiv:2103.06268, Abstract⟩.
- The dataset contains 510 contracts and 13,101 labeled clauses spanning 41 label categories across 25 different contract types ⟨arXiv:2103.06268, §3 Dataset Statistics / Table 3⟩.
- The 41 labels are broadly grouped into general information, "restrictive covenants," and "revenue risks" ⟨arXiv:2103.06268, §3 Labels⟩.
- For each label category, models extract the relevant clause spans by predicting start and end token positions, learning to highlight the portions of text lawyers should attend to ⟨arXiv:2103.06268, §3 Task Definition⟩.
- Labeled clauses make up only about 10% of each contract on average, and about 0.25% per individual label category — a "needles in a haystack" task ⟨arXiv:2103.06268, §3 Dataset Statistics⟩.
- Contracts were collected from the U.S. SEC's EDGAR system, which yields heavily negotiated contracts rich in clauses that are rare in the general population ⟨arXiv:2103.06268, §3 Contract Sources⟩.
- Quality control was extensive: law-student annotators underwent 70-100 hours of training, followed over 100 pages of annotation rules, and each annotation was verified by three additional annotators ⟨arXiv:2103.06268, §1 / §3 Labeling Process⟩.
- A conservative estimate of the dataset's pecuniary value is over $2 million (each of 9,283 pages reviewed at least four times at an assumed $500/hour) ⟨arXiv:2103.06268, §1⟩.
- The prediction task is formatted like SQuAD 2.0 extractive question answering, allowing an empty (no-answer) span, with a sliding window over long contracts ⟨arXiv:2103.06268, §4.1 / Appendix A.3⟩.
- Evaluation uses AUPR and Precision at 80%/90% Recall, with a highlighted span counted as a match when its Jaccard similarity to the ground truth is at least 0.5 ⟨arXiv:2103.06268, §4.1 Metrics⟩.
- Among evaluated models, DeBERTa-xlarge performs best (AUPR 47.8, Precision@80%Recall 44.0), far above BERT-base (8.2 Precision@80%Recall), showing the benchmark is difficult but improving with model design ⟨arXiv:2103.06268, §4.2 / Table 2⟩.
- Performance is strongly influenced by both model design and the amount of labeled training data, indicating that data is a major bottleneck for contract review ⟨arXiv:2103.06268, Abstract / §5 Conclusion⟩.

## Concepts & entities covered
Concepts: [[contract-clause-extraction]] · [[document-element-classification]]
Entities: [[cuad-dataset]] · [[org-atticus-project]]
