.PHONY: help install dev test lint run

help:
	@echo "Backend targets:"
	@echo "  make install  pip install -e .[dev]"
	@echo "  make test     pytest"
	@echo "  make lint     ruff check"
	@echo "  make run      uvicorn app.main:app --reload"

install:
	pip install -e ".[dev]"

dev:
	pip install -e ".[dev]"
	pip install -e ../ai

test:
	pytest -q

lint:
	ruff check .

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
