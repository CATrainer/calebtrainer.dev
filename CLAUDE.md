# calebtrainer.dev

Caleb's blog: fortnightly build logs on training models from scratch and on skill-fleet (agents that test AI agent skills for security problems). Quarto static site, deployed by Vercel.

## How it builds

- Vercel runs `scripts/vercel-build.sh` on every push. It installs the Quarto version pinned in `requirements.txt` and renders to `_site/`.
- `main` is production. Drafts (`draft: true`) render as empty pages and stay out of the list, search, sitemap and RSS.
- Every other branch gets a preview deployment built with `--profile preview` (`_quarto-preview.yml`), which shows drafts with a "Draft" label in the list. Preview URLs sit behind Caleb's Vercel login, so drafts aren't public there. The branch source is public, because the repo is.
- Vercel never runs code. Notebooks (`.ipynb`) render with the outputs saved in the file. `.qmd` files with executable code cells use `freeze: auto`: render them locally and commit `_freeze/`.

## Layout

- `posts/YYYY-MM-DD-slug/index.md` (or `index.ipynb`, or `index.qmd` for executable code). One folder per post, images beside it.
- `posts/_metadata.yml`: defaults for every post (TOC, margin footnotes, date format).
- `_templates/`: `post.md`, `notebook.ipynb`, and `posts-list.ejs` (the home page list).
- `styles/`: `light.scss`, `dark.scss`, `_shared.scss`, `_fonts.scss`.
- `fonts/` and `katex/` are self-hosted on purpose. Don't swap them for CDN links.
- `scripts/new_post.py` creates a draft from a template. `scripts/vercel-build.sh` is the deploy build.

## Front matter

```yaml
title: "Short, specific title"
description: "One sentence. Shows on the posts list and in link previews."
date: 2026-12-01
categories: [gpt-from-scratch]   # project names: gpt-from-scratch, skill-fleet, ...
draft: true                      # false only when publishing
```

## Publishing flow

1. New post on a branch: `git checkout -b post/<slug>` then `python scripts/new_post.py "Title" --slug <slug>` (add `--notebook` for a notebook post).
2. Push the branch. Vercel builds a preview. Get its URL with:
   `gh api "repos/CATrainer/calebtrainer.dev/deployments?ref=post/<slug>" --jq '.[0].statuses_url' | xargs gh api --jq '.[0].environment_url'`
3. Publish: set `draft: false`, set `date` to the publish date, merge into `main`, push. Live in a couple of minutes at `https://calebtrainer.dev/posts/<folder>/`.

Small fixes to a published post can go straight to `main`.

Slash commands in `.claude/commands/` wrap this: `/new-post`, `/check-post`, `/publish`.

## Caleb writes the posts

Don't write post prose in his voice unless he asks. Default help is scaffolding, formatting, checking, suggesting cuts, fixing maths and code, and making plots readable. When he pastes notes or a draft, keep his wording and fix only formatting.

## Build-log rule

Every post needs at least one of these. If a draft has none, say so before publishing.

- a number he measured that isn't published anywhere else
- something that broke, and why
- a prediction written down first, and what happened
- a small experiment that explains a result
- a finding from the fleet
- something reusable: code, a table, a checklist

## Writing rules (any copy on this site)

- No em dashes. Use a full stop, a comma or brackets.
- No "not X, it's Y" or "not just X, but Y".
- No filler or hype words: actually, really, honestly, genuinely, deep dive, delve, journey, passionate, game-changer, unlock, supercharge, seamless, robust (unless it's about statistics), leverage (say use).
- Don't end sentences on three-part lists for rhythm. Two items or one is usually better.
- No italics for emphasis. No exclamation marks.
- State facts plainly in the present tense. Don't anchor them to a past change ("since X, Y now...").
- Prefer the specific: a number, a file name, the actual error message.
- British spelling.

## Checks before publishing

- `quarto render` (or `quarto render <file>`) finishes without errors or warnings. (While there are no published posts, Quarto warns that the home page listing matches no files. That one is expected.)
- Front matter complete. Description is one sentence. Date is right.
- Images exist, have alt text, and are under about 500 KB. PNG or SVG for plots.
- Links resolve.
- Notebooks: every code cell has run, outputs are present, no huge outputs, no local paths (`/Users/...`), no tokens or keys.
- No API keys, tokens or secrets anywhere in the diff.
- Build-log rule met. Writing rules met (search the post for `—`).

## Local preview

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # includes the pinned Quarto
quarto preview
```

`quarto preview --profile preview` shows drafts locally.
