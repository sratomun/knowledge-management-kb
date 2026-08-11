---
title: "Evidence-grounded generation"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[provenance]]", "[[precise-retrieval]]"]
updated: 2026-08-10
---

# Evidence-grounded generation

## What it is
Evidence-grounded generation is the practice of producing answers that are tied to, and traceable back to, specific retrieved sources — so a reader (or auditor) can check each claim against the evidence that supports it. It goes beyond retrieval-augmented generation's use of context by making the linkage explicit: citations, source-and-definition triples, or verbatim spans accompany the output. The aim is credibility and verifiability, particularly in high-stakes domains where distorted or unsupported statements carry real cost.

## How sources treat it
- **[[medical-graph-rag]]** _(article · informational)_ — links each RAG entity to a source entity and a dictionary entity as a [RAG entity, source, definition] triple, which the authors say makes responses traceable to sources and definitions ⟨§2.1⟩
- **[[medical-graph-rag]]** _(article · informational)_ — reports human evaluation (7 clinicians + 5 laypersons) rating the system higher notably in citation precision/recall and understandability, which the authors attribute to responses being more source-based ⟨§3⟩
- **[[legalbench-rag]]** _(article · informational)_ — argues that precise retrieved results let the LLM generate citations and let a human-in-the-loop quickly verify claims, whereas imprecise large contexts lead LLMs to forget or hallucinate ⟨Abstract; §1⟩

## Where sources differ
The two sources ground generation at different points in the pipeline. [[medical-graph-rag]] builds grounding into the *knowledge structure* — triple links from content to authoritative vocabularies and literature — so traceability is a property of the graph itself, and it reports clinician-rated citation quality as evidence. [[legalbench-rag]] locates grounding upstream in *retrieval precision* — tight snippets that make citation and human verification feasible — and does not itself construct a grounding graph. One treats grounding as constructed provenance in the index; the other as a downstream benefit of precise retrieval. Both papers' comparative results are attributed to their authors on their own pages.

## See also
[[provenance]] · [[precise-retrieval]]
