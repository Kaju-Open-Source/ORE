from pathlib import Path

import pytest

SAMPLE_PDF = Path(__file__).resolve().parent / "data" / "sample.pdf"


@pytest.fixture(scope="session")
def sample_pdf():
    assert SAMPLE_PDF.exists(), f"missing test fixture: {SAMPLE_PDF}"
    return SAMPLE_PDF
