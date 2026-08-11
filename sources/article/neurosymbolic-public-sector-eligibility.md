---
title: "A Neuro-Symbolic Framework for Legal Accountability in Public-Sector AI"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Neuro-Symbolic eligibility"]
publisher: "Allen Daniel Sunny; Ido Sivan-Sevilla"
url: https://arxiv.org/abs/2512.12109
version: "arXiv:2512.12109v4"
published: 2025-12
effective_from: 2025-12
effective_to: ongoing
status: current
tags: [knowledge-processing]
concepts: ["[[eligibility-determination]]", "[[rules-as-code]]", "[[neuro-symbolic-rule-evaluation]]"]
entities: []
updated: 2026-08-10
---

# A Neuro-Symbolic Framework for Legal Accountability in Public-Sector AI

## Scope & purpose
A FAccT '26 paper by Allen Daniel Sunny (University of Maryland) and Ido Sivan-Sevilla (Hebrew University of Jerusalem / University of Maryland) on **explanation-level accountability** for automated public-benefit eligibility determination. It designs and implements a neuro-symbolic framework that uses an LLM to encode statutory eligibility rules into a formal ontology and satisfiability-based verification to assess whether benefits explanations comply with the governing law ⟨arXiv:2512.12109, Abstract⟩. The stated concern is that explanations issued to applicants function as legal justifications and sites of contestation, so they must be legally valid and not merely interpretable ⟨arXiv:2512.12109, §1⟩. Written for FAccT / public-sector-AI, ontology-engineering, and administrative-law audiences.

## Structure
Organised as: §1 Introduction (automation of welfare decisions, the accountability gap); §2 Literature Review (legal knowledge representation, ontology extraction, SMT, neuro-symbolic frameworks); §3 Methodology (data sources, four-stage architecture, ontology/TBox/ABox construction, solver); §4 CalFresh case study and empirical evaluation; §5 Discussion; §6 Limitations; §7 Conclusion ⟨arXiv:2512.12109, §1–§7⟩.

## Key points
- The authors argue explanation-level verification is a distinct and necessary complement to algorithmic auditing, shifting attention from model behaviour to the legal integrity of justificatory artifacts, and call for a shift "from interpretability to auditability" of public algorithms ⟨arXiv:2512.12109, Abstract, §1⟩
- The framework is demonstrated on California's SNAP program (CalFresh), whose determinations are governed by the Manual of Policies and Procedures (MPP) Division 63; the Notice of Action (NOA) is treated as the central accountability artifact ⟨arXiv:2512.12109, §3.1⟩
- The architecture has four stages: ontology construction, Terminological Box (TBox) encoding of case-invariant legal rules, Assertion Box (ABox) construction from a case's explanation and facts, and SMT-based joint satisfiability verification ⟨arXiv:2512.12109, §3.2⟩
- A SAT outcome means the explanation is coherent under the governing law and can function as a legally admissible justification; an UNSAT outcome means the explanation fails to justify the determination — the authors stress this does not mean the eligibility decision itself was wrong ⟨arXiv:2512.12109, §3.2, §3.6⟩
- On inconsistency the solver extracts an unsatisfiable core (a minimal conflicting constraint subset) and maps it back to the implicated MPP provisions, yielding a statute-grounded accountability signal rather than a binary verdict ⟨arXiv:2512.12109, §3.2, §3.6⟩
- Ontology construction adopts class naming and structural patterns from the LKIF-Core framework and uses the statute's own structure (eligibility dimensions: income, residency, citizenship, resources, student status) as the top-level class hierarchy ⟨arXiv:2512.12109, §3.3⟩
- Operative terms are extracted from statutory sections via named-entity recognition (noun→candidate class, verb→candidate relation), embedded with Qwen3-Embedding-8B, and merged above a cosine-similarity threshold of 0.85 to prevent duplicate concepts ⟨arXiv:2512.12109, §3.3⟩
- OpenAI's o1 is prompted to translate each statutory provision into a solver-ready logical rule stored with a citation to its source provision, preserving a direct link between formal constraints and legal authority ⟨arXiv:2512.12109, §3.4⟩
- The paper situates the work within the Rules as Code movement, which advocates encoding legislation as machine-executable specifications at the drafting stage ⟨arXiv:2512.12109, §2⟩
- The authors report that directed symbolic prompting (instructing the model to produce solver-compatible logic over a controlled vocabulary) has been shown to improve formalisation success rates, while unconstrained/undirected generation yields narratively plausible but semantically drifted outputs even from frontier models — positioning LLMs as extraction/translation components validated against symbolic constraints, not autonomous legal reasoners ⟨arXiv:2512.12109, §2⟩
- The authors report that formal verification reveals violations of statutory requirements even when explanations appear reasonable or complete to human readers ⟨arXiv:2512.12109, Abstract, §4.1⟩
- Evaluation used 50 administrative cases across five statutory eligibility dimensions, with a paired incoherent instance per case (inverted determination) for 100 total instances; overall SMT accuracy is reported as 0.977, with per-category localization F1 for UNSAT cases ranging from 0.51 (Income) to 0.83 (Citizenship) ⟨arXiv:2512.12109, §4.1.2, §4.2, Table 1⟩
- The worked San Diego single-person-household case shows the NOA "gross income exceeds the limit" translated (via §63-409.111) to Implies(GrossIncome > GrossIncomeLimit(HouseholdSize), Not(Applicant_Eligible)); the solver returns SAT for the termination and UNSAT when the determination is inverted to "eligible" ⟨arXiv:2512.12109, §4⟩
- Stated limitations: welfare law's open-textured standards and discretionary exceptions cannot be fully captured symbolically; effectiveness depends on explanations mapping to the controlled vocabulary; evaluation uses controlled single-law cases; unsatisfiable cores are not guaranteed unique; and the system is evaluated as a technical artifact, not a deployed workflow ⟨arXiv:2512.12109, §6⟩

## Concepts & entities covered
Concepts: [[eligibility-determination]] · [[rules-as-code]] · [[neuro-symbolic-rule-evaluation]]
Entities: —
