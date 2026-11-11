#!/usr/bin/env python3
"""Create a new draft post.

    python scripts/new_post.py "Backprop by hand"
    python scripts/new_post.py "Tokenizer benchmarks" --notebook
    python scripts/new_post.py "Fleet week 3" --date 2027-02-14

Makes posts/<date>-<slug>/index.md (or index.ipynb) from _templates/,
marked as a draft. Drafts show on preview deployments, not on the live site.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slugify(title: str) -> str:
    slug = re.sub(r"['\u2019]", "", title.lower())
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug or "post"


def main() -> int:
    ap = argparse.ArgumentParser(description="Create a draft post.")
    ap.add_argument("title")
    ap.add_argument("--notebook", action="store_true", help="start from the notebook template")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--slug", help="override the folder name after the date")
    args = ap.parse_args()

    dt.date.fromisoformat(args.date)  # fail early on a bad date
    folder = ROOT / "posts" / f"{args.date}-{args.slug or slugify(args.title)}"
    if folder.exists():
        print(f"{folder.relative_to(ROOT)} already exists", file=sys.stderr)
        return 1
    folder.mkdir(parents=True)

    title = args.title.replace('"', '\\"')
    if args.notebook:
        nb = json.loads((ROOT / "_templates" / "notebook.ipynb").read_text())
        front = "".join(nb["cells"][0]["source"])
        front = front.replace("TITLE", title).replace("DATE", args.date)
        nb["cells"][0]["source"] = front.splitlines(keepends=True)
        out = folder / "index.ipynb"
        out.write_text(json.dumps(nb, indent=1) + "\n")
    else:
        text = (ROOT / "_templates" / "post.md").read_text()
        text = text.replace("TITLE", title).replace("DATE", args.date)
        out = folder / "index.md"
        out.write_text(text)

    print(out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
