"""Tests for embedding.py

Most tests need a running Ollama daemon. They are marked ``network`` and
skipped by default; run with::

    pytest -m network

A tiny pure-Python test (model-name plumbing) runs without Ollama.
"""

import pytest

from embedding import DEFAULT_EMBED_MODEL, get_embedding, get_embeddings


def test_default_model_is_nomic_embed_text():
    """The default embedding model is documented; pin it."""
    assert DEFAULT_EMBED_MODEL == "nomic-embed-text"


def test_get_embedding_empty_text_raises():
    with pytest.raises(ValueError):
        get_embedding("")
    with pytest.raises(ValueError):
        get_embedding("   \n  ")


@pytest.mark.network
def test_get_embedding_returns_vector():
    """Requires Ollama running with nomic-embed-text pulled."""
    v = get_embedding("hello world")
    assert isinstance(v, list)
    assert len(v) > 0
    assert all(isinstance(x, float) for x in v)


@pytest.mark.network
def test_get_embeddings_filters_empty():
    out = get_embeddings(["a", "", "  ", "b"])
    assert len(out) == 2
    assert all(len(v) > 0 for v in out)


@pytest.mark.network
def test_get_embeddings_empty_input_returns_empty():
    assert get_embeddings([]) == []
    assert get_embeddings(["", "   "]) == []
