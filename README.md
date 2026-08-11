# Knowledge Management KB

A densely cross-linked markdown knowledge base over a heterogeneous corpus — regulations,
standards, RFCs, vendor docs, whitepapers, and research papers — built to be read and
maintained by an LLM agent.

It is **not** vanilla flat notes, and **not** a formal ontology (no OWL/RDF triplestore).
It sits between: a small fixed set of node types, free-form subtypes that emerge from the
corpus, typed links, and three maintenance loops that let structure grow while linting
keeps it coherent.

**753 pages** · 171 concepts · 456 entities · 109 cited sources · 17 domain maps

---

## The one rule that shapes everything

> When sources disagree, this KB surfaces **every** perspective with citations and
> **leaves them standing**. It never picks a winner.

It is descriptive, never prescriptive. It captures and organizes what a corpus says so
that software leadership and enterprise architects can navigate it — it does not make
recommendations, take org stances, or record decisions. Adjudication is the reader's job.

Every page section titled *"Where sources differ"* exists to hold that tension open rather
than resolve it. For example, [`concepts/complex-table-understanding.md`](concepts/complex-table-understanding.md)
records three papers proposing incompatible architectures, including one calling another's
approach "fragile" — attributed as that paper's own claim, with the shared-benchmark
caveat noted, and no verdict rendered.

---

## Node types

Three core types. Each page declares `type`, and may declare a free-form `subtype` that
emerges from the corpus rather than being fixed up front.

| Type | Path | What it holds |
|---|---|---|
| **Concept** | `concepts/` | A universal or topic — *"table serialization"*, *"least privilege"*. Source-agnostic, and the primary human entry point. |
| **Entity** | `entities/` | A named individual — GDPR Art. 32, AWS KMS, NIST, a specific control edition. Time-bound when its referent is. |
| **Source** | `sources/<kind>/` | One page per ingested item: summary, metadata, citations. Clause content lives here as cited summary, never exploded into one file per clause. |

Subtypes accrue from use — currently `vocabulary-term` (172), `specification-construct`
(51), `organization` (46), `ai-technique`, `benchmark`, `standard-edition`, and others. A
subtype becomes "known" only by recurring often enough to be promoted.

## Source kinds and authority

Every source declares `kind` and `authority`. These are **descriptive weight signals**
shown next to citations — they are deliberately *not* used to rank sources or resolve
disagreements.

| kind | authority | count |
|---|---|---|
| regulation | binding | 2 |
| standard | normative | 28 |
| provider-doc | vendor | 16 |
| whitepaper | informational | 10 |
| article | informational / practitioner | 49 |
| blog | practitioner | 4 |

## Citation rules

- **Cite everything.** Every factual claim carries a source link and a locator in `⟨…⟩` —
  clause id, section, article, or URL. **No locator → don't assert it.**
- **Preserve modality verbatim** for normative or binding sources. Never soften MUST → should.

---

## Temporal model

The corpus supersedes itself constantly, so time is modeled — but on a single axis.

Sources and time-bound entities carry `published`, `effective_from`, `effective_to`.
Supersession is a **typed link** (`superseded_by` / `supersedes`), not a flag — so it can
be partial, and two editions can overlap during a transition window. `status`
(`current | superseded | draft`) is a derived convenience label; the dates and links are
the source of truth.

There is deliberately **no second temporal axis** for when the KB learned something —
git history is that axis, for free.

---

## The three loops

**1. Ingest** — add one source and weave it in, never file it in isolation. Classify,
write the source page with cited key points and temporal fields, then extract the concepts
and entities it touches and draft or extend their pages.

**2. Evolve** — let structure settle. Resolve entities against existing pages before
creating new ones; re-link older pages whose "where sources differ" sections the new
material affects; promote recurring terms and subtypes to first-class status; merge
duplicates and split overloaded pages.

**3. Lint** — validate the graph. `python lint/lint.py` runs the mechanical checks; the
judgment checks are the agent's. Linting is what makes aggressive ingestion safe.

### The emergence gate

New concepts, promotions, and merges are never applied silently. A change is **proposed**
with rationale, then **judged** by an independent sub-agent (is it genuinely new, well-formed,
cited, non-adjudicating?). Confident-yes applies it; confident-no discards it with a note;
anything short of confident leaves a `<!-- REVIEW: … -->` marker for a human and stops.

---

## Layout

```
concepts/     171 pages   universals and topics
entities/     456 pages   named individuals
sources/      109 pages   one per ingested item, by kind
index/         17 pages   domain maps of content — start here
guidance/                 synthesis notes across domains
templates/                page template per node type
lint/                     rules.md (human-readable) + lint.py (mechanical)
```

## Domains

Each has a map-of-content page in `index/`:

[Semantic Web](index/semantic-web.md) ·
[OBDA & Virtual Knowledge Graphs](index/obda.md) ·
[Knowledge Organization](index/knowledge-organization.md) ·
[Metadata & Registries](index/metadata.md) ·
[Ontology Engineering](index/ontology-engineering.md) ·
[Semantic Layer & Headless BI](index/semantic-layer.md) ·
[Data Architecture & Management](index/data-architecture.md) ·
[Enterprise Architecture](index/enterprise-architecture.md) ·
[Semantic Wikis](index/semantic-wiki.md) ·
[Knowledge Management](index/knowledge-management.md) ·
[GraphRAG & LLM KG Construction](index/graph-rag.md) ·
[AI Governance & Compliance](index/ai-governance.md) ·
[HR & Occupation Standards](index/hr-standards.md) ·
[Document Ingestion & IDP](index/doc-processing.md) ·
[Document Use-Case Processing Patterns](index/knowledge-processing.md) ·
[Human-vs-AI Performance Benchmarking](index/benchmarking.md)

## Guidance notes

Two cross-domain synthesis documents that read across the corpus rather than describing
one source:

- [**Realistic Performance Expectations**](guidance/realistic-performance-expectations.md) —
  measured human baselines vs LLM performance per task, dominant failure modes, and why a
  benchmark number should be distrusted before it is trusted.
- [**Knowledge Processing Playbook**](guidance/knowledge-processing-playbook.md) — how to
  build each document use case.

---

## Reading it

Start at [`index/home.md`](index/home.md), or any domain map above. Links use `[[slug]]`
(the target filename stem) — the vault opens directly in [Obsidian](https://obsidian.md),
though everything is plain markdown and readable without it.

```bash
python lint/lint.py     # mechanical integrity checks
```

## Note on scope

Markdown is the source of truth. This repository omits the raw ingested source material
(`sources/_raw/`) and the agent operating model (`CLAUDE.md`), so what you see is the
distilled graph with its citations, not the originals it was distilled from.

Git history began 2026-08-10 with the existing corpus as a single commit, so learned-on
dates are only meaningful for material added after that point.
