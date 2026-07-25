.PHONY: install format lint typecheck test coverage clean

install:
	pip install -e ".[dev]"

format:
	black markrethe/ tests/

lint:
	flake8 markrethe/ tests/

typecheck:
	mypy markrethe/

test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=markrethe --cov-report=html --cov-report=term

clean:
	rm -rf .pytest_cache .mypy_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
