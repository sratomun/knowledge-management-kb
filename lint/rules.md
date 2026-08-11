# Lint rules

Two classes of check. **Mechanical** rules are implemented in `lint.py` and can be
auto-fixed or reliably reported. **Judgment** rules require the agent (and, on low
confidence, the emergence gate / a human).

Severity: `error` blocks a clean run; `warn` is advisory.

## Mechanical (lint.py)

| # | rule | severity | auto-fix |
|---|------|----------|----------|
| M1 | **Valid `type`** — every page frontmatter has `type ∈ {concept, entity, source}`. | error | no |
| M2 | **Required fields present** — concept: `title,type,updated`; entity: `title,type,updated`; source: `title,type,kind,authority,publisher,updated`. | error | no |
| M3 | **Allowed enums** — source `kind` and `authority` are from the CLAUDE.md sets; `status ∈ {current,superseded,draft}`. | error | no |
| M4 | **Dangling links** — every `[[slug]]` resolves to an existing page (by stem, title, or alias). | error | no |
| M5 | **Alias uniqueness** — no alias (or title) claimed by two different pages. | error | no |
| M6 | **Orphans** — every concept/entity/source page is reachable from at least one index or other page. | warn | link into index |
| M7 | **Missing citations** — bullets under "How sources treat it" / "Key points" / "Key facts" must contain a `⟨…⟩` locator. | warn | no |
| M8 | **Date sanity** — `effective_from ≤ effective_to`; `published` parseable; if `superseded_by` set then `status` should be `superseded`. | warn | fix status |
| M9 | **Superseded-still-cited** — a source/entity with `effective_to` in the past (or `superseded_by` set) is still linked as current from a concept/entity page. | warn | no |

## Judgment (agent, via evolve loop + emergence gate)

- **J1 Duplicate/near-duplicate** — two pages describe the same concept/entity under
  different names. → propose merge through the gate.
- **J2 Overloaded page** — one concept page covers what should be two. → propose split.
- **J3 Silent adjudication (scope drift)** — a page has started recommending, concluding,
  or resolving a divergence. Highest-priority judgment check; the KB must stay descriptive.
- **J4 Subtype promotion** — an emergent `subtype` recurs enough to become "known". →
  propose through the gate.
- **J5 Modality drift** — a normative claim was paraphrased in a way that softens
  MUST/SHOULD/MAY relative to the source. → fix against the source.

## Running
- `python lint/lint.py` — report all mechanical checks.
- `python lint/lint.py --fix` — apply the safe auto-fixes (M6 index stub, M8 status).
- Judgment checks: run as part of the evolve loop; on low confidence, escalate per the
  emergence gate.
