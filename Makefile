.PHONY: up down shell lint format check

up:
	docker compose up -d
down:
	docker compose down
shell:
	docker compose exec app sh
lint:
	uv run flake8 .
format:
	uv run black .
	uv run black .
check:
	uv run isort --check-only --diff .
	uv run black --check --diff .
	uv run flake8 .
