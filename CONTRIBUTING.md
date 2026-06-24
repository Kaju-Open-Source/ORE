# Contributing to ORE

Welcome! ORE is split into **three folders**, one per team. Pick yours,
read only that section, then jump to [`COMMANDS.md`](COMMANDS.md) for
every shell command.

| Team        | Folder        | You write             | You never touch         |
|-------------|---------------|-----------------------|-------------------------|
| 🤖 AI       | `ai-rag/`     | Python + Ollama glue  | `backend/`, `frontend/` |
| 🧠 Backend  | `backend/`    | HTTP API (FastAPI)    | `ai-rag/`, `frontend/`  |
| 🎨 Frontend | `frontend/`   | Next.js UI            | `ai-rag/`, `backend/`   |

> **New to Python?** The AI team's code is just four `.py` files at the
> top of `ai-rag/` — no sub-packages, no `__init__.py`, no fancy imports.
> Open one, read top-to-bottom.

---

## Ground rules (all teams)

1. **Stay in your folder.** If your change needs to touch another team's
   folder, stop and open an issue first.
2. **Read [`COMMANDS.md`](COMMANDS.md).** Every command you need is
   there, copy-paste-able. No `make`, no build tool.
3. **Tests + lint must pass** before opening a PR:
   - Python: `cd ai-rag && pytest -q -m "not network" && ruff check .`
   - Backend: `cd backend && pytest -q && ruff check .`
   - Frontend: `cd frontend && npm run lint`
4. **Bump the version** in `pyproject.toml` whenever you change a public
   Python API or HTTP route. Mention it in the PR title: `feat(ai): … · v0.5`.

---

## 🤖 AI team — `ai-rag/`

You own: `ingestion.py`, `chunking.py`, `embedding.py`,
and their tests.

You ship a **Python package**. The Backend team installs it with
`pip install -e ./ai-rag`. The Backend team is your downstream customer.

→ Full details: [`ai-rag/README.md`](ai-rag/README.md)

## 🧠 Backend team — `backend/`

You own: the FastAPI app and its HTTP routes.

You wrap the AI package in HTTP routes. The Frontend team consumes
those routes — they **never** import from `ai-rag/` directly.

Every route you add or change goes in the **API contract**:

> 📄 `docs/GETTING-STARTED.md` lists the contract file (it doesn't exist
> yet — open an issue to start it).

→ Full details: [`backend/README.md`](backend/README.md)

## 🎨 Frontend team — `frontend/`

You own: the Next.js app under `frontend/`.

You talk to the Backend **only** through the routes declared in the API
contract. If you need a new field in a response, open an issue tagged
`team:backend`.

→ Full details: [`frontend/README.md`](frontend/README.md)

---

## 🌿 Branch + PR workflow

1. Branch: `git switch -c <type>/<scope>-<thing>`
   - Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.
2. Keep the PR scoped to **one team's folder**.
3. CI green + at least one approving review from your team.
4. Linked issue: `Closes #123` in the PR body.

## 🐛 Bugs · 💡 Features

Open an issue. Tag the owning team: `team:ai`, `team:backend`,
`team:frontend`. Use the templates if they exist.
