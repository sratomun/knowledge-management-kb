---
title: "Retrieval-Augmented Generation with Graphs (GraphRAG)"
type: source
kind: article
authority: informational
subtype: framework
aliases: ["GraphRAG survey (Han et al.)"]
publisher: arXiv
url: https://arxiv.org/abs/2501.00309
published: 2025
effective_from: 2025-01
effective_to: ongoing
status: current
tags: [graph-rag]
updated: 2026-08-10
---

# Retrieval-Augmented Generation with Graphs (GraphRAG)

## Scope & purpose

This survey reviews GraphRAG — retrieval-augmented generation (RAG) that retrieves from
graph-structured data sources rather than i.i.d. text or image corpora. It argues that
graphs, by their "nodes connected by edges" nature, encode heterogeneous and relational
knowledge that is a valuable external resource for RAG, but that the uniqueness of
graph-structured data (diverse formats, domain-specific relations) imposes design
challenges not present in conventional RAG. The paper proposes a unified GraphRAG
framework, reviews techniques for each component and across ten graph domains, and
outlines research challenges. It is preprint arXiv:2501.00309 (v2, Jan 2025), authored by
Haoyu Han, Yu Wang, Harry Shomer, Jiliang Tang, and collaborators from Michigan State
University, University of Oregon, Adobe, Amazon, Meta, Snap, and others.

## Structure

The survey is organized as: (1) an introduction motivating GraphRAG and contrasting
graph data with text/image data; (2) a holistic framework (§2) defining five components —
query processor, retriever, organizer, generator, and graph data source — with
representative techniques for each; (3) domain-specific reviews (§3–§9) across knowledge,
document, scientific, social, planning & reasoning, tabular, infrastructure, biological,
scene, and random graphs, each covering task applications ("when to retrieve"), graph
construction ("what to retrieve"), and component techniques ("how to retrieve"); and
(4) challenges and future work (§10) plus conclusion (§11).

## Key points

- GraphRAG augments generation by retrieving heterogeneous, relational knowledge from
  graph-structured sources, offering advantages over similarity-only RAG through
  graph-based ML (e.g. GNNs) and graph analysis (e.g. traversal search, community
  detection) ⟨arXiv 2501.00309, Abstract / §1⟩.
- The survey proposes a holistic GraphRAG framework of five components: query processor,
  retriever, organizer, generator, and graph data source, arranged as
  Q → processor → retriever → organizer → generator → answer ⟨arXiv 2501.00309, §2.1⟩.
- Three differences from conventional RAG drive dedicated designs: graph data is
  diverse-formatted (vs. unified), interdependent (vs. independent chunks), and
  domain-specific (vs. domain-invariant transferable semantics) ⟨arXiv 2501.00309, §1⟩.
- The query processor bridges text queries and graph sources via five techniques: named
  entity recognition, relational extraction, query structuration (to GQL such as Cypher,
  GraphQL, SPARQL), query decomposition, and query expansion ⟨arXiv 2501.00309, §2.3⟩.
- Retrievers are grouped into heuristic-based (entity linking, relational matching, graph
  traversal, graph kernels, domain expertise), learning-based (shallow embeddings like
  Node2Vec/DeepWalk and deep embeddings like GNNs), and advanced strategies ⟨arXiv 2501.00309, §2.4⟩.
- Unlike RAG's uniform "Text-in, Text-out" retrieval, GraphRAG retrieval spans
  Text-in/Graph-out, Graph-in/Text-out, and Graph-in/Graph-out workflows and must capture
  graph-structure signals that BM25/TF-IDF and dense text retrievers overlook ⟨arXiv 2501.00309, §2.4⟩.
- Advanced retrieval strategies include integrated retrieval (e.g. neural-symbolic,
  multimodal), iterative retrieval that follows causal/resource/temporal dependencies, and
  adaptive retrieval that adjusts reasoning depth or need for external knowledge ⟨arXiv 2501.00309, §2.4.3⟩.
- The organizer refines retrieved content through graph pruning (semantic, syntactic,
  structure-based, dynamic), reranking, graph augmentation (structure and feature), and
  verbalizing (linear and model-based) so it is consumable by the generator ⟨arXiv 2501.00309, §2.5⟩.
- Generators fall into three types: discrimination-based (GNNs, graph transformers for
  classification/regression), LLM-based (via verbalizing, embedding-fusion, or positional
  embedding-fusion), and graph-based generators (e.g. diffusion models for molecules) ⟨arXiv 2501.00309, §2.6⟩.
- Graph data sources are built by explicit construction (from predefined relations) or
  implicit construction (derived connections such as word co-occurrence or feature
  interaction), and represented as adjacency matrices, edge lists, adjacency lists, node
  sequences, or natural language ⟨arXiv 2501.00309, §2.7⟩.
- GraphRAG designs are specialized across ten domains: knowledge, document, scientific,
  social, planning & reasoning, tabular, infrastructure, biological, scene, and random
  graphs, each with distinct tasks, construction methods, and component techniques ⟨arXiv 2501.00309, §1 / §3–§9⟩.
- Knowledge graphs are constructed manually (e.g. WikiData, UMLS), by rule-based parsers
  (e.g. ConceptNet, Freebase), or by LLM-based extraction of entities and relations from
  documents (e.g. Graph-RAG, AutoKG) ⟨arXiv 2501.00309, §3.2⟩.
- Per-component challenges include how to construct graphs (granularity, disambiguation,
  multimodal and dynamic graphs), differentiating neural vs. symbolic knowledge and
  harmonizing internal/external knowledge in retrieval, balancing completeness vs.
  conciseness in the organizer, and correct prompting format / structural encoding for
  generation ⟨arXiv 2501.00309, §10.1–§10.4⟩.
- Treated as a system, GraphRAG raises challenges of cross-component integration,
  scalability, and trustworthiness — reliability, robustness, safety, privacy, and
  explainability — where relational structure adds risks absent in conventional RAG ⟨arXiv 2501.00309, §10.5⟩.
- Evaluation is complicated by the multi-component nature, motivating component-level,
  end-to-end, task/domain-specific, and trustworthiness benchmarks ⟨arXiv 2501.00309, §10.6⟩.
- The authors position this as the first survey dedicated to graph-structured data that
  specializes GraphRAG designs per domain, distinguishing it from prior RAG surveys that
  focus on i.i.d. data or review graph techniques only under a conventional RAG architecture ⟨arXiv 2501.00309, §1⟩.

## Concepts & entities covered
Concepts: [[retrieval-augmented-generation]] · [[graphrag]] · [[knowledge-fusion]] · [[entity-relation-extraction]]
Entities: [[graphrag-taxonomy]]
