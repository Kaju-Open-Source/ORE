"""
config.py

Read settings from environment variables (or a `.env` file).

This is the ONLY file in the project that should read `os.environ`.
Every other module gets its config by calling `get_settings()`.

Available settings (with their env variable name):
    ollama_host    ORERAG_OLLAMA_HOST     (default: http://127.0.0.1:11434)
    embed_model    ORERAG_EMBED_MODEL     (default: nomic-embed-text)
    chunk_size     ORERAG_CHUNK_SIZE      (default: 1000)
    chunk_overlap  ORERAG_CHUNK_OVERLAP   (default: 200)
    documents_dir  ORERAG_DOCUMENTS_DIR   (default: ./documents)
"""

import os
from dataclasses import dataclass, field
from pathlib import Path


def _project_path(*parts):
    """Resolve a path relative to the ai-rag/ project folder."""
    # ai-rag/config.py -> ai-rag/
    return Path(__file__).resolve().parent.joinpath(*parts)


@dataclass(frozen=True)
class Settings:
    """All runtime settings for the ORERAG pipeline."""

    ollama_host: str = field(
        default_factory=lambda: os.environ.get("ORERAG_OLLAMA_HOST", "http://127.0.0.1:11434")
    )
    embed_model: str = field(
        default_factory=lambda: os.environ.get("ORERAG_EMBED_MODEL", "nomic-embed-text")
    )
    chunk_size: int = field(
        default_factory=lambda: int(os.environ.get("ORERAG_CHUNK_SIZE", "1000"))
    )
    chunk_overlap: int = field(
        default_factory=lambda: int(os.environ.get("ORERAG_CHUNK_OVERLAP", "200"))
    )
    documents_dir: Path = field(
        default_factory=lambda: Path(
            os.environ.get("ORERAG_DOCUMENTS_DIR", str(_project_path("documents")))
        )
    )


def get_settings():
    """Return a fresh Settings object (re-reads env vars)."""
    return Settings()
