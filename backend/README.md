# 🧠 Backend team — `backend/`

Status: **scaffolded.** A tiny FastAPI app and one smoke test live here
so the team has something to run while the real implementation lands.

## Run it

See [`../COMMANDS.md`](../COMMANDS.md) § "Backend team" for setup,
tests, lint, and how to start `uvicorn`.

## When you start implementing

- You are the **only** team that imports `ai-rag/` as a library.
  Install it with `pip install -e ../ai-rag` (already in COMMANDS.md).
- For every HTTP route you add, update the API contract doc — it lives
  in the `docs/` folder. (Doesn't exist yet — open an issue to start.)
- You are **forbidden** from editing anything inside `ai-rag/`. If you
  need new AI capability, open an issue tagged `team:ai`.
