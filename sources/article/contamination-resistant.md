---
title: "LLM Benchmark Datasets Should Be Contamination-Resistant"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Contamination-Resistant Benchmarks"]
publisher: "Al-Lawati, Lucas, Lee & Wang (The Pennsylvania State University)"
url: https://arxiv.org/abs/2605.19999
version: "arXiv:2605.19999v1 [cs.LG]; ICLR 2026"
published: 2026
effective_from: 2026-05
effective_to: ongoing
status: current
tags: [benchmarking]
concepts: ["[[benchmark-contamination]]", "[[benchmark-validity]]"]
entities: []
updated: 2026-08-10
---

# LLM Benchmark Datasets Should Be Contamination-Resistant

## Scope & purpose
A position paper arguing that LLM benchmark datasets should be released in a contamination-resistant form — unlearnable during pretraining yet still usable for inference — because benchmark samples now leak so pervasively into pretraining corpora that scores increasingly reflect memorization rather than generalization ⟨Abstract; §1⟩. It documents contamination prevalence, formalizes a "contamination-resistant dataset" (CRD) with three required properties, grounds a construction in the training-inference asymmetry of the Transformer, and addresses cross-model interoperability ⟨Abstract; §2–4⟩. It closes with a call to the community to advance CRD methods, standardize anchor models, and integrate CRD validation into existing pipelines ⟨§7⟩.

## Structure
- §1 Introduction — contamination as an obstacle to fair evaluation; the position statement
- §2 Contamination-resistance: motivation and formalization — prevalence, unlearnable data, CRD definition (Def. 2.1) and three properties, evaluation framework
- §3 Transformer training/inference asymmetry — why releasing KV cache + penultimate hidden state supports inference but blocks training
- §4 Interoperability — near-term anchor-model subspace alignment (Cross-LoRA) and long-term model-agnostic relative representations
- §5 Discussion — how well irreversibility, equivalence, interoperability are realized; space complexity
- §6 Alternative views — data curation (private/dynamic benchmarking) and data refactoring (obfuscation/decontamination)
- §7 Conclusion

## Key points
- The paper's position is that benchmark datasets should be released in a contamination-resistant form that stays useful for evaluating models while being unlearnable during public release ⟨Abstract; §1 position statement⟩
- Benchmark dataset contamination is defined as benchmark samples being ingested into pretraining corpora, which the authors argue diminishes benchmarks' value as reliable measures of generalization and instead inflates accuracy by rewarding recall of pretraining data ⟨§1; §2.1⟩
- The paper reports contamination as widespread and rising over time, citing figures such as GPT-3 flagging over 90% of examples in some benchmarks, Llama 2 showing contamination in over 16% of MMLU, and multilingual audits up to 91.8%, with the effect growing with model scale ⟨§2.1, Fig. 1⟩
- It reports (via Zhang et al. 2024) that using a clean, non-public mirror of GSM8K can reduce accuracy by up to 13% on model families such as Mistral, illustrating inflation from contamination ⟨§1⟩
- Definition 2.1 defines a contamination-resistant dataset ϕ(D) as one that maintains inference utility (M(ϕ(D)) yields valid task performance) while being unlearnable (training steps on ϕ(D) fail to improve generalized performance) ⟨§2.3, Def. 2.1⟩
- CRDs must satisfy three properties: (1) Irreversibility — computationally/economically impractical to reconstruct plaintext D from ϕ(D); (2) Equivalence — M(ϕ(D)) ≈ M(D); (3) Interoperability — ϕ(D) can be mapped to a form usable by another arbitrary LLM ⟨§2.3⟩
- The construction exploits the Transformer training-inference asymmetry: training needs all raw tokens to compute per-position hidden states, whereas inference needs only the cached key-value pairs plus the penultimate-layer hidden state of the final token; releasing only {KV cache, penultimate hidden state, plaintext Y} therefore supports inference but not training ⟨§3, Eqs. 1–3⟩
- The paper argues generic "unlearnable data" perturbation methods (adversarial noise, shortcut learning, data poisoning) are largely incompatible with discrete text, because modern LLMs are robust denoisers and paraphrasing/back-translation removes crafted perturbations ⟨§2.2⟩
- For interoperability it proposes two paradigms: a near-term anchor-model approach using subspace alignment (building on Cross-LoRA's LoRA-Align/LoRA-Shift, computed only from model weights, not plaintext) and a long-term model-agnostic relative-representation approach projecting all models into a shared coordinate frame via anchor samples ⟨§4.2; §4.3⟩
- The interoperability argument is grounded in three representation-learning results the paper cites: the Platonic Representation Hypothesis (converging representations), Centered Kernel Alignment (measurable representational similarity), and model stitching (functionally interchangeable representations under linear maps) ⟨§4.1⟩
- On irreversibility the paper concedes KV-cache inversion attacks exist, but reports they are much less effective on modern Grouped-Query-Attention architectures than on Multi-Head Attention, and that lossy representations make exact plaintext recovery difficult; it lists defenses (noise, entropy perturbation, differential privacy, KV obfuscation like KV-Cloak) ⟨§5 (Property 1)⟩
- The paper notes CRDs suit benchmarks with structurally independent inputs/outputs (single-turn QA, classification, code generation, summarization) but are less compatible with multi-turn, agentic, adaptive, or trajectory-scored benchmarks ⟨§5 Benchmark Compatibility⟩
- On storage overhead it reports KV-cache release is manageable with compression — e.g., PyramidKV reduces a 100K-token LLaMA-2-7B cache from ~50GB toward ~350MB — citing evidence that retaining 12–20% (even 0.7%) of the cache preserves performance ⟨§5 Space Complexity, Fig. 4⟩
- Stated limitations: CRDs depend on the Transformer architecture and do not apply to non-Transformer models (e.g., Mamba), and behavior varies across model families, attention mechanisms, and positional-encoding choices ⟨§5 Limitations⟩
- The paper reviews alternative approaches descriptively and argues each has drawbacks: private benchmarking (bottlenecks, cost barriers, weight-sharing/API exposure), dynamic benchmarking (short-lived, rapidly re-ingested, complicates longitudinal comparison), lexical obfuscation (LLMs already trained on obfuscated formats), and decontamination/filtering (misses paraphrase/translation, does not scale to trillion-token corpora) ⟨§6.1; §6.2⟩

## Concepts & entities covered
Concepts: [[benchmark-contamination]] · [[benchmark-validity]]
Entities: —
