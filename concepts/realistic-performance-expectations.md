---
title: "Realistic performance expectations"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[human-parity]]", "[[human-in-the-loop-verification]]", "[[llm-failure-modes]]"]
updated: 2026-08-10
---

# Realistic performance expectations

## What it is
Realistic performance expectations concern calibrating what LLM and agent systems actually deliver on real professional tasks — attending to the reported gap against experts, output variance and reliability, robustness under degraded conditions, and questions of human oversight — rather than reading a headline accuracy number as a promise of expert-equivalence. Sources ground these expectations in how models behave on economically-consequential, open-ended, or safety-critical work, and typically frame the gap between benchmark scores and deployment as the practical concern.

## How sources treat it
- **[[euroexec]]** _(article · informational)_ — reports the strongest model solving 56.9% of tasks against a generous passing bar and only barely surpassing 50% on the easiest question subset, with "Reasoning" the weakest rubric attribute across the board ⟨§4; §5.1⟩
- **[[onemillion-bench]]** _(article · informational)_ — reports many models reaching a moderate Expert Score (~45–50%) while Pass Rates stay much lower (often below ~25%), that web search amplifies strong models but regresses weak ones, and that pass@k rises while pass^k decays toward zero — capability gains alongside degrading reliability ⟨§4.2; §4.7⟩
- **[[occubench]]** _(article · informational)_ — reports completion falling from 67.5% in clean environments to 53.4% under implicit faults, reads this as separating clean-environment capability from deployment readiness, and argues organizations should select agents by industry rather than aggregate ranking ⟨§6.2; §6.1⟩
- **[[automation-narrative-flaws]]** _(article · informational)_ — argues consistency and reliability are prerequisites of expertise that accuracy metrics miss, citing an MIT NANDA pilot reporting 95% of industry LLM rollouts produced no return on investment alongside its catastrophic-error findings ⟨§1.1; §3⟩
- **[[medical-graph-rag]]** _(article · informational)_ — grounds expectations in a human panel (7 clinicians and 5 laypersons) that rated its graph-RAG framework higher on citation precision/recall and understandability, and reports state-of-the-art gains while stressing medicine's need for credible, source-based responses ⟨§3⟩

## Where sources differ
The sources frame realistic expectations from different angles: [[euroexec]] and [[onemillion-bench]] by shortfall against an expert bar, [[occubench]] by the robustness gap between clean capability and deployment, [[automation-narrative-flaws]] by variance, error magnitude, and rollout ROI, and [[medical-graph-rag]] by improvements validated through a human evaluation panel — a comparatively optimistic, source-based framing that still emphasizes high domain stakes. The KB records these as complementary lenses on expectation-setting, not a single forecast.

## See also
[[human-parity]]
[[human-in-the-loop-verification]]
[[llm-failure-modes]]
[[benchmark-validity]]
