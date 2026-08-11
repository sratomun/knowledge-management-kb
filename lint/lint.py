#!/usr/bin/env python3
"""Mechanical linter for the LLM wiki KB. Stdlib only.

Implements the mechanical checks in lint/rules.md (M1-M9). Judgment checks
(J1-J5) are handled by the agent's evolve loop, not here.

Usage:
    python lint/lint.py            # report
    python lint/lint.py --fix      # apply safe auto-fixes (M8 status)
"""
import os
import re
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINT_DIRS = ["concepts", "entities", "sources"]      # pages subject to linting
LINK_DIRS = LINT_DIRS + ["index"]                    # dirs scanned for outgoing links

KINDS = {"regulation", "standard", "rfc", "provider-doc", "whitepaper", "article", "blog"}
AUTH = {"binding", "normative", "vendor", "practitioner", "informational"}
STATUS = {"current", "superseded", "draft"}
CITE_SECTIONS = {"how sources treat it", "key points", "key facts"}
REQUIRED = {
    "concept": ["title", "type", "updated"],
    "entity": ["title", "type", "updated"],
    "source": ["title", "type", "kind", "authority", "publisher", "updated"],
}
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
PLACEHOLDER = re.compile(r"[<>]")

errors, warns = [], []
def err(f, m): errors.append((f, m))
def warn(f, m): warns.append((f, m))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")


def parse(path):
    """Return (frontmatter dict of raw strings, body str)."""
    text = open(path, encoding="utf-8").read()
    fm, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end]
            body = text[end + 4:]
            for line in block.splitlines():
                line = line.split("#", 1)[0].rstrip() if not line.strip().startswith("#") else ""
                if ":" not in line:
                    continue
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm, body


def links_in(text):
    out = []
    for m in WIKILINK.findall(text):
        if PLACEHOLDER.search(m):        # skip template placeholders
            continue
        out.append(slug(m))
    return out


def aliases_of(fm):
    raw = fm.get("aliases", "")
    raw = raw.strip().lstrip("[").rstrip("]")
    return [slug(a) for a in raw.split(",") if a.strip() and not PLACEHOLDER.search(a)]


def parse_date(s):
    s = (s or "").strip()
    if not s or s in ("ongoing", "empty") or PLACEHOLDER.search(s):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return "bad"


def collect():
    pages = {}          # stem -> {path, fm, body, type, dir}
    key_to_stem = {}    # stem/title/alias slug -> stem
    for d in LINK_DIRS:
        base = os.path.join(ROOT, d)
        for dp, _, fns in os.walk(base):
            for fn in fns:
                if not fn.endswith(".md"):
                    continue
                path = os.path.join(dp, fn)
                stem = fn[:-3]
                fm, body = parse(path)
                rec = {"path": os.path.relpath(path, ROOT), "fm": fm, "body": body,
                       "type": fm.get("type", ""), "dir": d, "stem": stem}
                pages[stem] = rec
                key_to_stem[slug(stem)] = stem
                if fm.get("title") and not PLACEHOLDER.search(fm["title"]):
                    key_to_stem[slug(fm["title"])] = stem
                for a in aliases_of(fm):
                    key_to_stem.setdefault(a, stem)
    return pages, key_to_stem


def main():
    fix = "--fix" in sys.argv
    pages, key_to_stem = collect()

    # M5 alias uniqueness
    seen = {}
    for stem, r in pages.items():
        keys = [slug(stem)]
        if r["fm"].get("title") and not PLACEHOLDER.search(r["fm"]["title"]):
            keys.append(slug(r["fm"]["title"]))
        keys += aliases_of(r["fm"])
        for k in keys:
            if k in seen and seen[k] != stem:
                err(r["path"], f"M5 alias/title collision on '{k}' (also {pages[seen[k]]['path']})")
            seen[k] = stem

    referenced = set()
    for stem, r in pages.items():
        f, fm, body, t = r["path"], r["fm"], r["body"], r["type"]
        if r["dir"] == "index":
            for lk in links_in(fm.get("title", "") + "\n" + body):
                if lk in key_to_stem:
                    referenced.add(key_to_stem[lk])
            continue

        # M1 type
        if t not in ("concept", "entity", "source"):
            err(f, f"M1 invalid or missing type: '{t}'")
        # M2 required fields
        for req in REQUIRED.get(t, []):
            v = fm.get(req, "")
            if not v or PLACEHOLDER.search(v):
                err(f, f"M2 missing required field '{req}'")
        # M3 enums (sources)
        if t == "source":
            if fm.get("kind") and fm["kind"] not in KINDS and not PLACEHOLDER.search(fm["kind"]):
                err(f, f"M3 invalid kind '{fm['kind']}'")
            if fm.get("authority") and fm["authority"] not in AUTH and not PLACEHOLDER.search(fm["authority"]):
                err(f, f"M3 invalid authority '{fm['authority']}'")
        st = fm.get("status", "")
        if st and st not in STATUS and not PLACEHOLDER.search(st):
            err(f, f"M3 invalid status '{st}'")

        # M4 dangling links + collect references
        for lk in links_in(body + "\n" + " ".join(v for v in fm.values())):
            if lk in key_to_stem:
                referenced.add(key_to_stem[lk])
            else:
                err(f, f"M4 dangling link [[{lk}]]")

        # M7 missing citations
        cur = None
        for line in body.splitlines():
            h = re.match(r"##+\s+(.*)", line)
            if h:
                cur = h.group(1).strip().lower()
            elif cur in CITE_SECTIONS and line.strip().startswith("- "):
                if "⟨" not in line and not PLACEHOLDER.search(line):
                    warn(f, f"M7 uncited bullet under '{cur}': {line.strip()[:60]}")

        # M8 date sanity + status derivation
        ef, et = parse_date(fm.get("effective_from")), parse_date(fm.get("effective_to"))
        if ef == "bad":
            warn(f, "M8 unparseable effective_from")
        if et == "bad":
            warn(f, "M8 unparseable effective_to")
        if isinstance(ef, datetime.date) and isinstance(et, datetime.date) and ef > et:
            warn(f, "M8 effective_from after effective_to")
        sup = fm.get("superseded_by", "")
        superseded = (sup and not PLACEHOLDER.search(sup)) or (
            isinstance(et, datetime.date) and et < datetime.date.today())
        if superseded and st == "current":
            warn(f, "M8 marked current but superseded_by/effective_to says otherwise")
            if fix:
                _apply_status_fix(os.path.join(ROOT, f))

    # M6 orphans
    for stem, r in pages.items():
        if r["dir"] == "index":
            continue
        if stem not in referenced:
            warn(r["path"], "M6 orphan — not linked from any index or page")

    # M9 superseded-still-cited
    for stem, r in pages.items():
        if r["dir"] == "index":
            continue
        st, sup = r["fm"].get("status", ""), r["fm"].get("superseded_by", "")
        et = parse_date(r["fm"].get("effective_to"))
        is_old = st == "superseded" or (sup and not PLACEHOLDER.search(sup)) or (
            isinstance(et, datetime.date) and et < datetime.date.today())
        if not is_old:
            continue
        for other, o in pages.items():
            if other == stem or o["dir"] == "index":
                continue
            if slug(stem) in links_in(o["body"]):
                warn(o["path"], f"M9 cites superseded page [[{stem}]] — verify it isn't presented as current")

    # report
    n = len([p for p in pages.values() if p["dir"] != "index"])
    print(f"Linted {n} pages.\n")
    for label, items in (("ERROR", errors), ("WARN", warns)):
        for f, m in items:
            print(f"  {label:5} {f}: {m}")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s).")
    sys.exit(1 if errors else 0)


def _apply_status_fix(path):
    text = open(path, encoding="utf-8").read()
    new = re.sub(r"(?m)^(status:\s*)current\b", r"\1superseded", text, count=1)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)


if __name__ == "__main__":
    main()
