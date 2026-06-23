"""FastAPI app for the ORE backend (scaffold).

Run:
    uvicorn app.main:app --reload --port 8000
or:
    make run
"""
from fastapi import FastAPI

app = FastAPI(
    title="ORE Backend",
    description="HTTP API for the ORE platform (Kaju Open Source).",
    version="0.0.1",
)


@app.get("/")
def root():
    return {"status": "online", "service": "ore-backend"}


@app.get("/health")
def health():
    return {"status": "ok"}
