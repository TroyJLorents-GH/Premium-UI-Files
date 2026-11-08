#!/usr/bin/env python3
"""Look up tools in the bundled 341-entry UI/UX tool index (references/library/tool-index.csv).

Usage:
    python3 lookup.py <keyword> [<keyword> ...] [--category motion|components|platform|native|styling] [--evidence V|R] [--json] [--limit N]

Keywords match (case-insensitive) against id, name, function, tradeoff and url; all keywords must match
unless --any is given. Prints id · name · evidence · category, then function / tradeoff / url.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "library", "tool-index.csv")
CATEGORY_ALIASES = {
    "native": "5.", "browser": "5.", "css": "5.",
    "motion": "6.", "3d": "6.", "animation": "6.",
    "components": "7.", "component": "7.", "design": "7.",
    "platform": "8.", "perf": "8.", "a11y": "8.", "mobile": "8.",
    "styling": "9.", "research": "9.", "prototyping": "9.",
}


def load_rows():
    with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keywords", nargs="*")
    ap.add_argument("--category", help="category prefix or alias: native|motion|components|platform|styling or '6.'")
    ap.add_argument("--evidence", choices=["V", "R"])
    ap.add_argument("--any", action="store_true", help="match any keyword instead of all")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    if not os.path.exists(CSV_PATH):
        print(f"error: index not found at {CSV_PATH}", file=sys.stderr)
        sys.exit(2)

    rows = load_rows()
    kws = [k.lower() for k in args.keywords]
    cat = args.category
    if cat:
        cat = CATEGORY_ALIASES.get(cat.lower(), cat)

    out = []
    for r in rows:
        hay = " ".join([r.get("id", ""), r.get("name", ""), r.get("function", ""), r.get("tradeoff", ""), r.get("url", "")]).lower()
        if kws:
            ok = any(k in hay for k in kws) if args.any else all(k in hay for k in kws)
            if not ok:
                continue
        if cat and not r.get("category", "").lower().startswith(cat.lower()):
            continue
        if args.evidence and r.get("evidence", "").strip() != args.evidence:
            continue
        out.append(r)

    # rank: name matches first
    def score(r):
        name = r.get("name", "").lower()
        return (0 if any(k in name for k in kws) else 1, r.get("id", ""))

    out.sort(key=score)
    out = out[: args.limit]

    if args.json:
        print(json.dumps(out, indent=2))
        return
    if not out:
        print("no matches · try fewer keywords, --any, or grep references/library/cheat-sheet-2026.md")
        return
    for r in out:
        print(f"{r['id']} · {r['name']} · {r['evidence']} · {r['category']}")
        print(f"    what: {r['function']}")
        print(f"    tradeoff: {r['tradeoff']}")
        print(f"    url: {r['url']}  (checked {r.get('research_date','')})")
    print(f"\n{len(out)} shown. V = official source inspected on the research date; R = recheck before adopting.")


if __name__ == "__main__":
    main()
