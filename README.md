# calebtrainer.dev

Source for [calebtrainer.dev](https://calebtrainer.dev): build logs on training models from scratch and on testing AI agent skills for security problems. Built with [Quarto](https://quarto.org), deployed on Vercel.

## How publishing works

Each post is a folder: `posts/YYYY-MM-DD-slug/index.md` (or `index.ipynb`), with its images beside it.

- A post with `draft: true` only shows up on preview deployments.
- Pushing any branch other than `main` builds a preview, and drafts show there.
- Merging into `main` publishes. The live site updates in a couple of minutes.

## Writing a post

### Laptop, with Claude Code

```
/new-post "Backprop by hand"    # branch, draft file, preview link
...write...
/check-post                     # build check, links, secrets, build-log rule, writing rules
/publish                        # draft off, merge to main, confirm it's live
```

### Laptop, by hand

```bash
pip install -r requirements.txt          # once; includes the pinned Quarto
git checkout -b post/backprop-by-hand
python scripts/new_post.py "Backprop by hand" --slug backprop-by-hand
quarto preview --profile preview         # live reload, drafts visible
# when it's ready: set draft: false, merge into main, push
```

### From a notebook

`python scripts/new_post.py "Loss curves" --notebook` creates `index.ipynb` with the front matter in its first cell. To use a notebook from another repo, copy it in as `index.ipynb` and add the first (raw) cell from `_templates/notebook.ipynb`.

Run every cell and save with outputs. The site shows the notebook exactly as saved and never runs code on the server. `#| echo: false` at the top of a cell shows only its output, and `#| include: false` hides the cell.

### Phone

- **Claude Code on the web or in the app:** open this repo and use the same `/new-post`, `/check-post` and `/publish` commands. You can paste rough notes into `/new-post`.
- **GitHub in the browser:**
  1. Open `_templates/post.md` and copy it.
  2. Choose Add file, then Create new file, and name it `posts/2026-12-01-slug/index.md`.
  3. Paste, write, then commit to a new branch and open a pull request.
  4. Vercel comments a preview link on the pull request.
  5. When it's ready, set `draft: false` and merge.

## Repo layout

| Path | What it is |
|---|---|
| `posts/` | One folder per post. `_metadata.yml` holds the defaults for every post. |
| `_templates/` | Post and notebook templates, plus the home page list template. |
| `index.qmd`, `about.qmd` | Home page and About page. |
| `styles/` | Theme (light and dark). |
| `fonts/`, `katex/` | Self-hosted fonts and maths rendering. |
| `scripts/` | `new_post.py` and the Vercel build script. |
| `CLAUDE.md`, `.claude/commands/` | Instructions and commands for Claude Code. |
