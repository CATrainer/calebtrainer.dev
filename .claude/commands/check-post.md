---
description: Check a draft against the publishing checks and the build-log rule
argument-hint: "[post folder, defaults to the post on the current branch]"
---

Check this post: $ARGUMENTS (if empty, use the post folder changed on the current branch compared with `main`).

Run every check under "Checks before publishing" in CLAUDE.md:

1. `quarto render <post file>` and report any error or warning.
2. Front matter: title, one-sentence description, date, categories, draft flag.
3. Images: files exist, alt text present, sizes under about 500 KB.
4. Links: internal links point at real files; for external links, flag any that look wrong.
5. Notebooks: all cells run in order, outputs saved, no huge outputs, no local paths, no secrets.
6. Secrets: scan the diff against `main` for keys, tokens and passwords.
7. Build-log rule: say which item the post meets, quoting the line. If none, say so plainly.
8. Writing rules: list every em dash and every phrase that breaks the rules, with line numbers.

Report as a short list: blocking problems first, then suggestions. Fix formatting and broken syntax yourself if it's mechanical. Don't change his prose without asking.
