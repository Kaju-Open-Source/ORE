from ingestion import extract_pages
from chunking import chunk_pages
from vector_store import store_chunk
from retriever import retrieve_context
from generation.answer_questions import answer_questions

pdf_path = "./tests/data/sample.pdf"

pages = extract_pages(pdf_path)

chunks = chunk_pages(pages)

for i, chunk in enumerate(chunks):
    store_chunk(
        chunk_id=i,
        text=chunk["text"],
        page=chunk["page"]
    )


question = input("Ask a Question")
ans = answer_questions(question)
print("Answer : "+ans)

