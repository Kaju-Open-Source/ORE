# 🤖 AI team — `ai-rag/`

This is the **AI team's home**. Three Python files at the top
level turn PDFs into embeddings:

```text
ingestion.py     📄 PDF → text
chunking.py      ✂️  text → chunks
embedding.py     🧠 text → vectors (Ollama)
```

No sub-packages. No `__init__.py`. No `src/` folder. No settings file.

---

## Run it

See [`../COMMANDS.md`](../COMMANDS.md) § "AI team" for setup, tests,
lint, and a copy-paste Python snippet.

> **TL;DR** for the impatient:
> ```bash
> cd ai-rag
> python3 -m venv .venv && source .venv/bin/activate
> pip install -e ".[dev]"
> pytest -q -m "not network"      # 10 passed, 3 deselected
> ```

`pytest` works from inside `ai-rag/` because `pyproject.toml` sets
`pythonpath = ["."]`. If you ever want to run it from the repo root,
use `pytest ai-rag/tests` instead.

## Change the embedding model

The default is `nomic-embed-text`. To use a different Ollama model,
either:

- set the env var `ORERAG_EMBED_MODEL=<your-model>`, **or**
- pass it per call: `get_embedding(text, model="<your-model>")`.

## Bump the version

Edit `version = "…"` in `pyproject.toml`. Use semver. Mention the new
version in your PR title (`feat(ai): … · v0.5`).

## Hand off to Backend

When you change a public function signature, treat it like a breaking
change. Bump the major version, call it out in the PR, ping the
Backend team in your team's channel.
