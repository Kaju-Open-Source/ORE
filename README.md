# ORE — Kaju Open Source

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-early--alpha-yellow)](#)

ORE turns academic documents into a shared, searchable, AI-powered
knowledge repository. **Three teams** build it together, each owning a
separate folder:

```text
ore/
├── ai-rag/       🤖 AI team       — Python + Ollama (ingestion / chunking / embedding)
├── backend/      🧠 Backend team   — HTTP API (coming soon)
├── frontend/     🎨 Frontend team  — Next.js 16 UI (coming soon)
├── docs/         📚 shared docs (API contract, architecture)
├── CONTRIBUTING.md    ← start here
├── LICENSE
└── README.md          ← you are here
```

---

## 🚀 I just cloned the repo — what now?

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md). It's short and tells you
   which team you are on.
2. Open **your team's folder** below and follow its README.

| You are on…         | Open this folder        | Tech you'll touch                |
|---------------------|-------------------------|----------------------------------|
| 🤖 **AI team**       | [`ai-rag/`](ai-rag/)    | Python · Ollama · LangChain      |
| 🧠 **Backend team**  | [`backend/`](backend/)  | (TBD — see `backend/README.md`)  |
| 🎨 **Frontend team** | [`frontend/`](frontend/)| Next.js 16 · React 19 · Tailwind |

**Don't edit another team's folder.** If your change spans teams, open
an issue first — see `CONTRIBUTING.md` § Cross-team changes.

---

## 📚 Shared docs

- [`docs/GETTING-STARTED.md`](docs/GETTING-STARTED.md) — new contributor? start here (even non-Python folks).
- [`docs/API.md`](docs/API.md) — the HTTP contract between Backend and
  Frontend. Treat it as the single source of truth.
- [`docs/architecture.png`](docs/architecture.png) — high-level diagram.

---

## 📄 License

MIT © Kaju Open Source. See [LICENSE](LICENSE).
