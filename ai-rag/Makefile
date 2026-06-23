# ORE AI-RAG - developer convenience commands.

.PHONY: help install dev test lint clean clean-pyc

help:
	@echo "ORERAG make targets:"
	@echo "  make install  pip install -e .[dev]"
	@echo "  make test     run pytest (offline tests only by default)"
	@echo "  make test-net run pytest including tests that hit Ollama"
	@echo "  make test-cov run pytest with coverage"
	@echo "  make lint     run ruff"
	@echo "  make clean    remove caches + build artifacts"

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

dev:
	pip install -e ".[dev]"

test:
	pytest -q

test-net:
	pytest -q -m network

test-cov:
	pytest --cov=orerag --cov-report=term-missing

lint:
	ruff check src tests

clean-pyc:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov

clean: clean-pyc
