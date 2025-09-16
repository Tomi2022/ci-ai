# Makefile for CI-AI

# Variables
PYTHON=python3
VENV=.venv

# Default target
help:
	@echo "Available commands:"
	@echo "  make venv        Create virtual environment and install dependencies"
	@echo "  make run         Run inference stub"
	@echo "  make rebirth     Run rebirth cycle (stub mode)"
	@echo "  make clean       Remove caches and temporary files"
	@echo "  make docker      Build Docker image"
	@echo "  make compose     Start with docker-compose"

venv:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
	$(PYTHON) inference.py "Hello, who are you?"

rebirth:
	./rebirth.sh --base base-v0 --since 2025-09-01

clean:
	rm -rf __pycache__ .pytest_cache *.pyc *.pyo */__pycache__ .venv

docker:
	docker build -t ci-ai .

compose:
	docker compose up -d
