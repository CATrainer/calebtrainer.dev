#!/usr/bin/env bash
# Vercel runs this for every deployment (see vercel.json).
# main -> production build, drafts hidden.
# any other branch -> preview build, drafts visible.
set -euo pipefail

QUARTO_VERSION="$(grep -E '^quarto-cli==' requirements.txt | cut -d= -f3)"

if ! command -v quarto >/dev/null 2>&1; then
  echo "Installing Quarto ${QUARTO_VERSION}"
  url="https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"
  if curl -fsSL "$url" -o /tmp/quarto.tar.gz; then
    mkdir -p /tmp/quarto
    tar -xzf /tmp/quarto.tar.gz -C /tmp/quarto --strip-components=1
    export PATH="/tmp/quarto/bin:$PATH"
  else
    echo "Release download failed, falling back to pip"
    python3 -m venv /tmp/qvenv
    /tmp/qvenv/bin/pip install --quiet "quarto-cli==${QUARTO_VERSION}"
    export PATH="/tmp/qvenv/bin:$PATH"
  fi
fi

quarto --version

if [ "${VERCEL_ENV:-preview}" = "production" ]; then
  quarto render
else
  quarto render --profile preview
fi
