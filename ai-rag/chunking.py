"""
chunking.py

Split a long piece of text into smaller, overlapping chunks.

This is the SECOND step of the ORERAG pipeline.

Public functions:
    create_chunks(text) -> ["chunk 1", "chunk 2", ...]
    chunk_pages(pages)  -> [{"chunk_id": 1, "page": 1, "text": "..."}]

Why chunk?
    Embedding models have a maximum input size. Splitting long documents
    into ~1000-character chunks lets us embed them safely while keeping
    a small overlap so context isn't lost at chunk boundaries.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def _splitter(chunk_size=1000, chunk_overlap=200):
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


def create_chunks(text, chunk_size=1000, chunk_overlap=200):
    """
    Split a flat text blob into overlapping chunks.

    Default: 1000 characters per chunk, 200 characters of overlap.

    Returns a list of strings. Empty / whitespace-only input returns [].
    """
    if not text or not text.strip():
        return []
    return _splitter(chunk_size, chunk_overlap).split_text(text)


# Alias: "I have text, not pages" intent.
chunk_text = create_chunks


def chunk_pages(pages, chunk_size=500, overlap=50):
    """
    Split a list of {page, text} dicts into chunks that remember which
    page they came from.

    Each output dict has:
        {
            "chunk_id": 1,           # globally unique, starts at 1
            "page":     3,           # which page the text came from
            "text":     "..."        # the chunk itself
        }

    Use this when you want to show citations like "(see page 3)".
    """
    out = []
    chunk_id = 1
    step = max(chunk_size - overlap, 1)

    for page in pages:
        text = page.get("text", "") or ""
        page_num = page.get("page", 0)
        if not text:
            continue

        start = 0
        n = len(text)
        while start < n:
            out.append(
                {
                    "chunk_id": chunk_id,
                    "page": page_num,
                    "text": text[start : start + chunk_size],
                }
            )
            chunk_id += 1
            start += step

    return out
