# Contributing to ORE

Welcome to **ORE** (Kaju Open Source)! 🎉

This repository hosts **three independent sub-projects** that together
make up the platform. **Pick your team and read only that section.**

| Team        | Folder        | Tech                                            | Public interface             |
|-------------|---------------|-------------------------------------------------|------------------------------|
| 🤖 **AI**       | `ai-rag/`     | Python, Ollama                                  | `import ingestion` etc.      |
| 🧠 **Backend**  | `backend/`    | (TBD — see `backend/README.md`)                 | HTTP API the Frontend calls  |
| 🎨 **Frontend** | `frontend/`   | Next.js 16, React 19, Tailwind v4, TypeScript   | UI at `localhost:3000`       |

The **AI team** ships a Python package. The **Backend team** wraps that
package in HTTP routes. The **Frontend team** consumes those routes. They
**never** share code directly — only contracts (docs and HTTP).

> **Heads-up: Python is not a hard requirement for this repo.** The AI
> team's four `.py` files live at the top level of `ai-rag/` with **no
> sub-packages, no `__init__.py`, no `src/` folder**. If you can read a
> flat folder, you can read this codebase.

---

## 🚀 One-time setup (everyone)

```bash
git clone https://github.com/Kaju-Open-Source/ORE
cd ore
```

**Never commit inside another team's folder** without their approval.

---

## 🤖 AI team — `ai-rag/`

> Owns: ingestion, chunking, embedding (today).
> Will own: retrieval, storage, RAG chat (later).

### Setup

```bash
cd ai-rag
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Required local service:
ollama serve           # leave running
ollama pull nomic-embed-text
```

### What's in this folder (the only file layout you need to know)

```text
ai-rag/
├── ingestion.py     📄 PDF -> text     — read a document
├── chunking.py      ✂️  text -> chunks  — split into pieces
├── embedding.py     🧠 text -> vectors  — turn text into numbers
├── config.py        ⚙️  settings        — env vars, nothing else
│
├── tests/                              — pytest, fully offline
│   ├── data/sample.pdf
│   ├── test_ingestion.py
│   ├── test_chunking.py
│   └── test_embedding.py
│
├── pyproject.toml    # pip reads this
├── requirements.txt  # mirror of runtime deps (plain pip)
├── Makefile          # `make test`, `make lint`, …
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

**That's it.** Four Python files at the top level. No sub-packages to
navigate, no `__init__.py` to wonder about.

### Where to put new code

| You want to…                  | Edit this file            |
|-------------------------------|---------------------------|
| Improve PDF reading           | `ingestion.py`            |
| Add a chunking strategy       | `chunking.py`             |
| Change the embedding model    | `embedding.py` + `config.py` |
| Add a new setting (env var)   | `config.py` only          |
| Write tests for any of the above | add a file under `tests/` |

**Don't add new top-level `.py` files without an issue first** — we want
to keep this folder small and obvious.

### Day-to-day commands

```bash
make install        # editable install + dev deps
make test           # fast, offline tests only
make test-net       # also run tests that need Ollama
make lint           # ruff
```

### Coding rules (the short version)

- **Docstring** on every public function (one-line summary is fine).
- **Type hints** on every public function.
- **Imports** use the flat names: `from chunking import create_chunks`.
- **`config.py` is the only file that reads `os.environ`.**
- **Tests that need Ollama** are marked `@pytest.mark.network` and don't
  run by default (`make test` skips them).
- If you're unsure, **open an issue first**. We're friendly.

### Hand-off to Backend

When you change a public function signature, bump the version in
`pyproject.toml` (semver) and call it out in the PR title, e.g.
`feat(ai): add chunking tokens · v0.5`.

---

## 🧠 Backend team — `backend/`

> Owns: the HTTP API the Frontend consumes.
> Status: scaffolded, not implemented yet.

### Setup (when implementation starts)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e .
# In a second terminal (or the same venv):
pip install -e ../ai-rag     # consume the AI package as a library
```

### Boundaries

- The Backend is the **only** team that imports `ai-rag/` as a library.
- The Backend is **forbidden** from editing anything inside `ai-rag/`.
  If you need a new AI capability, open an issue tagged `team:ai`.

### Talking to the AI team

- AI ships Python **functions**, not endpoints. Your job is to wrap them.
- AI returns plain Python types (`list[str]`, `dict`, …) — keep responses
  JSON-serialisable.
- For async work or batch ingestion, agree on the **request schema** in
  `docs/API.md` **before** implementing.

### Hand-off to Frontend

When you add or change an HTTP route, update `docs/API.md` **in the same
PR**. Frontend treats that doc as the source of truth — if it's not
there, the route doesn't exist.

---

## 🎨 Frontend team — `frontend/`

> Owns: the Next.js UI at `localhost:3000`.

### Setup

```bash
cd frontend
npm install
npm run dev
```

Open <http://localhost:3000>.

### Boundaries

- The Frontend is the **only** team that edits `frontend/`.
- The Frontend talks to the Backend **only** through routes declared in
  `docs/API.md`. No direct calls into `ai-rag/`.
- **Never import from another team's folder.** If you need data the AI
  pipeline produces, ask the Backend team to expose it.

---

## 🔁 Cross-team changes

Some PRs genuinely span teams (e.g. "add citation-aware answers" needs
AI + Backend + Frontend). Process:

1. **Open an issue first**, tag all three teams.
2. **One team owns the PR** — usually the one whose code changes most.
3. Other teams review and co-approve.
4. PR description must list **what each team ships**.

Even small cross-team work follows this flow.

---

## 🌿 Branch + PR workflow

1. Branch from `main`: `git switch -c <type>/<scope>-<thing>`
   - Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.
   - Example: `feat/ai-embedding-batch`, `fix/backend-chat-500`.
2. Keep PRs scoped to **one team's folder** unless the issue is
   explicitly cross-team.
3. CI must be green: tests + lint.
4. Update the docs that live with your team's folder:
   - AI → `ai-rag/README.md`
   - Backend → `backend/README.md` and `docs/API.md`
   - Frontend → `frontend/README.md`
5. At least one approving review from a teammate **on the same team**.

---

## 🐛 Bug reports · 💡 Feature requests

Open an issue at <https://github.com/kajuopensource/ore/issues>.
Tag the owning team: `team:ai`, `team:backend`, `team:frontend`.

## 📜 License

By contributing you agree your work is MIT-licensed, same as the project.
