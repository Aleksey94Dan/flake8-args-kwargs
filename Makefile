SHELL:=/usr/bin/env bash

.PHONY: install
install:
	poetry install


.PHONY: lint
lint:
	poetry run flake8 .
	poetry run mypy .

.PHONY: unit
unit:
	poetry run pytest

.PHONY: test
test: lint unit

