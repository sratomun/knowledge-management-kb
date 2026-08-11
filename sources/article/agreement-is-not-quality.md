---
title: "Agreement Is Not Quality"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Agreement Is Not Quality"]
publisher: "Alex Liu; Lief Esbenshade; Michael Xiao; Victor Tian (University of Washington); Zachary Zhang; Kevin He (Colleague AI); Min Sun (University of Washington)"
url: https://arxiv.org/abs/2607.28890
version: "arXiv:2607.28890"
published: 2026
effective_from: 2026-07
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[inter-annotator-agreement]]", "[[human-baseline]]", "[[benchmark-validity]]", "[[llm-as-judge-bias]]"]
entities: []
updated: 2026-08-10
---

# Agreement Is Not Quality

> This paper IS a critique of treating human consensus as ground truth. All agreement, preference, and "human consensus can encode bias" claims below are reported as the authors' findings, not as KB conclusions. The KB never declares who is better.

## Scope & purpose
A July 2026 arXiv paper by Alex Liu, Lief Esbenshade, Michael Xiao, Victor Tian, and Min Sun (University of Washington) with Zachary Zhang and Kevin He (Colleague AI) that challenges the standard practice of evaluating LLM-assisted qualitative coding by its agreement with trained human coders — a practice that presumes human coding is the standard to approximate ⟨arXiv:2607.28890, Abstract, Introduction⟩. The authors argue this presumption fails in ways agreement metrics structurally cannot detect, and demonstrate it with a blind expert-verification protocol that judges human and LLM code sets symmetrically, without assuming either is ground truth ⟨arXiv:2607.28890, Abstract, Introduction⟩. The full-title subtitle is "Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth" ⟨arXiv:2607.28890, title⟩.

## Structure
Organised as: Introduction; four Research Questions (RQ1 agreement, RQ2 moderators, RQ3 blind verification, RQ4 division of labor); Related Work (LLM-assisted coding; evaluation without a gold standard); Methodology (data, 72-item codebook, human coding, LLM coding, analysis framework, blind verification protocol); Findings (RQ1–RQ4); Discussion; Limitations; Conclusion ⟨arXiv:2607.28890, Research Questions, Findings⟩.

## Key points
- The paper's core argument is that nearly all evaluations of LLM qualitative coding — optimistic and cautionary alike — measure quality as agreement with human coders, treating human coding as the reference; the authors argue this is compelling only when humans converge on a shared valid interpretation and breaks down when interpretations are contested or when human consensus reflects shared bias ⟨arXiv:2607.28890, Introduction, Related Work⟩
- Study design: five LLM systems (Claude Opus 4.8, Claude Haiku 4.5, Gemini 3.5 Flash, GPT-4o, GPT-5.5) and three trained human coders independently applied a 72-item hierarchical multi-label codebook to 2,560 K-12 educator messages, and an independent domain expert judged 855 anonymized pairwise comparisons of code sets blind to source ⟨arXiv:2607.28890, Abstract, Methodology⟩
- Reported agreement picture (RQ1): mean human-LLM Jaccard was 0.30 (range 0.23–0.34) versus human-human Jaccard of ~0.52 — a gap of ~0.22 that the authors note standard practice would read as inferior LLM coding ⟨arXiv:2607.28890, Abstract, RQ1⟩
- The authors report that LLM-LLM agreement (0.37–0.68) is comparable to human-human agreement and higher than human-LLM agreement, which they interpret as models sharing interpretive tendencies that differ systematically from human patterns rather than as stochastic noise (intra-model re-run kappa 0.871–0.995 exceeded the human-human baseline) ⟨arXiv:2607.28890, RQ1, Methodology⟩
- Central blind-verification finding (RQ3): among 555 Human-vs-LLM pairs with a decisive preference, the verifier preferred human coding in 51.5% and LLM coding in 48.5% of cases (binomial p = 0.537, a negligible effect) — i.e. no overall expert preference for human coding despite the large agreement gap ⟨arXiv:2607.28890, Abstract, RQ3, Discussion⟩
- The authors present this as the study's key epistemic point: when two sources disagree and no ground truth exists, deviation from a human coder cannot distinguish an LLM that codes poorly from one that codes differently but well; agreement metrics and expert quality judgments diverge in both directions ⟨arXiv:2607.28890, Introduction, Discussion⟩
- Bradley-Terry ranking of the eight verified sources: the best LLM (Claude Opus) occupies the top position with a confidence interval overlapping the best human coder (statistically indistinguishable), GPT-5.5 and Gemini Flash rank above two of the three human coders, while GPT-4o and Claude Haiku rank below — the authors read the interleaving as evidence that source type does not determine quality ⟨arXiv:2607.28890, RQ3, Discussion⟩
- The authors report that for several substantive codes human consensus encoded shared conservative bias the verifier rejected: e.g. ELA Skills Development (human-human agreement 0.48) was endorsed 61% of the time when an LLM applied it but only 30% when a human did; Entire Lesson Planning and Unit Planning showed the same pattern — two coders reliably agreeing while both, in the verifier's judgment, under-applying the code ⟨arXiv:2607.28890, Findings Pattern 2, Discussion⟩
- The paper reports four code-level patterns showing agreement does not predict quality: (1) high agreement confirms automatability; (2) high human-human agreement yet verifier prefers LLM; (3) low agreement yet LLM preferred (e.g. Inquiry and Deep Questions, 65% vs 23%); (4) low agreement and human strongly preferred (e.g. Tiered Scaffolding, 86% vs 27%) — the authors argue Patterns 2 and 3 make agreement alone insufficient to determine automatability ⟨arXiv:2607.28890, Findings RQ3, Figure 4⟩
- The authors argue model selection matters more than the human-vs-machine choice: the Bradley-Terry gap between the best and worst LLM exceeds the gap between the best LLM and the best human by a factor of ~14, so choosing a model on cost without instrument-specific evaluation could underperform human coding ⟨arXiv:2607.28890, Discussion⟩
- Reported division-of-labor classification (RQ4): 6 codes automatable (4 fully, 2 with light review), 16 LLM-assisted with confidence-based triage, 12 LLM-preferred (verifier endorses LLM over human), and 15 human-required (codes needing recognition of unstated pedagogical intent, endorsement ratios 2–5x favoring humans) ⟨arXiv:2607.28890, RQ4, Conclusion⟩
- The authors position their contribution against the LLM-as-judge literature: rather than using an LLM judge, they use a human domain expert to preserve domain authority, and note prior work (Norman et al. 2026) that LLM judges can show reliability without validity and that models can produce consistent-but-biased outputs standard metrics score as reliable ⟨arXiv:2607.28890, Related Work, Discussion⟩
- The paper's stated conclusion is that agreement-based evaluation alone cannot ground automation decisions and that high human-human agreement should not be treated as sufficient evidence that human coding is correct; the authors offer the blind, source-symmetric protocol as a transferable alternative ⟨arXiv:2607.28890, Conclusion, Implications for Practice⟩
- The authors hedge extensively: a single codebook on a single dataset, a single independent verifier (a panel would be stronger; a different expert might endorse the humans), a capability snapshot whose specific rankings will shift, and temperature-zero inference that leaves enhanced prompting unexplored — so the divergence findings show divergence is possible, not that human coding is systematically wrong ⟨arXiv:2607.28890, Limitations⟩

## Concepts & entities covered
Concepts: [[inter-annotator-agreement]] · [[human-baseline]] · [[benchmark-validity]] · [[llm-as-judge-bias]]
Entities: —
