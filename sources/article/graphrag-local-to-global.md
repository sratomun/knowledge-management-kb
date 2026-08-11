---
title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["GraphRAG paper"]
publisher: "Microsoft Research"
url: https://arxiv.org/abs/2404.16130
version: "v2 (2025-02-19)"
published: 2024-04
effective_from: 2024-04
effective_to: ongoing
status: current
tags: [graph-rag]
concepts: ["[[graphrag]]", "[[retrieval-augmented-generation]]", "[[global-vs-local-search]]", "[[community-detection-summarization]]", "[[entity-relation-extraction]]", "[[llm-kg-construction]]"]
entities: ["[[microsoft-graphrag]]", "[[leiden-community-detection]]", "[[org-microsoft]]"]
updated: 2026-08-10
---

# From Local to Global: A Graph RAG Approach to Query-Focused Summarization

## Scope & purpose
A Microsoft Research paper (Edge, Trinh, Cheng, Bradley, et al.) proposing **GraphRAG**, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text ⟨arxiv 2404.16130, §Abstract⟩. It targets the failure of conventional retrieval-augmented generation (RAG) on *global* sensemaking questions directed at an entire corpus (e.g. "What are the main themes in the dataset?"), which the authors frame as a query-focused summarization (QFS) task rather than an explicit retrieval task ⟨arxiv 2404.16130, §Abstract⟩. Written for researchers and practitioners building LLM question-answering systems, using podcast-transcript and news-article corpora in the ~1 million token range as running examples.

## Structure
- §Abstract — problem framing (global vs. local questions), the two-stage graph-index approach, headline result
- §1 Introduction — vector RAG vs. sensemaking; GraphRAG pipeline overview; LLM-as-a-judge evaluation; open-source availability
- §2 Background — 2.1 RAG approaches and systems; 2.2 knowledge graphs with LLMs and RAG; 2.3 adaptive benchmarking; 2.4 RAG evaluation criteria
- §3 Methods — 3.1 GraphRAG workflow (chunking, entity/relationship/claim extraction, graph construction, community detection, community summaries, map-reduce answers); 3.2 global sensemaking question generation; 3.3 evaluation criteria
- §4 Analysis — Experiment 1 (datasets, six conditions, configuration); Experiment 2 (claim-based measures)
- §5 Results — Experiment 1 and Experiment 2 findings
- §6 Discussion — limitations and future work
- §7 Conclusion; References; Appendices A–G (prompts, examples, statistics)

## Key points
- GraphRAG uses an LLM to build a graph index in two stages: first deriving an entity knowledge graph from the source documents, then pre-generating community summaries for all groups of closely related entities ⟨arxiv 2404.16130, §Abstract⟩
- At query time, each community summary is used to generate a partial response, then all partial responses are again summarized into a final response to the user (a map-reduce over summaries) ⟨arxiv 2404.16130, §Abstract⟩
- Conventional "vector RAG" retrieves records individually relevant to the query that collectively fit the context window, and works well for queries answerable from information localized within a small set of records, but does not support sensemaking queries requiring global understanding of the entire dataset ⟨arxiv 2404.16130, §2.1⟩
- The pipeline first splits documents into text chunks; chunk size is a fundamental design decision, since longer chunks require fewer LLM calls (lower cost) but suffer degraded recall of information appearing early in the chunk ⟨arxiv 2404.16130, §3.1.1⟩
- The LLM is prompted to extract instances of important entities and the relationships between them from each chunk, and to generate short descriptions for the entities and relationships; prompts can be tailored to a domain via few-shot exemplars for in-context learning ⟨arxiv 2404.16130, §3.1.2⟩
- The LLM can additionally extract *claims* — important factual statements about entities such as dates, events, and interactions with other entities ⟨arxiv 2404.16130, §3.1.2⟩
- In graph construction, extracted instances become nodes and edges; entity descriptions are aggregated and summarized per node/edge, and the number of duplicate relationships becomes edge weights; the manuscript's analysis uses exact string matching for entity matching, though softer matching can be substituted ⟨arxiv 2404.16130, §3.1.3⟩
- GraphRAG uses **Leiden community detection** (Traag et al., 2019) in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned ⟨arxiv 2404.16130, §3.1.4⟩
- Each level of the hierarchy provides a community partition covering the graph's nodes in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization ⟨arxiv 2404.16130, §3.1.4⟩
- Community summaries are generated bottom-up: leaf-level community element summaries are prioritized by combined source-and-target node degree and added until the token limit is reached; higher-level summaries substitute shorter sub-community summaries for longer element summaries when they do not fit ⟨arxiv 2404.16130, §3.1.5⟩
- For a global answer, community summaries are randomly shuffled and chunked, intermediate "map" answers are generated in parallel with a 0–100 helpfulness score (score-0 answers filtered), then the "reduce" step adds answers in descending helpfulness order until the token limit, producing the final global answer ⟨arxiv 2404.16130, §3.1.6⟩
- Evaluation uses an adaptive-benchmarking, LLM-based question generator: from a corpus description the LLM generates K personas, N tasks per user, and M questions per (user, task) pair (set to K=M=N=5 for 125 test questions per dataset) requiring understanding of the entire corpus without low-level fact retrieval ⟨arxiv 2404.16130, §3.2⟩
- Answers are compared head-to-head by an LLM judge on three target criteria — Comprehensiveness, Diversity, and Empowerment — plus a control criterion, Directness ⟨arxiv 2404.16130, §3.3⟩
- Across two ~1M-token datasets, global approaches significantly outperformed conventional vector RAG (semantic search) on comprehensiveness (win rates 72–83%, p<.001) and diversity, while vector RAG produced the most direct responses ⟨arxiv 2404.16130, §5.1⟩
- Root-level community summaries (C0) required dramatically fewer tokens per query (9x–43x fewer than source-text summarization), offering a highly efficient method for iterative global question answering while retaining comprehensiveness (72% win rate) and diversity (62% win rate) advantages over vector RAG ⟨arxiv 2404.16130, §5.1⟩
- GraphRAG is available as open-source software at github.com/microsoft/graphrag, with versions also available as extensions to LangChain, LlamaIndex, NebulaGraph, and Neo4J ⟨arxiv 2404.16130, §1⟩
- Future work proposes hybrid schemes combining embedding-based matching of queries to graph annotations with just-in-time community-report generation, plus "roll-up" and exploratory "drill-down" mechanisms across the community hierarchy ⟨arxiv 2404.16130, §6.2⟩

## Concepts & entities covered
Concepts: [[graphrag]] · [[retrieval-augmented-generation]] · [[global-vs-local-search]] · [[community-detection-summarization]] · [[entity-relation-extraction]] · [[llm-kg-construction]]
Entities: [[microsoft-graphrag]] · [[leiden-community-detection]] · [[org-microsoft]]
