# Getting started

> New to ORE? Read this first. It's the shortest path from `git clone`
> to a useful first commit — even if you're not a Python person.

---

## 0. Pick your team

ORE is split into three independent folders. You only need to learn the
one your team owns:

| Folder        | Team        | Stack                          | Public surface           |
|---------------|-------------|--------------------------------|--------------------------|
| `ai-rag/`     | 🤖 AI        | Python · Ollama · LangChain    | Python package           |
| `backend/`    | 🧠 Backend   | (TBD)                          | HTTP API                 |
| `frontend/`   | 🎨 Frontend  | Next.js · React · TypeScript   | Web UI                   |

If you don't know which team you're on, ask your lead. The full rules
are in [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## 1. Clone + open the repo

```bash
git clone https://github.com/kajuopensource/ore
cd ore
```

You'll see three folders. **Open only yours.**

## 2. Open your team's README

- 🤖 AI: [`../ai-rag/README.md`](../ai-rag/README.md)
- 🧠 Backend: [`../backend/README.md`](../backend/README.md)
- 🎨 Frontend: [`../frontend/README.md`](../frontend/README.md)

Each one is short. Follow the setup section.

## 3. Make sure the basics work

| Team  | Smoke test                                                   |
|-------|--------------------------------------------------------------|
| 🤖 AI    | `cd ai-rag && make test`   — should print `10 passed`        |
| 🧠 Backend | (no smoke test yet — open an issue)                    |
| 🎨 Frontend | `cd frontend && npm run dev` — should open `localhost:3000` |

If your smoke test doesn't pass, **stop and ask in the team channel.**
Don't try to "fix it" by editing random files — usually it's a missing
system dependency or a stale venv.

## 4. Pick a first task

Open the issue tracker and look for issues tagged with your team:
`team:ai`, `team:backend`, `team:frontend`. Pick one labelled
`good first issue` if you're new.

## 5. Open a PR

The PR workflow is in [`../CONTRIBUTING.md`](../CONTRIBUTING.md) §
"Branch + PR workflow". TL;DR:

1. Branch: `git switch -c feat/<scope>-<thing>`
2. Commit small, focused changes inside **your team's folder**.
3. Push + open a PR. Mention the issue number with `Closes #123`.
4. At least one teammate from your team must approve.

---

## ❓ FAQ

**I'm a Python beginner on the AI team. Where do I start?**
Read [`../ai-rag/README.md`](../ai-rag/README.md) — the four files at
the top (`ingestion.py`, `chunking.py`, `embedding.py`, `config.py`)
are deliberately small and flat. No sub-packages, no `__init__.py`,
no fancy imports. Open one, read top-to-bottom, and you'll get it.

**I broke a test I don't understand.**
Revert with `git checkout -- .` and ask in your team channel. Don't
push a "fix" you can't explain.

**My change needs to touch two folders.**
Stop. Open an issue first. See `CONTRIBUTING.md` § Cross-team changes.

**Where do I report a bug?**
GitHub Issues: <https://github.com/kajuopensource/ore/issues>.
Tag the owning team.
