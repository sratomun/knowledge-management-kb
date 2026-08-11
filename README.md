# LLM Wiki KB

An emergent, lightweight semantic wiki for a heterogeneous corpus (regulations,
standards, RFCs, vendor docs, whitepapers, articles, blogs). Read **CLAUDE.md** — it is
the operating model. Markdown is the source of truth; git history is the transaction-time
record.

- `concepts/` `entities/` `sources/<kind>/` `index/` — the wiki
- `templates/` — page templates for each node type
- `lint/rules.md` + `lint/lint.py` — integrity checks (`python lint/lint.py`)
- `.claude/skills/ingest-source/` — the ingest → evolve → lint procedure
