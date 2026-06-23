"""Shared pytest fixtures for ORERAG tests.

These tests are fully offline — they exercise the ingestion / chunking
modules without ever calling Ollama or ChromaDB.
"""

from pathlib import Path

import pytest

# Sample PDF committed under tests/data/ for offline ingestion tests.
SAMPLE_PDF = Path(__file__).resolve().parent / "data" / "sample.pdf"


@pytest.fixture(scope="session")
def sample_pdf():
    """Path to the small sample PDF shipped under tests/data/."""
    assert SAMPLE_PDF.exists(), f"missing test fixture: {SAMPLE_PDF}"
    return SAMPLE_PDF
