---
title: "EURO-5K: When Does Domain Pretraining Matter? Benchmarking Transformers for EU Reporting Obligation Extraction"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["EURO-5K"]
publisher: "Koniaris, Kotronis, Giannini & Tsanakas (National Technical University of Athens)"
url: https://arxiv.org/abs/2606.02971
version: "arXiv:2606.02971v1 [cs.CL]"
published: 2026-06
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [knowledge-processing]
concepts: ["[[obligation-extraction]]", "[[obligation-lookup]]", "[[machine-readable-legal-norms]]"]
entities: ["[[euro-5k-benchmark]]"]
updated: 2026-08-10
---

# EURO-5K: When Does Domain Pretraining Matter? Benchmarking Transformers for EU Reporting Obligation Extraction

## Scope & purpose
A benchmarking study from the National Technical University of Athens that curates EURO-5K, a sentence-level corpus of reporting obligations from EU legislation, and uses it to ask when domain (legal) pretraining actually matters for extraction ⟨Abstract; §1⟩. The authors motivate the task by the scale of the EU's reporting burden — roughly 180K legal acts — and by the difficulty of distinguishing reporting obligations from structurally similar provisions, which requires specialised legal understanding ⟨§1⟩. They train and compare discriminative token-classification models (BERT-style) against generative span-extraction models (LLMs), under both full fine-tuning and parameter-efficient tuning, and release the dataset, trained models, and an interactive demo with RDF export ⟨Abstract; §1; §6⟩.

## Structure
- §1 Introduction — reporting-burden motivation, the three obligation types, and the field's missing prerequisites (datasets, models, methodologies)
- §2 Related work — legal NLP and domain adaptation, information-extraction paradigms, LLMs for legal tasks, parameter-efficient training
- §3 Methodology — task definition (Definition 1) and dataset curation from the AROLD corpus
- §4 Experimental setup — discriminative vs generative models, baselines, evaluation framework, cross-dataset design
- §5 Results and discussion — model performance, statistical significance, data-efficiency and domain-adaptation analysis, cross-dataset evaluation, explainability, sustainability
- §6 Practical applications — interactive web interface, REST API, and RRMV-compliant RDF export
- §7 Conclusions & future work; Appendices A–E (annotation examples, curation methodology, significance testing, prompts)

## Key points
- The paper frames reporting-obligation extraction as a supervised sentence-level task: given a legislative text, identify the sentences that mandate information submission from an entity to a regulatory authority for supervisory purposes ⟨§3.1, Eq. 1⟩
- Definition 1 defines a reporting obligation as a mandatory legal requirement for a regulated subject to submit specific information to a regulatory or oversight authority for supervision, enforcement, or regulatory coordination, explicitly excluding behavioural obligations, disclosure obligations, and non-supervisory peer coordination ⟨§3.1, Definition 1⟩
- Following Marcus and Thomadakis (2025), the authors distinguish three obligation types — reporting (submit data to authorities), behavioural (conduct activities), and disclosure (make information public) — and target only the reporting subclass ⟨§1; §3.1⟩
- EURO-5K contains 5,253 sentence-level examples — 1,751 reporting obligations (positives) and 3,502 non-obligations (negatives, including 532 hard negatives at 10.3%) — drawn from 136 EU legislative documents, at a 1:2 positive:negative ratio ⟨Abstract; §3.2; App. B.5⟩
- The dataset is curated from AROLD (the JRC's Annotation of Reporting obligations in EU Legislation dataset, 30,432 raw positive annotations) through a multi-stage pipeline: rule-based filtering, legal-aware resegmentation, LLM-assisted review (Claude Sonnet 4), dual-blind human validation (κ=0.613), and three rounds of model-driven refinement ⟨§3.2; App. B⟩
- Annotation applies a five-criteria framework — reporting action, mandatory language, target regulatory authority, information submission, and obligation primacy — with hard negatives targeting obligation-like language to prevent superficial pattern learning ⟨§3.2; App. B.2⟩
- The models compared are discriminative token classifiers (BERT-base, Legal-BERT) and generative span extractors (Mistral-7B, Saul-7B, Llama-3.1-8B), evaluated under full fine-tuning (FFT) and parameter-efficient tuning (LoRA for BERT, QLoRA for LLMs) ⟨§4.1; §4.2⟩
- The paper reports that fully fine-tuned generic and legal BERT models achieve similar performance (~0.89 F1) and that fine-tuned LLMs match encoder accuracy for sentence-level extraction ⟨Abstract; §5.1, Table 3⟩
- It reports Llama-3.1-8B (QLoRA) as achieving the highest F1 (0.891), narrowly surpassing discriminative FFT (Legal-BERT FFT 0.883), and states that Llama achieves statistical parity with the BERT-FFT models (p=0.08) ⟨§5.1, Table 3; §5.3⟩
- On domain adaptation the paper reports that legal pretraining offers only small, statistically non-significant gains for discriminative FFT (Legal-BERT vs BERT-base, +1.8 F1, p=0.31) and negligible benefit for generative models at 7B scale (Saul vs Mistral), concluding that systematic hyperparameter optimization lets generic models approach domain-adapted performance ⟨Abstract; §5.3; §5.6⟩
- The abstract nonetheless states that legal pretraining is clearly beneficial when adaptation capacity is constrained, reporting that parameter-efficient tuning of Legal-BERT outperforms its generic counterpart, and that legal pretraining accelerates early learning with minimal data ⟨Abstract; §5.5; §5.6⟩
- Learning-curve analysis reports that all approaches converge around 3K samples with diminishing returns thereafter, which the authors read as validating dataset sufficiency ⟨Abstract; §5.5⟩
- Cross-dataset evaluation on two external corpora reports that the models behave as specialised reporting-obligation extractors rather than generic regulatory classifiers, with 88.7–90.3% zero-shot recall on out-of-domain financial reporting obligations ⟨Abstract; §5.7, Tables 6–7⟩
- For practical deployment the paper describes an interactive web interface and REST API that produce RRMV-compliant RDF/Turtle export (aligned to the EC's Reporting Requirements Metadata Vocabulary) to populate regulatory knowledge bases, generating valid RDF for a reported 60–80% of detected obligations ⟨§6; §6.3⟩
- The authors propose a human-in-the-loop deployment workflow in which high-confidence predictions are provisionally accepted and lower-confidence cases referred for expert review, citing the models' 85–87% precision as reducing validation effort ⟨§6.4⟩

## Concepts & entities covered
Concepts: [[obligation-extraction]] · [[obligation-lookup]] · [[machine-readable-legal-norms]]
Entities: [[euro-5k-benchmark]]
