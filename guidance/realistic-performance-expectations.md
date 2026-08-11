---
title: "Realistic Performance Expectations — Knowledge Management through an AI Lens"
subtitle: "Human baselines, LLM task performance, and failure modes — a neutral reference for conscious pipeline design"
updated: 2026-08-10
status: draft v1
---

# Realistic Performance Expectations — KM through an AI Lens

## Why this exists

Leaders often ask a knowledge-processing pipeline for **100% accuracy**. Two things are usually missed in that ask: there is rarely a 100%-accuracy *system* — human or machine — and there is even less often a genuine 100% *requirement*. The useful questions for designing a knowledge pipeline are therefore not "is it perfect?" but: **what does the human baseline actually look like, what do LLMs realistically deliver on this task, how do they fail, and given that, where do we place humans and guardrails?**

This reference answers those questions from the ingested literature (the KB `benchmarking` domain). It is **neutral**: every performance figure is the *cited study's* result under its own conditions, not a recommendation or a claim that one approach is better. It pairs with the [Knowledge Processing Playbook](./knowledge-processing-playbook.md) — the playbook says *how* to build each use case; this says *how well it can realistically work and where the humans go*.

## Part 1 — The measured human baseline is already well under 100%

The number a leader imagines as "human accuracy" is, wherever it has actually been *measured*, a band well below 100%. The table below collects the **quantitative human baselines** the ingested studies report — each is a real measured figure, alongside the best model on the same test. Note that every human number is itself sub-100%.

| Task | **Measured human performance** | Metric / how measured | Best LLM on same test | Source |
|---|---|---|---|---|
| European executive decision tasks (finance, legal, tax, tech) | **Human experts 92.4%** win rate · 74.24 rubric score · 94.9% checklist fulfillment | Expert-authored reference answers, blind-judged; 47 vetted experts, 4,000+ expert hours | best model 56.9% · 49.5 · 61.9% | [euroexec](../sources/article/euroexec.md) |
| Italian Bar exam | **Top human candidate 62 / 100** | National exam scoring criteria, blind Turing-test | Gemini 2.5 Pro 79, ChatGPT-5 65 (both > human) | [italian-legal-turing](../sources/article/italian-legal-turing.md) |
| Italian Judicial exam | **Top human 18 / 24** (legal analysis: human essay 14 / 21) | Examiner scoring | Gemini 2.5 Pro 21 / 24 (> human) | [italian-legal-turing](../sources/article/italian-legal-turing.md) |
| Italian Notary exam | **Humans pass** (only a small % of candidates pass annually) | National exam | **all LLMs fail** | [italian-legal-turing](../sources/article/italian-legal-turing.md) |
| Qualitative coding of educator messages | **Human–human agreement Jaccard 0.52** | Inter-annotator agreement, 3 trained coders | human–LLM 0.30; blind expert preferred human 51.5% vs LLM 48.5% (p=0.537) | [agreement-is-not-quality](../sources/article/agreement-is-not-quality.md) |
| Document-layout annotation | **Human inter-annotator ceiling ~82–83 mAP** | mAP@0.5-0.95 between annotators (DocLayNet, 80,863 pages) | best models ~10 points below the human ceiling | [docling](../sources/provider-doc/docling.md) |

Three things this table makes concrete:
- **Human performance is not 100%.** Trained coders agree ~half the time (0.52); the top Bar candidate scored 62/100; the human layout-annotation ceiling is ~82–83, not 100. Where a *human* task tops out at 62% or 0.52 agreement, that is the realistic ceiling — asking a pipeline for 100% there is asking for better-than-human.
- **The gap runs both ways.** LLMs *exceed* top humans on the Bar and Judicial exams, *fall well short* of experts on open-ended executive decisions (92.4% vs 56.9%), and *fail outright* on the notary planning exam — so there is no single "human vs AI" number; it is per task.
- **The human baseline itself is contested.** A blind expert preferred human and LLM output at indistinguishable rates and, for some codes, judged human *consensus* to encode a shared bias ([agreement-is-not-quality](../sources/article/agreement-is-not-quality.md)) — so "match the humans" is not automatically "be correct." See [inter-annotator-agreement](../concepts/inter-annotator-agreement.md), [human-baseline](../concepts/human-baseline.md).

(Where a use case below has *no* measured human figure, that is a genuine gap in the ingested literature, and the matrix says so rather than inventing one — e.g. help-desk resolution and rule-based eligibility are not measured against a quantified human score in this set.)

## Part 2 — Use-case × realistic expectation

Rows are the five use-case profiles; each cell reports the *literature's* human baseline, LLM performance, dominant failure mode, and the design implication that follows. Figures are the cited study's, under its conditions.

| Use case | **Measured human baseline** | LLM performance (reported) | Dominant failure mode | Design implication |
|---|---|---|---|---|
| [issue-resolution](../concepts/issue-resolution.md) | *No quantified human score in the ingested set* (KCS is methodology, not a benchmark); nearest proxy is occupational-task completion | Professional-task completion drops **67.5% → 53.4%** under implicit faults (missing/truncated data) ([occubench](../sources/article/occubench.md)) | **Evaluation illusion** — fluent answers that are not sound; automated judges can read 100% reliability where experts do not ([clexeval](../sources/article/clexeval.md)) | Self-serve on high-confidence known issues; route uncertain/novel to humans; measure deflection, not perfection |
| [obligation-lookup](../concepts/obligation-lookup.md) | **Top human 62/100** (Bar), **18/24** (Judicial), **14/21** (legal analysis) ([italian-legal-turing](../sources/article/italian-legal-turing.md)); expert-lawyer gold (CUAD) ([cuad](../sources/article/cuad.md)) | Some LLMs **exceed** those humans (Bar 79, Judicial 21/24) — *out-of-the-box, single prompt* ([italian-legal-turing](../sources/article/italian-legal-turing.md)); but snippet **retrieval precision is low** (best Precision@1 ~14%) ([legalbench-rag](../sources/article/legalbench-rag.md)) | Imprecise retrieval → hallucination when the wrong context is pulled ([legalbench-rag](../sources/article/legalbench-rag.md)) | Precise minimal-snippet retrieval + cite-to-clause + human verification of the cited span |
| [eligibility-determination](../concepts/eligibility-determination.md) | *Not separately measured* — the statute/rule is itself the deterministic ground truth a caseworker applies | Frontier LLMs score **100% on shallow rule scenarios but degrade sharply on three-level nested rules** ("A unless B unless C") — *exception-chain collapse*, failures are false negatives ([exception-chain-collapse](../sources/article/exception-chain-collapse.md)) | **Exception-chain collapse** on nested conditional logic ([exception-chain-collapse](../sources/article/exception-chain-collapse.md)) | Use LLMs to *extract* rules, not to *evaluate* them; deterministic rules-as-code execution for the decision ([openfisca](../sources/provider-doc/openfisca.md)) |
| [extraction-verification](../concepts/extraction-verification.md) | **Human inter-annotator ceiling ~82–83 mAP** on layout annotation ([docling](../sources/provider-doc/docling.md)); plus mandatory human review as the operational reference | Field-level extraction up to **87.27%** on long scanned KYC docs; best models sit **~10 points below** the human layout ceiling ([kyc-multistage-extraction](../sources/article/kyc-multistage-extraction.md), [docling](../sources/provider-doc/docling.md)) | OCR/terminology/currency errors; small tampered regions; sparse relevant pages ([kyc-multistage-extraction](../sources/article/kyc-multistage-extraction.md)) | Page-retrieval → compact-VLM extract → **mandatory human review** (already a regulatory step, not added cost) |
| [compliance-checking](../concepts/compliance-checking.md) | **Human experts 92.4%** win rate · 74.24 rubric · 94.9% checklist on executive decisions (4,000+ expert hours) ([euroexec](../sources/article/euroexec.md)) | Best model **56.9%** / 49.5 / 61.9% — LLMs **fall well short** ([euroexec](../sources/article/euroexec.md)); automated gap-detection F1 ~**87.7** on its own benchmark ([compliancenlp-gap-detection](../sources/article/compliancenlp-gap-detection.md)) | Falls short of expert judgment on open-ended, high-stakes decisions ([euroexec](../sources/article/euroexec.md)) | LLM-assisted gap *flagging*; expert adjudicates the decision |

## Part 3 — Cross-cutting truths for setting expectations

- **Parity is task-specific, not a global property.** The same models that matched top humans on legal argumentation *all failed* the notary exam, which requires goal-directed planning under strict constraints ([italian-legal-turing](../sources/article/italian-legal-turing.md)). "The LLM is at expert level" is never true in general — only per task. See [human-parity](../concepts/human-parity.md).
- **Headline benchmark scores overstate deployment performance.** Clean-environment capability and deployment readiness diverge (OccuBench's 67.5%→53.4% under faults) ([occubench](../sources/article/occubench.md)); one critique argues expert-parity claims rest on benchmark artifacts and cites the gap to real ROI ([automation-narrative-flaws](../sources/article/automation-narrative-flaws.md)). See [realistic-performance-expectations](../concepts/realistic-performance-expectations.md).
- **Variance matters as much as the mean.** Expert ensembles can score higher *and* with far less variance than a top model ([automation-narrative-flaws](../sources/article/automation-narrative-flaws.md)) — a pipeline decision should weigh worst-case, not just average, output.
- **On the hard extraction tasks specifically, "it parsed" overstates "it's right."** Structured-extraction benchmarks report **near-perfect schema compliance but best value accuracy only ~83% (text), ~67% (image), ~24% (audio)** — valid JSON with wrong leaf values ([structured-output-benchmark](../sources/article/structured-output-benchmark.md)). Complex tables are a standout weakness: flattening/serializing nested and multi-header tables loses the structure the answer needs ([astra-table-qa](../sources/article/astra-table-qa.md), [st-raptor](../sources/article/st-raptor.md)). And bolting on agentic reflection/memory bought ~+10 records for 7× the log volume in one study ([agentic-controllability-ie](../sources/article/agentic-controllability-ie.md)) — so budget expectations for the *extract* stage on value accuracy and failure mode, not schema-validity or "we added an agent." See [structured-output-generation](../concepts/structured-output-generation.md), [complex-table-understanding](../concepts/complex-table-understanding.md).

## Part 4 — Distrust the measurement itself (before you trust a number)

A benchmark number is only as good as the instrument that produced it. This is central to methodology: do not baseline anyone — human or model — on a number whose validity you have not checked.

- **LLM-as-judge is biased.** Reporting an LLM judge as a scalar accuracy hides systematic error; one judge showed raw preference **0.967 driven by answer position**, not quality — "prompting moves the criterion, not the resolution" ([llm-judge-dark-current](../sources/article/llm-judge-dark-current.md)). Inter-LLM judges agree with each other more than with humans ([llm-as-judge-bias](../concepts/llm-as-judge-bias.md)).
- **Benchmarks saturate.** Many lose discriminative power near the top (29/60 benchmarks highly saturated in one study) ([benchmark-saturation](../sources/article/benchmark-saturation.md)) — a high score on a saturated benchmark says little.
- **Benchmarks get contaminated.** Test data leaks into pretraining corpora at scale, inflating scores ([contamination-resistant](../sources/article/contamination-resistant.md)).
- **Agreement is not quality.** High inter-evaluator agreement can reflect shared bias rather than correctness ([agreement-is-not-quality](../sources/article/agreement-is-not-quality.md)); fluency can masquerade as soundness — the *evaluation illusion* ([evaluation-illusion](../concepts/evaluation-illusion.md)).

Practical rule: when a vendor or paper cites a single accuracy number, ask *which benchmark, judged how, and is it saturated or contaminated* before treating it as a baseline.

## Part 5 — What this means for KM pipeline design

Reading the above as design guidance (still neutral — these follow from the cited findings, they are not a house mandate):

1. **Set targets to the measured human band, not 100%.** Where the human task itself agrees ~0.5, that is the realistic ceiling; specify the *actual* accuracy the process needs (often far below 100%) rather than a reflexive 100%.
2. **Put humans where the failure modes are, not everywhere.** Nested-rule eligibility → deterministic execution + human exception handling; open-ended executive/compliance judgment → expert adjudication; high-volume extraction → the mandatory review that already exists.
3. **Separate extraction from decision.** LLMs are stronger at pulling structure from text than at evaluating multi-step rules over it (exception-chain collapse) — extract with the LLM, decide with code where determinism matters.
4. **Demand provenance so humans can verify fast.** Cite-to-span retrieval and evidence-grounded generation turn "trust the model" into "check the cited source," which is what makes human-in-the-loop affordable at scale ([legalbench-rag](../sources/article/legalbench-rag.md), [medical-graph-rag](../sources/article/medical-graph-rag.md)).
5. **Instrument your own evaluation.** Before trusting internal benchmark numbers, check the judge and the dataset for the biases above.

## Sources

Benchmarks & human baselines: [euroexec](../sources/article/euroexec.md), [onemillion-bench](../sources/article/onemillion-bench.md), [occubench](../sources/article/occubench.md), [profbench](../sources/article/profbench.md), [clexeval](../sources/article/clexeval.md), [italian-legal-turing](../sources/article/italian-legal-turing.md). Methodology critiques: [automation-narrative-flaws](../sources/article/automation-narrative-flaws.md), [agreement-is-not-quality](../sources/article/agreement-is-not-quality.md), [llm-judge-dark-current](../sources/article/llm-judge-dark-current.md), [benchmark-saturation](../sources/article/benchmark-saturation.md), [contamination-resistant](../sources/article/contamination-resistant.md). Re-lensed prior sources: [cuad](../sources/article/cuad.md), [docling](../sources/provider-doc/docling.md), [exception-chain-collapse](../sources/article/exception-chain-collapse.md), [medical-graph-rag](../sources/article/medical-graph-rag.md), [kyc-multistage-extraction](../sources/article/kyc-multistage-extraction.md), [legalbench-rag](../sources/article/legalbench-rag.md).

_Every figure above is the cited study's result under its stated conditions; this document reports and organizes them and does not adjudicate who is "better." The KB `benchmarking` domain index is the descriptive system of record._
