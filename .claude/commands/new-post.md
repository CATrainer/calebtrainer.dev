---
description: Start a new draft post on its own branch
argument-hint: "<title> [--notebook] [notes or draft text]"
---

Start a draft post from: $ARGUMENTS

1. `git checkout main && git pull`.
2. Pick a short slug from the title (three to six words, lowercase, hyphens).
3. `git checkout -b post/<slug>`.
4. `python scripts/new_post.py "<title>" --slug <slug>`. Add `--notebook` if Caleb asked for one or if the post is mostly an experiment with code and plots.
5. If Caleb gave notes or draft text, put them in the body as written. Fix formatting only (headings, code fences, maths, links). Don't rewrite his prose or add your own.
6. Commit as `Draft: <title>` and `git push -u origin post/<slug>`.
7. Wait for the Vercel preview (about a minute), then get its URL with the `gh api` command in CLAUDE.md and give it to him with the file path.
