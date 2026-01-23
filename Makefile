.PHONY: help install install-dev run test clean venv setup

help:
	@echo "AI Governance Assessment - Makefile Commands"
	@echo ""
	@echo "Setup Commands:"
	@echo "  make setup          - Complete project setup (venv + install)"
	@echo "  make venv           - Create virtual environment"
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install development dependencies"
	@echo ""
	@echo "Development Commands:"
	@echo "  make run            - Run Flask development server"
	@echo "  make test           - Run test suite"
	@echo "  make lint           - Run linters (flake8, black check)"
	@echo "  make format         - Format code with black"
	@echo ""
	@echo "Deployment Commands:"
	@echo "  make deploy-heroku  - Deploy to Heroku"
	@echo ""
	@echo "Cleanup Commands:"
	@echo "  make clean          - Remove temporary files"
	@echo "  make clean-all      - Remove venv and temporary files"

# Setup
setup: venv install
	@echo "✓ Setup complete!"
	@echo "Run: source venv/bin/activate && make run"

venv:
	python3 -m venv venv
	@echo "✓ Virtual environment created"
	@echo "Activate with: source venv/bin/activate"

install:
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	@echo "✓ Dependencies installed"

install-dev:
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements-dev.txt
	@echo "✓ Development dependencies installed"

# Development
run:
	@echo "Starting Flask development server..."
	@echo "Open: http://localhost:5000"
	venv/bin/python app.py

test:
	venv/bin/python test_webapp.py

lint:
	@echo "Running flake8..."
	venv/bin/flake8 app.py src/
	@echo "Checking black formatting..."
	venv/bin/black --check app.py src/

format:
	@echo "Formatting with black..."
	venv/bin/black app.py src/

# Deployment
deploy-heroku:
	@echo "Deploying to Heroku..."
	git push heroku main

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache htmlcov .coverage
	@echo "✓ Temporary files removed"

clean-all: clean
	rm -rf venv
	@echo "✓ Virtual environment removed"
