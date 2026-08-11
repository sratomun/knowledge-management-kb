---
title: "Entity and Relation Extraction"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[llm-kg-construction]]", "[[schema-based-vs-schema-free-construction]]", "[[knowledge-fusion]]", "[[graphrag]]"]
updated: 2026-08-10
---

# Entity and Relation Extraction

## What it is
Entity and relation extraction is the task of reading text and emitting the entities it mentions together with the relationships (typically subject–predicate–object triples) among them. It is the core knowledge-extraction step that turns unstructured text into graph nodes and edges. LLM-based extractors do this by prompting — either extracting triplets directly or annotating entities first and then their relations.

## How sources treat it
- **[[graphrag-local-to-global]]** _(article · informational)_ — The LLM is prompted to extract instances of important entities and the relationships between them from each chunk, and to generate short descriptions for the entities and relationships; prompts can be tailored to a domain via few-shot exemplars ⟨arxiv 2404.16130, §3.1.2⟩
- **[[llm-kg-construction-survey]]** _(article · informational)_ — Knowledge extraction evolved from brittle handcrafted rules to statistical and neural methods (BiLSTM-CRF, Transformers), yet remained constrained by data scarcity, weak generalization, and cumulative error propagation ⟨§2.2⟩
- **[[all-relations-rome]]** _(article · informational)_ — Annotation uses an LLM-based entity tagger; relations are obtained either by directly extracting triplets or by a two-step process of entity annotation followed by relation extraction, the latter a chain-of-thought that improves accuracy for larger ontologies ⟨§4.1.3⟩
- **[[rag-with-graphs-survey]]** _(article · informational)_ — Knowledge graphs are constructed manually, by rule-based parsers, or by LLM-based extraction of entities and relations from documents (e.g. Graph-RAG, AutoKG) ⟨arXiv 2501.00309, §3.2⟩
- **[[graph-rag-survey]]** _(article · informational)_ — Lists relation extraction and entity linking among GraphRAG downstream tasks, alongside KBQA, fact verification, and link prediction ⟨§9.1; §9.2; §9.4⟩

## Where sources differ
The sources converge on LLM prompting as the current extraction method and are complementary in detail. [[graphrag-local-to-global]] and [[all-relations-rome]] give operational recipes (per-chunk prompting with descriptions; direct-triplet vs. two-step entity-then-relation via chain-of-thought). [[llm-kg-construction-survey]] situates LLM extraction in a historical arc from handcrafted rules through neural sequence models, noting persistent error propagation. [[rag-with-graphs-survey]] and [[graph-rag-survey]] frame extraction as one of several ways to build/consume a graph and as a named downstream task. No source ranks the approaches.

## See also
[[llm-kg-construction]] · [[schema-based-vs-schema-free-construction]] · [[knowledge-fusion]] · [[graphrag]]
