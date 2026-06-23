"""
ingestion.py

Load a PDF and turn it into text.

This is the FIRST step of the ORERAG pipeline.

Public functions:
    extract_pages(pdf_path) -> [{"page": int, "text": str}, ...]
    extract_pdf_text(pdf_path) -> str

Quick example:
    from ingestion import extract_pdf_text
    text = extract_pdf_text("documents/sample.pdf")
"""

import fitz  # PyMuPDF


def extract_pages(pdf_path):
    """
    Read a PDF and return one dict per page.

    Each dict looks like:
        {"page": 1, "text": "First page text..."}

    Page numbers start at 1 (the way humans count).
    """
    pdf_path = str(pdf_path)
    doc = fitz.open(pdf_path)
    pages = []
    try:
        for page_num, page in enumerate(doc):
            pages.append(
                {
                    "page": page_num + 1,
                    "text": page.get_text() or "",
                }
            )
    finally:
        doc.close()
    return pages


def extract_pdf_text(pdf_path):
    """
    Read a PDF and return ALL of its text as one big string.

    Pages are joined with newlines. Use this when you don't care which
    page a piece of text came from.
    """
    pages = extract_pages(pdf_path)
    return "\n".join(p["text"] for p in pages).strip() + "\n"
