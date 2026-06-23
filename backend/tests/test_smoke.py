"""Backend smoke test."""
from fastapi.testclient import TestClient

from app.main import app


def test_root():
    c = TestClient(app)
    r = c.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "online"


def test_health():
    c = TestClient(app)
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
