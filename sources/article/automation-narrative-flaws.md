---
title: "Flaws in the LLM Automation Narrative"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Flaws in the LLM Automation Narrative"]
publisher: "George Perrett; Javae Elliott; Jennifer Hill; Marc Scott (New York University)"
url: https://arxiv.org/abs/2606.11166
version: "arXiv:2606.11166v1"
published: 2026
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[benchmark-validity]]", "[[human-parity]]", "[[realistic-performance-expectations]]"]
entities: []
updated: 2026-08-10
---

# Flaws in the LLM Automation Narrative

> This paper IS a critique of human-parity claims. All limitation, comparison, and "LLMs do not match experts" claims below are reported as the authors' arguments and findings, not as KB conclusions. The KB never declares who is better.

## Scope & purpose
A June 2026 arXiv paper (stat.OT) by George Perrett, Javae Elliott, Jennifer Hill, and Marc Scott (New York University) that argues the widely repeated claim that "LLMs perform at the level of human experts on knowledge-economy tasks" rests on a benchmarking paradigm the authors consider methodologically flawed ⟨arXiv:2606.11166, Abstract, §1⟩. The authors contend that popular benchmarks (they cite OpenAI's GDPVal) measure average accuracy on standardized datasets while ignoring benchmark contamination, response variance, and the magnitude of errors — qualities they argue are decisive in high-stakes deployment ⟨arXiv:2606.11166, Abstract, §1.1⟩. To make the case empirically they build a novel benchmark task (writing analysis code for the 2016 ACIC causal-inference data competition) and compare a frontier LLM against human PhD experts on continuous metrics ⟨arXiv:2606.11166, Abstract, §2⟩.

## Structure
Organised as: §1 Introduction, including §1.1 Limitations of Existing LLM Benchmark Evaluations (contamination, stochasticity, binary criteria); §2 Methods (§2.1 the 2016 ACIC competition and experimental design, §2.2 performance measures); §3 Results (RMSE, standardized bias, coverage/interval length, variance); §4 Discussion (objections, prompt engineering, implications); Appendices A–B (prompt and the 20 generated scripts) ⟨arXiv:2606.11166, §1–§4⟩.

## Key points
- The authors frame the "automation narrative" as developer claims that LLMs can replace or match expert human labor — citing an Anthropic estimate that LLMs could theoretically replace up to 94% of computer/math work and ~90% of finance, management, law, and administration work, and OpenAI's GDPVal claim that ChatGPT 5.2 performs at or above human workers 74.9% of the time — and argue these claims generalise benchmark scores into broad expert-equivalence assertions ⟨arXiv:2606.11166, §1⟩
- The paper identifies benchmark contamination as "perhaps most fundamental": when questions/answers leak into training data, high scores no longer indicate expertise; the authors cite a contamination-controlled benchmark on which frontier LLMs answered only 10% of questions correctly while human experts answered 90% ⟨arXiv:2606.11166, §1.1⟩
- The authors argue two further benchmark limitations: stochasticity (LLM output varies across instantiations even at low temperature, and one correct answer does not guarantee the next), and strictly binary scoring that records correct/incorrect but ignores the magnitude of errors, which they argue is critical when a catastrophic error (e.g. deleting a production database) is far more consequential than a minor one ⟨arXiv:2606.11166, §1.1⟩
- The paper attributes the benchmark-vs-deployment gap to these limitations, citing an MIT NANDA pilot study reporting that 95% of industry LLM rollouts produced no return on investment ⟨arXiv:2606.11166, §1.1⟩
- Study design: the authors ran ChatGPT Codex 5.2 twenty times to generate independent analysis scripts for the 2016 ACIC competition (7,700 datasets, private/unreleased participant code to limit contamination), giving each run the same prompt human contestants received, and compared results against 9 human PhD-statistician teams plus historical strawman and post-hoc submissions ⟨arXiv:2606.11166, §2.1⟩
- The authors selected ChatGPT Codex 5.2 specifically because OpenAI is the only developer to explicitly claim PhD-expert-level intelligence for its models and because that model is optimized for programming/statistical tasks ⟨arXiv:2606.11166, §2⟩
- Reported result: 3 of the 20 scripts (15%) failed to run; across RMSE, standardized bias, and interval coverage/length the authors report human experts performed better on average and with markedly less variability ⟨arXiv:2606.11166, §3⟩
- The paper reports catastrophic-magnitude LLM errors: five scripts produced RMSE values exceeding 100 billion standard deviations of the outcome (for reference, 0.8 SD is a "large" effect size), which the authors attribute to subtle conceptual errors such as ignoring functional-form instructions or reweighting incorrectly ⟨arXiv:2606.11166, §3⟩
- The authors report a variance contrast they treat as the central liability: human submissions had standard deviations of .029 (RMSE), .012 (standardized bias), and 1.76 (interval length), while ChatGPT Codex 5.2 submissions had standard deviations in the billions (58,171,865,734.93 for RMSE), driven by five scripts that catastrophically failed rather than one outlier ⟨arXiv:2606.11166, §3⟩
- The paper reports a split by approach: 8 of 20 submissions (40%) used the grf R package for causal forests and produced RMSE/bias nearly as good as the best humans (though with poorer coverage), while IPTW/AIPTW submissions implemented from scratch performed particularly poorly — which the authors read as the LLM succeeding when a package removed the hard statistical work and failing when it had to implement methods itself ⟨arXiv:2606.11166, §3, §4⟩
- The authors preempt the prompt-engineering objection, arguing that better output would require substantial statistics/coding expertise from the prompt author and would reflect the human's expertise rather than the LLM's capacity ⟨arXiv:2606.11166, §4⟩
- The paper's stated conclusion is that ChatGPT Codex 5.2's performance is not equivalent to their ensemble of PhD-level experts, and that consistency and reliability are prerequisites of expertise that current benchmark-accuracy metrics fail to capture; the authors argue benchmark evaluations should measure response variance and error magnitude, not just accuracy ⟨arXiv:2606.11166, §4⟩
- The authors hedge that their study evaluates a single frontier model (out-of-the-box, one prompt) on one task, and note the eight competitive causal-forest submissions as a genuine counter-consideration while maintaining that even the best LLM submissions fell short of the best human submissions and that the variance finding is troubling ⟨arXiv:2606.11166, §3, §4⟩

## Concepts & entities covered
Concepts: [[benchmark-validity]] · [[human-parity]] · [[realistic-performance-expectations]]
Entities: —
