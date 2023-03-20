lint:
	poetry run flake8

format:
	poetry run black .

check-format:
	poetry run black . --check

check-all: lint check-format

check-all-then-build: format lint run-dev

run-dev:
	poetry run python manage.py runserver --settings=backend.settings.development

run-prod:
	poetry run python manage.py runserver --settings=backend.settings.production
