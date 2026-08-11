---
title: "Deep Tabular Research via Continual Experience-Driven Execution"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["Deep Tabular Research"]
publisher: arXiv
url: https://arxiv.org/abs/2603.09151
version: "arXiv:2603.09151v2 [cs.AI]"
published: 2026
effective_from: 2026-03
effective_to: ongoing
status: current
tags: [doc-processing]
concepts: ["[[complex-table-understanding]]", "[[table-serialization]]", "[[agentic-extraction]]"]
entities: ["[[deep-tabular-agent]]"]
updated: 2026-08-11
---

# Deep Tabular Research via Continual Experience-Driven Execution

## Scope & purpose

The paper (Tencent Youtu Lab; Ruijin Hospital, Shanghai Jiao Tong University) formalizes
Deep Tabular Research (DTR): long-horizon, multi-hop analytical reasoning over unstructured
tables that feature hierarchical and bidirectional headers, merged cells, and non-canonical
layouts, where a single query may require chained factual checks, numerical computation, and
aggregation across disparate regions ⟨Abstract; §1; §2⟩. Its central argument is to decouple
high-level strategic planning from low-level programmatic execution and to drive planning
with accumulated execution experience rather than rigid heuristics ⟨Abstract; §1⟩. The KB
records the paper's comparative results descriptively.

## Key points

- The paper says prior TableQA pipelines assume clean schemas, flat headers, and single-pass
  reasoning, and that treating tables as serialized text is limited by token constraints and
  imprecise numerical operations over large irregular headers, motivating a programmatic
  (DataFrame-based) execution approach ⟨§1⟩.
- It names two challenges of moving from text reasoning to a code-driven agent: a prohibitive
  search space for translating high-level intent into concrete code operations over
  unstructured tables, and error propagation across long executions with little mechanism to
  learn from past outcomes (especially failures) ⟨§1⟩.
- Tabular comprehension first builds a structured representation: Meta Information Extraction
  (explicit headers/sub-headers plus implicit units, temporal/categorical markers, aggregation
  indicators), Bi-directional Header Identification (resolving row and column header spans so
  each cell gets row-wise and column-wise descriptors), and Meta Graph Construction (an
  overlapping tree-like graph where a sub-item can belong to both row and column parents)
  ⟨§3.1⟩.
- Query-Guided Operation Mapping decomposes the query and, using a predefined seed operation
  bank ({CLEAN, FILTER, GROUP, AGG, JOIN, SORT, ...}), an LLM agent selects candidate
  operations over the linearized graph (relational triples) and builds an operation map
  encoding admissible orderings and prerequisites ⟨§3.2⟩.
- Path Planning uses an expectation-aware selection score (a p-UCB-style formula balancing
  an empirical expected-return term for exploitation against a structural-prior exploration
  term) to rank candidate operation paths, refining preferences iteratively from intermediate
  execution results rather than in a single pass ⟨§3.3; Eq. 1⟩.
- A siamese structured memory records two feedback streams: parameterized execution signals
  (execution validity, time, and output-type consistency, aggregated into a reward) for
  immediate path refinement, and abstracted textual experience (value-agnostic strategic
  patterns, e.g. "insert CHECK/CLEAN before AGG") for longer-term transfer across instances
  ⟨§3.4; Eq. 4⟩; a structured [THINK]/[CODE] flag interleaves reasoning and coding along a path
  ⟨§3.3⟩.
- The final answer is chosen by majority agreement across multiple executed paths, which the
  paper says improves robustness against individual execution errors ⟨§3.5; Eq. 6⟩.
- Evaluation is on two unstructured-table benchmarks: RealHitBench (real-world hierarchical
  tables) and the paper's own DTR-Bench (500 scenario-driven analytical QA pairs across 8
  personas and domains such as Economy/Business/Education, with answers computed
  programmatically and machine-checkable AnswerKeyPoints) ⟨§4.1; App B; App C⟩.
- On DTR-Bench the paper reports DTR (DeepSeek-V3) achieves the strongest overall performance
  across accuracy, analysis depth, feasibility, and aesthetics under both strict Win-Rate and
  tolerant Score-Rate evaluation, and that agentic baselines (ST-Raptor, TreeThinker, Code
  Loop) gain structural reasoning but incur heavy compute and instability from branching and
  repeated trials ⟨§4.1; Table 1⟩.
- On RealHitBench the paper reports DTR (DeepSeek-V3) leads across Fact Checking, Numerical
  Reasoning, Structure Comprehension, Data Analysis, and Chart/Report Generation (e.g. 100.0
  ECR and 52.69 Pass@1 on visualization) ⟨§4.1; Table 2⟩.
- An architecture ablation reports a 4.0-point total accuracy gain over a pure DeepSeek-V3
  baseline (33.5% → 37.5%), with meta-information (+1.3) and query decomposition (+1.4) the
  largest contributors and diminishing returns from expectation-aware selection (+0.9) and
  abstracted experience (+0.4) ⟨§4.2; Table 3⟩.
- A prompting-strategy ablation reports the structured [THINK]+[CODE] scheme reduces code error
  rate from 42.3% (direct generation) to 28.4% while attaining the highest accuracy (37.5%) at
  4.78 average LLM calls ⟨§4.2; Table 4⟩; an efficiency analysis reports DTR's 4.78-call
  operating point outperforms the CodeLoop baseline, which reaches only 27.5% accuracy despite
  8.8 calls ⟨§4.3; Figure 3⟩.
- The paper states its broader-impact position and does not claim new ethical risks beyond
  those common to LLM-based data-analysis systems, recommending human-in-the-loop validation
  for high-stakes settings ⟨Broader Impact⟩.

## Concepts & entities covered
Concepts: [[complex-table-understanding]] · [[table-serialization]] · [[agentic-extraction]]
Entities: [[deep-tabular-agent]]
