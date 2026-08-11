---
title: "Fact-Grounded Question Generation"
type: concept
aliases: []
tags: [graph-rag]
related: ["[[llm-kg-construction]]", "[[entity-relation-extraction]]", "[[retrieval-augmented-generation]]"]
updated: 2026-08-10
---

# Fact-Grounded Question Generation

## What it is
Fact-grounded question generation is the automatic creation of question–answer pairs whose answers are anchored to specific facts extracted from a source corpus, so each generated question is verifiably answerable (or, by design, unanswerable) from that corpus. In a KG-plus-retrieval setting it selects entities, retrieves associated chunks, extracts the grounding facts, and formulates questions whose ground-truth answers are those facts — producing evaluation data aligned to the same corpus the retrieval system uses.

## How sources treat it
- **[[all-relations-rome]]** _(article · informational)_ — Phase 2 (QA generation) pre-defines question configurations and persona specifications, selects entities, retrieves associated chunks, extracts facts, formulates a base question, and reformulates it per persona ⟨§4.2⟩
- **[[all-relations-rome]]** _(article · informational)_ — An LLM fact extractor selects one or more facts from the retrieved chunks, framed by the question configuration so each fact corresponds to the specified entity and relations rather than an unrelated chunk fact ⟨§4.2.3⟩
- **[[all-relations-rome]]** _(article · informational)_ — A base question is generated that requires the extracted facts to answer, with the fact as ground-truth answer, then reformulated across three persona expertise levels (novice, intermediate, expert) to produce variants ⟨§4.2.4, Table 2⟩
- **[[all-relations-rome]]** _(article · informational)_ — Question configurations span question type (factoid vs open), relation (entity vs relation), complexity (single vs double), persona, and existent (in vs not in dataset), the last enabling evaluation of retrieval precision on unanswerable questions ⟨§4.2.1, Table 1⟩
- **[[all-relations-rome]]** _(article · informational)_ — The instantiated ARLtR dataset provides 8,400 QA pairs — 6,000 grounded in KG entities and 2,400 concerning entities or facts not present — enabling evaluation of retrieval precision on unanswerable questions ⟨§5.3⟩

## Where sources differ
Only [[all-relations-rome]] treats fact-grounded question generation, so there is no cross-source disagreement to surface. The source presents it as one half of a unified framework (paired with KG creation over the shared corpus) and describes the configuration axes and persona reformulation descriptively, without comparing the approach to alternative QA-generation methods.

## See also
[[llm-kg-construction]] · [[entity-relation-extraction]] · [[retrieval-augmented-generation]]
