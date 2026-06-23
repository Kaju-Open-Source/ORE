# 🤖 AI team — `ai-rag/`

This folder is the **AI team's home**. It owns the Python pipeline that
turns PDFs into chunks and embeddings. Retrieval and the chat API will
land here later.

> **Before contributing, read [`../CONTRIBUTING.md`](../CONTRIBUTING.md).**
> It explains the team workflow, what you can edit, and how to hand off
> changes to the Backend team.

---

## What's in here (you can read the whole folder in 60 seconds)

```text
ai-rag/
├── ingestion.py     📄 PDF → text            (read a document)
├── chunking.py      ✂️  text → chunks          (split into pieces)
├── embedding.py     🧠 text → vectors          (turn text into numbers)
├── config.py        ⚙️  settings               (env vars, nothing else)
│
├── tests/
│   ├── data/sample.pdf
│   ├── test_ingestion.py
│   ├── test_chunking.py
│   └── test_embedding.py
│
├── pyproject.toml    # pip reads this
├── requirements.txt  # plain-pip mirror of runtime deps
├── Makefile          # make test, make lint, …
├── .env.example
├── .gitignore
├── LICENSE
└── README.md         # ← you are here
```

**No sub-packages. No `__init__.py`. No `src/` folder.**
Four Python files at the top. That's it.

---

## ⚡ Quick start

```bash
cd ai-rag
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Required: Ollama running locally with one model pulled.
ollama serve &
ollama pull nomic-embed-text
```

Then in Python:

```python
from ingestion import extract_pdf_text
from chunking  import create_chunks
from embedding import get_embeddings

text   = extract_pdf_text("documents/sample.pdf")
chunks = create_chunks(text)
vecs   = get_embeddings(chunks)
```

---

## 🧪 Run the tests

```bash
make test        # fast, offline tests only
make test-net    # also run tests that need Ollama running
make lint        # ruff
```

---

## ⚙️ Settings (`.env.example`)

| Variable                  | Default                 | What it does                |
|---------------------------|-------------------------|-----------------------------|
| `ORERAG_OLLAMA_HOST`      | `http://127.0.0.1:11434`| Where Ollama is running     |
| `ORERAG_EMBED_MODEL`      | `nomic-embed-text`      | Embedding model to use      |
| `ORERAG_CHUNK_SIZE`       | `1000`                  | Chunk size in characters    |
| `ORERAG_CHUNK_OVERLAP`    | `200`                   | Overlap between chunks      |
| `ORERAG_DOCUMENTS_DIR`    | `./documents`           | Default docs folder         |

Only one rule: **`config.py` is the only file that reads environment
variables.** Add new settings there.

---

## 📄 License

MIT © Kaju Open Source. See [`../LICENSE`](../LICENSE).
