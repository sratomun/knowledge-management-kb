---
title: "LegalBench-RAG: A Benchmark for Retrieval-Augmented Generation in the Legal Domain"
type: source
kind: article
authority: informational
subtype: benchmark
aliases: ["LegalBench-RAG"]
publisher: "Nicholas Pipitone & Ghita Houir Alami (ZeroEntropy)"
url: https://arxiv.org/abs/2408.10343
version: "arXiv:2408.10343v1 [cs.AI]"
published: 2024-08
effective_from: 2024-08
effective_to: ongoing
status: current
tags: [knowledge-processing]
concepts: ["[[obligation-lookup]]", "[[precise-retrieval]]", "[[retrieval-evaluation]]", "[[contract-clause-extraction]]", "[[retrieval-augmented-generation]]"]
entities: ["[[legalbench-rag-benchmark]]"]
updated: 2026-08-10
---

# LegalBench-RAG: A Benchmark for Retrieval-Augmented Generation in the Legal Domain

## Scope & purpose
A benchmark paper by Nicholas Pipitone and Ghita Houir Alami (ZeroEntropy, San Francisco) that targets what it frames as a critical gap in legal AI evaluation: existing benchmarks such as LegalBench assess the *generative* capabilities of LLMs, but none evaluate the *retrieval* component of RAG pipelines in the legal domain ⟨Abstract; §1⟩. The authors present LegalBench-RAG as, in their words, the first benchmark specifically designed to evaluate the retrieval step of legal RAG, emphasizing precise retrieval of minimal, highly relevant snippets so that downstream LLMs can generate citations and stay within context-window limits ⟨Abstract; §1⟩. The dataset is publicly released (github.com/zeroentropy-cc/legalbenchrag) ⟨header⟩.

## Structure
- §1 Introduction — the retrieval-evaluation gap and why legal RAG needs a domain-specific benchmark
- §2 Related work — RAG mechanics (chunking, embeddings, reranking) and the original LegalBench reasoning benchmark
- §3 The dataset — construction by retracing LegalBench annotations to source spans; four source corpora; quality control; statistics; the LegalBench-RAG-mini subset; limitations
- §4–5 Benchmarking & results — hyperparameters (chunking, top-k, reranker, embedding model), experimental setup, and key findings on precision/recall
- §6 Conclusion — retrieval-focused evaluation and the call for domain-specific legal tooling

## Key points
- The paper positions LegalBench-RAG as the first benchmark dedicated to the retrieval step of RAG in the legal space, distinct from LegalBench which the authors describe as assessing generation and legal reasoning rather than retrieval quality over a large corpus ⟨Abstract; §1; §2.3⟩
- It emphasizes *precise* retrieval — extracting minimal, highly relevant text segments — and argues that such snippets are preferable to returning document IDs or large sequences of imprecise chunks that can exceed context-window limits ⟨Abstract; §1⟩
- The authors motivate precision by noting that long context windows cost more, add latency, and lead LLMs to forget or hallucinate, whereas precise results let the LLM generate citations and let a human-in-the-loop quickly verify claims ⟨Abstract; §1⟩
- The benchmark is constructed by retracing the context used in LegalBench queries back to their original locations within the source legal corpus ⟨Abstract; §3⟩
- It comprises 6,858 query–answer pairs over a corpus of more than 79M characters, entirely human-annotated by legal experts (reported as 714 documents, ~79.7M characters, 6,889 queries) ⟨Abstract; §3⟩
- The four source datasets are PrivacyQA (consumer-app privacy policies, 194 queries), CUAD (private contracts, 4,042), MAUD (public-company M&A documents, 1,676), and ContractNLI (NDA-related documents, 977) ⟨§3⟩
- Each query is paired with a list of relevant snippets; the label for a snippet is its file path, exact quote, and precise character indices, expressed as an array of (filename, index-range) tuples so that non-adjacent spans can be captured ⟨§3⟩
- Quality control is applied at three decision points: mapping annotation categories to interrogatives, mapping document IDs to GPT-4o-mini-generated descriptions (regex-validated, manually inspected, near-duplicate pairs excluded via embedding similarity), and selecting which annotation categories to include ⟨§3⟩
- LegalBench-RAG-mini is a lightweight subset of exactly 194 queries from each source dataset — 776 queries, 72 documents, 8.68M characters — intended for rapid iteration ⟨§3⟩
- The experimental setup uses OpenAI text-embedding-3-large, a SQLite Vec vector DB, and the Cohere rerank-english-v3.0 reranker, comparing two chunking strategies (naive fixed-size 500-char and Recursive Character Text Splitter) with and without the reranker ⟨§4–5⟩
- The paper reports that its most effective configuration was the Recursive Character Text Splitter (RCTS) *without* a reranker, yielding the highest precision and recall of the setups tested ⟨§4–5, Key findings⟩
- The paper reports the surprising result that the Cohere reranker performed *worse* than using no reranker, which it attributes to the difficulty and legal focus of the benchmark not aligning with a general-purpose reranker, and cites this as a limitation of applying general-purpose models to specialized legal text ⟨§4–5, Key findings; §6⟩
- The authors report that, as expected, recall improved with increasing k while precision decreased, attributing the low absolute precision to the highly targeted, concise nature of the ground-truth snippets ⟨§4–5⟩
- They report PrivacyQA as the easiest source dataset (Precision@1 14.38%, Recall@64 84.19%) and MAUD as the most challenging due to technical legal jargon (Precision@1 2.65%, Recall@64 28.28%), with ContractNLI and CUAD in between ⟨§4–5⟩
- Stated limitations: the corpus covers NDAs, M&A, commercial contracts, and privacy policies but is not exhaustive, does not assess structured numerical or medical data, and — because each query is answered by exactly one document — does not assess multi-document (multi-hop) reasoning ⟨§3⟩

## Concepts & entities covered
Concepts: [[obligation-lookup]] · [[precise-retrieval]] · [[retrieval-evaluation]] · [[contract-clause-extraction]] · [[retrieval-augmented-generation]]
Entities: [[legalbench-rag-benchmark]]
