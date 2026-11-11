---
description: Publish a draft post to calebtrainer.dev
argument-hint: "[post folder, defaults to the post on the current branch]"
---

Publish this post: $ARGUMENTS (if empty, use the post on the current branch).

1. Run the /check-post checks. Stop and report if anything is blocking.
2. Set `draft: false`. Set `date` to today unless Caleb gave a date. If the folder name's date no longer matches, `git mv` the folder so they agree.
3. Commit as `Publish: <title>`.
4. `git checkout main && git pull && git merge --no-ff post/<slug> -m "Publish: <title>" && git push`.
5. Delete the branch locally and on the remote.
6. Wait for the production deployment, then confirm `https://calebtrainer.dev/posts/<folder>/` returns 200 and shows the title. Also confirm the post appears in `https://calebtrainer.dev/index.xml`.
7. Reply with the live URL and a one-line description he can paste when sharing it. Write that line plainly, following the writing rules.
