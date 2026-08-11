---
name: ingest-source
description: Add a new source (regulation, standard, provider doc, RFC, whitepaper, article, or blog post) to the KB and weave it into the concept/entity graph through the three loops. Use when given a document, URL, or file to ingest.
---

# ingest-source

Ingest one source and integrate it. Run the three loops in order; never file a source in
isolation. Read `CLAUDE.md` for the operating model this skill assumes.

## Loop 1 — Ingest

1. **Classify** — determine `kind` and `authority` (CLAUDE.md table). Note uncertainty on
   the page if ambiguous.
2. **Create the source page** at `/sources/<kind>/<slug>.md` from `templates/source.md`.
   Fill frontmatter including temporal fields (`published`, `effective_from`,
   `effective_to`, and `supersedes`/`superseded_by` if it replaces something). Write scope,
   structure, and key points — **cite a locator on every point**; preserve MUST/SHOULD/MAY
   verbatim for normative/binding sources. Summarize; never explode into per-clause files.
3. **Extract concepts and entities** the source touches.

## Loop 2 — Evolve / consolidate

For each extracted concept/entity:

4. **Resolve before creating** — search existing pages by title + aliases + meaning. If it
   exists, extend it (add a "how sources treat it" bullet with kind·authority + locator;
   extend "where sources differ" descriptively — never resolve). If the new material bears
   on other existing pages, update their links/sections (memory-evolution).
5. **If it seems new**, or if you'd promote a recurring emergent `subtype`, do NOT create
   it directly — route through the **emergence gate** (Loop 2b).

### Loop 2b — Emergence gate (for every new page / promotion / merge)
- **Propose** the change with a one-line rationale.
- **Judge** — spawn an independent LLM-as-judge sub-agent: is it genuinely new (not a
  dup/alias), well-formed, cited, non-adjudicating?
- **Escalate** — if the judge is not confident enough, leave
  `<!-- REVIEW: <proposal + why uncertain> -->` on the source page and stop; a human
  decides. Confident-yes → apply. Confident-no → discard with a note.

6. **Update the index** for the relevant domain(s).

## Loop 3 — Lint

7. Run `python lint/lint.py`. Fix mechanical issues (dangling links, missing citations,
   date/status). Then do the judgment checks in `lint/rules.md` (J1–J5), especially **J3
   scope drift** — confirm nothing you wrote recommends, concludes, or resolves.

## Guardrails
- Descriptive only — never conclude, recommend, or adjudicate.
- No per-clause file explosion.
- Prefer extending existing pages over creating new ones.
- Every new concept/entity passes the emergence gate.
