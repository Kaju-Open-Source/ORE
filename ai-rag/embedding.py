"""
embedding.py

Turn text into numbers (vectors) using a local embedding model.

This is the THIRD step of the ORERAG pipeline.

Public functions:
    get_embedding("hello")        -> [0.12, -0.04, ...]   # one vector
    get_embeddings(["a", "b"])    -> [[...], [...]]       # many at once

We use Ollama running on your machine. Install it from
https://ollama.com/download, then run:

    ollama pull nomic-embed-text
"""

import ollama

from config import get_settings

DEFAULT_EMBED_MODEL = "nomic-embed-text"


def get_embedding(text, model=None):
    """
    Return the embedding vector for a single piece of text.

    Raises ValueError if `text` is empty or whitespace-only.
    """
    if not text or not text.strip():
        raise ValueError("get_embedding() requires non-empty text.")
    model = model or get_settings().embed_model

    response = ollama.embed(model=model, input=text)
    return response["embeddings"][0]


def get_embeddings(texts, model=None):
    """
    Return embedding vectors for many texts at once (one Ollama call).

    Empty / whitespace-only strings are silently skipped.
    """
    texts = [t for t in texts if t and t.strip()]
    if not texts:
        return []
    model = model or get_settings().embed_model

    response = ollama.embed(model=model, input=texts)
    return response["embeddings"]
