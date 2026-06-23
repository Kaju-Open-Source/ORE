# 🧠 Backend team — `backend/`

> Status: **scaffolded, not implemented yet.** The AI pipeline is
> landing first; this folder will hold the HTTP API the Frontend calls.

Before contributing, read [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
It explains how the Backend team talks to the AI team (via the
`ai-rag/` Python package) and how it talks to the Frontend team (via
[`../docs/API.md`](../docs/API.md)).

---

## Planned layout

```text
backend/
├── app/             # FastAPI / Flask app
├── tests/
├── pyproject.toml
├── requirements.txt
├── .env.example
└── README.md        # ← you are here
```

## Planned setup

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .
pip install -e ../ai-rag   # consume the AI package as a library
```

## Boundaries

- **Only the Backend team** edits this folder.
- The Backend is the **only** team that imports `ai-rag/`.
- The Backend is **forbidden** from editing anything inside `ai-rag/`.
- For every HTTP route you add or change, update
  [`../docs/API.md`](../docs/API.md) in the same PR — Frontend treats
  it as the source of truth.
