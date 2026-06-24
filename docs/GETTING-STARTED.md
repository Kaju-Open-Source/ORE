# Getting started

> New to ORE? Read this once, then jump to your team's README.

---

## 0. Pick your team

| Folder      | Team         | Stack                          |
|-------------|--------------|--------------------------------|
| `ai-rag/`   | 🤖 AI         | Python · Ollama                |
| `backend/`  | 🧠 Backend    | FastAPI (scaffolded)           |
| `frontend/` | 🎨 Frontend   | Next.js · React · TypeScript   |

Don't know which team? Ask your lead. The rules are in
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## 1. Clone

```bash
git clone https://github.com/kajuopensource/ore
cd ore
```

## 2. Open your team's README

- 🤖 AI: [`../ai-rag/README.md`](../ai-rag/README.md)
- 🧠 Backend: [`../backend/README.md`](../backend/README.md)
- 🎨 Frontend: [`../frontend/README.md`](../frontend/README.md)

## 3. Smoke test

| Team         | Command                                              | Expected                     |
|--------------|------------------------------------------------------|------------------------------|
| 🤖 AI        | `cd ai-rag && pytest -q -m "not network"`            | `10 passed, 3 deselected`       |
| 🧠 Backend   | `cd backend && pytest -q`                            | (no smoke test yet)          |
| 🎨 Frontend  | `cd frontend && npm run dev`                         | opens `localhost:3000`       |

If your smoke test fails, **stop and ask in the team channel.** Don't
edit random files trying to "fix" it.

## 4. Pick a first issue

Look for issues tagged `good first issue` and `team:<your-team>`.
Open a branch, make a small change, push, open a PR.

## ❓ FAQ

**I'm new to Python on the AI team. Where do I start?**
The four files at the top of `ai-rag/` are flat — no sub-packages, no
fancy imports. Open `ingestion.py`, read it, you'll get it.

**My change needs to touch two folders.**
Stop. Open an issue first. See CONTRIBUTING.md § Cross-team changes.

**Where do I report a bug?**
GitHub Issues. Tag the owning team.
