---
title: "Graph Retrieval-Augmented Generation: A Survey"
type: source
kind: article
authority: informational
subtype: framework
aliases: ["Graph RAG survey (Peng et al.)"]
publisher: "Peking University / Zhejiang University / Ant Group"
url: https://arxiv.org/abs/2408.08921
version: "arXiv:2408.08921v2 [cs.AI]"
published: 2024-08
effective_from: 2024-08
effective_to: ongoing
status: current
tags: [graph-rag]
concepts: ["[[retrieval-augmented-generation]]", "[[graphrag]]", "[[global-vs-local-search]]", "[[entity-relation-extraction]]"]
updated: 2026-08-10
---

# Graph Retrieval-Augmented Generation: A Survey

## Scope & purpose
The first comprehensive survey of GraphRAG methodologies, by Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, and Siliang Tang (Peking University, Zhejiang University, Ant Group, Renmin University, Rutgers) ⟨p.1 authors/abstract⟩. It argues that conventional Retrieval-Augmented Generation (RAG) mitigates LLM hallucination, missing domain knowledge, and outdated information by referencing an external knowledge base, but fails to capture the structured relationships among entities; GraphRAG addresses this by retrieving relational knowledge from a pre-constructed graph database ⟨§Abstract; §1⟩. The paper formalizes a universal GraphRAG workflow, surveys core technologies and training methods at each stage, and reviews downstream tasks, benchmarks, application domains, evaluation, industrial systems, and future directions ⟨§Abstract; §1⟩. Written for researchers and practitioners building LLM knowledge systems; a companion repository is maintained at github.com/pengboci/GraphRAG-Survey ⟨§Abstract⟩.

## Structure
- §1 Introduction — LLM limitations, RAG, and three shortcomings of traditional RAG (neglecting relationships, redundant information, lacking global information) that motivate GraphRAG
- §2 Comparison with related techniques — GraphRAG vs. RAG, LLMs on Graphs, and Knowledge Base Question Answering (KBQA)
- §3 Preliminaries — Text-Attributed Graphs (TAGs), Graph Neural Networks (GNNs), and Language Models
- §4 Overview of GraphRAG — formal problem definition and the three-stage workflow: Graph-Based Indexing (G-Indexing), Graph-Guided Retrieval (G-Retrieval), Graph-Enhanced Generation (G-Generation)
- §5 Graph-Based Indexing — graph data (open knowledge graphs vs. self-constructed) and indexing methods (graph, text, vector, hybrid)
- §6 Graph-Guided Retrieval — retriever types, retrieval paradigms, retrieval granularity, and retrieval enhancement
- §7 Graph-Enhanced Generation — generators (GNNs, LMs, hybrid), graph formats (graph languages, graph embeddings), and generation enhancement (pre/mid/post)
- §8 Training — training-free vs. training-based strategies for retriever, generator, and joint training
- §9 Applications and Evaluation — downstream tasks, application domains, benchmarks and metrics, and industrial GraphRAG systems
- §10 Future Prospects — dynamic graphs, multi-modality, scalable retrieval, graph foundation models, lossless compression, standard benchmarks, broader applications
- §11 Conclusion; References; the running example throughout uses an art-history query (Monet → Impressionism → Picasso/Cubism)

## Key points
- The survey formalizes GraphRAG as a three-stage workflow — Graph-Based Indexing (G-Indexing), Graph-Guided Retrieval (G-Retrieval), and Graph-Enhanced Generation (G-Generation) — and organizes its taxonomy of techniques and training methods around these stages ⟨§Abstract; §4⟩
- It identifies three limitations of traditional RAG that GraphRAG targets: neglecting relationships between interconnected texts, redundant information causing the "lost in the middle" problem, and lacking global information needed for tasks such as Query-Focused Summarization (QFS) ⟨§1⟩
- Unlike text RAG, GraphRAG retrieves graph elements carrying relational knowledge — nodes, triples, paths, or subgraphs — from a pre-constructed graph database, and treats GraphRAG as a branch of RAG that retrieves from graph databases rather than a text corpus ⟨§1; §2.1⟩
- Graph data is represented uniformly as Text-Attributed Graphs (TAGs), where nodes and edges carry textual attributes; knowledge graphs are one typical kind of TAG, with entities as nodes and relations as edges ⟨§3.1⟩
- The process is defined formally as finding the answer that maximizes p(a | q, G), decomposed via a graph retriever p_θ(G | q, G) and an answer generator p_φ(a | q, G), approximated by extracting an optimal subgraph G* because the number of candidate subgraphs grows exponentially with graph size ⟨§4, Eq. 3–6⟩
- G-Indexing constructs or selects a graph database aligned to the task and builds indices on it; graph databases originate from public/open knowledge graphs (general, e.g. Wikidata, Freebase, DBpedia, YAGO; and domain, e.g. CMeKG, CPubMed-KG) or from self-constructed graph data built from documents, tables, and other sources ⟨§5.1⟩
- Indexing methods are categorized as graph indexing (preserves full structure for BFS/shortest-path search), text indexing (converts graph data to textual descriptions for sparse/dense retrieval), vector indexing (embeddings for fast search), and hybrid indexing that combines them ⟨§5.2⟩
- Retrievers are categorized by underlying model into non-parametric (heuristic/graph-search, efficient but untrained), LM-based (strong language understanding, higher cost), and GNN-based (encode graph structure and score granularities), with many methods combining them in multi-stage retrieval ⟨§6.1⟩
- Retrieval paradigms are once retrieval (single pass, low latency), iterative retrieval (subdivided into non-adaptive and adaptive, where the model itself decides when to stop), and multi-stage retrieval that interleaves different retrievers and even generation steps ⟨§6.2⟩
- Retrieval granularity spans nodes, triplets, paths, subgraphs, and hybrid granularities; the survey notes boundaries between these are not sharp (subgraphs comprise paths, paths comprise triplets) and granularity choice trades retrieval content against efficiency ⟨§6.3⟩
- Retrieval enhancement splits into query enhancement (query expansion and query decomposition) and knowledge enhancement (knowledge merging and knowledge pruning, the latter via (re)ranking-based and LLM-based approaches) ⟨§6.4⟩
- G-Generation selects generators by task: GNNs and discriminative LMs for discriminative tasks, generative LMs (encoder-decoder / decoder-only) for generative tasks, and hybrid GNN+LM models in cascaded or parallel paradigms ⟨§7.1⟩
- Because LMs cannot ingest non-Euclidean graphs directly, retrieved graph data is converted via graph languages (adjacency/edge tables, natural language, code-like forms such as GML/GraphML, syntax trees, node sequences) or graph embeddings; good graph languages should be complete, concise, and comprehensible ⟨§7.2⟩
- Generation enhancement is grouped by stage into pre-generation (semantically enriching retrieved data), mid-generation (e.g. constrained decoding to keep outputs within KB classes/relations), and post-generation (integrating multiple generated responses) enhancement ⟨§7.3⟩
- Training methods are split into training-free (prompt-driven, common with closed-source LLMs like GPT-4) and training-based (supervised fine-tuning, distant supervision, reinforcement learning), covering separate training of retriever and generator plus joint/alternating training ⟨§8⟩
- Downstream tasks include KBQA, commonsense QA, entity linking, relation extraction, fact verification, link prediction, dialogue, and recommendation; application domains include e-commerce, biomedical, academic, literature, and legal; industrial systems named include Microsoft GraphRAG, NebulaGraph, Ant Group, and Neo4j's NaLLM and LLM Graph Builder ⟨§9.1; §9.2; §9.4⟩
- Future research directions include dynamic/adaptive graphs, multi-modal integration, scalable retrieval over billion-entity graphs, combination with graph foundation models, lossless compression of retrieved context, standard benchmarks, and broader application domains (healthcare, finance, legal/compliance, smart cities/IoT) ⟨§10⟩

## Concepts & entities covered
Concepts: [[retrieval-augmented-generation]] · [[graphrag]] · [[global-vs-local-search]] · [[entity-relation-extraction]]
Entities: —
