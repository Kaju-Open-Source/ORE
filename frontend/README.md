# 🎨 Frontend team — `frontend/`

This is the **Frontend team's home** — a Next.js 16 + React 19 app
styled with Tailwind v4.

Before contributing, read [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
It covers how the Frontend talks to the Backend **only** through the
HTTP routes declared in [`../docs/API.md`](../docs/API.md) — never by
importing from `ai-rag/` directly.

---

## 🚀 Quick start

```bash
cd frontend
npm install
npm run dev
```

Open <http://localhost:3000>.

## 🧪 Other commands

```bash
npm run build      # production build
npm run start      # serve the production build
npm run lint       # eslint
```

## 📂 What's in here

```text
frontend/
├── app/                # Next.js App Router (pages live here)
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── public/             # static assets
├── package.json
├── tsconfig.json
├── eslint.config.mjs
└── README.md           # ← you are here
```

## Boundaries

- **Only the Frontend team** edits this folder.
- Talk to the Backend through the routes in `docs/API.md`. If you need
  a new field in a response, open an issue tagged `team:backend`.
- **Never import from another team's folder** — there is no Node port
  of `ai-rag/`, and there shouldn't be.
