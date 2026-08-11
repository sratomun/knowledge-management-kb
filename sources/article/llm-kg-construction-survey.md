---
title: "LLM-Empowered Knowledge Graph Construction: A Survey"
type: source
kind: article
authority: informational
subtype: framework
aliases: ["LLM KG construction survey"]
publisher: "arXiv (Haonan Bian, Xidian University)"
url: https://arxiv.org/abs/2510.20345
published: 2025
status: current
tags: [graph-rag]
updated: 2026-08-10
---
# LLM-Empowered Knowledge Graph Construction: A Survey

## Scope & purpose

This survey by Haonan Bian (Xidian University), published as a conference paper at ICAIS
2025 (arXiv:2510.20345), reviews recent progress in LLM-empowered knowledge graph (KG)
construction. Its central claim is that the arrival of Large Language Models shifts KG
construction from rule-based and statistical pipelines toward language-driven, generative
frameworks, systematically reshaping the classical three-layered pipeline of ontology
engineering, knowledge extraction, and knowledge fusion. It first revisits traditional KG
methodologies to set conceptual foundations, then reviews emerging LLM-driven approaches
through two complementary lenses — schema-based and schema-free — before outlining future
research directions.

## Structure

The paper is organized as: Section 2 (Preliminaries) reviews the traditional three-layered
pipeline — ontology engineering, knowledge extraction, knowledge fusion — in the pre-LLM
era; Section 3 covers LLM-enhanced ontology construction, split into top-down (LLMs as
ontology assistants) and bottom-up (KGs for LLMs) paradigms; Section 4 presents LLM-driven
knowledge extraction, contrasting schema-based and schema-free methods; Section 5 discusses
LLM-powered knowledge fusion at schema level, instance level, and hybrid; Section 6
explores future directions; Section 7 concludes.

## Key points

- Conventional KG construction pipelines comprise three major components — ontology
  engineering, knowledge extraction, and knowledge fusion ⟨§1⟩.
- Traditional paradigms face three enduring challenges: scalability and data sparsity,
  expert dependency and rigidity, and pipeline fragmentation causing cumulative error
  propagation ⟨§1⟩.
- LLMs enable three key mechanisms for overcoming these bottlenecks: generative knowledge
  modeling, semantic unification through natural-language grounding, and instruction-driven
  orchestration of construction workflows ⟨§1⟩.
- In the pre-LLM era, ontologies were mainly hand-built by domain experts using tools such
  as Protégé and methodologies like METHONTOLOGY and On-To-Knowledge, offering rigor but
  limited scalability ⟨§2.1⟩.
- Semi-automatic ontology learning sought to derive ontological structures from textual
  corpora, but even frameworks such as NeOn struggled with ontology evolution, modular
  reuse, and dynamic adaptation ⟨§2.1⟩.
- Knowledge extraction evolved from brittle handcrafted rules to statistical and neural
  methods (BiLSTM-CRF, Transformers), yet remained constrained by data scarcity, weak
  generalization, and cumulative error propagation ⟨§2.2⟩.
- Knowledge fusion integrates heterogeneous sources by resolving duplication, conflict, and
  heterogeneity; its central subtask, entity alignment, decides whether entities from
  different datasets refer to the same real-world object ⟨§2.3⟩.
- LLM-enhanced ontology construction follows two complementary directions: a top-down
  approach using LLMs as ontology assistants, and a bottom-up approach where ontologies and
  KGs serve LLMs themselves ⟨§3⟩.
- In the top-down paradigm, LLMs act as co-modelers that translate natural-language
  specifications — competency questions, user stories, domain descriptions — into formal
  ontologies (typically OWL), with frameworks such as Ontogenia, CQbyCQ, LLMs4OL, and
  NeOn-GPT ⟨§3.1⟩.
- The bottom-up paradigm recasts the KG as dynamic infrastructure providing factual
  grounding and structured memory for LLMs, inducing schemas from data via frameworks such
  as GraphRAG, EDC (Extract–Define–Canonicalize), AdaKGC, and AutoSchemaKG ⟨§3.2⟩.
- LLM-driven knowledge extraction bifurcates into schema-based extraction — emphasizing
  normalization, structural consistency, and semantic alignment under explicit schema
  guidance — and schema-free extraction — prioritizing adaptability, openness, and
  exploratory discovery ⟨§4⟩.
- Schema-based extraction progresses from static, predefined ontological blueprints (e.g.
  KARMA, TBox-then-ABox pipelines) toward dynamic, adaptive schemas that co-evolve with
  extracted content (AutoSchemaKG, AdaKGC's schema-constrained decoding) ⟨§4.1⟩.
- Schema-free extraction unfolds along structured generative extraction (Chain-of-Thought
  prompting, AutoRE, ChatIE, KGGEN) and Open Information Extraction, which discovers all
  possible entity–relation–object triples without predefined types ⟨§4.2⟩.
- LLM-powered knowledge fusion divides into schema-level fusion (unifying the structural
  backbone), instance-level fusion (entity alignment, disambiguation, deduplication,
  conflict resolution), and hybrid frameworks that unify both in one workflow ⟨§5⟩.
- Schema-level fusion has moved from ontology-driven consistency to data-driven unification
  to LLM-enabled canonicalization, where LLMs generate natural-language definitions of
  schema components and compare them by vector similarity ⟨§5.1⟩.
- The survey identifies three future directions: KG-based reasoning for LLMs (structured
  KGs improving logical consistency and interpretability), dynamic knowledge memory for
  agentic systems (KG as evolving memory substrate, e.g. A-MEM, Zep), and multimodal KG
  construction integrating text, image, audio, and video ⟨§6⟩.
- Across all stages three overarching trends emerge: evolution from static schemas to
  dynamic induction, integration of pipeline modularity into generative unification, and a
  transition from symbolic rigidity to semantic adaptability ⟨§7⟩.

## Concepts & entities covered
Concepts: [[llm-kg-construction]] · [[ontology-learning]] · [[schema-based-vs-schema-free-construction]] · [[knowledge-fusion]] · [[entity-relation-extraction]]
Entities: —
