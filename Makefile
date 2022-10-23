.DEFAULT_GOAL := help

.PHONY: check
check:  ## Check code formatting and import sorting
	python3 -m black --check .
	python3 -m isort --check .
	python3 -m flake8
	python3 -m mypy .
	python3 -m bandit --quiet --recursive --exclude tests .
	python3 -m pip_audit --require-hashes --requirement requirements/common.txt

.PHONY: collectstatic
collectstatic:  ## Django collectstatic
	python3 -m manage collectstatic --clear --link --noinput

.PHONY: coverage
coverage:  ## Run coverage
	python3 -m coverage run manage.py test --noinput --parallel --shuffle

.PHONY: fix
fix:  ## Fix code formatting, linting and sorting imports
	python3 -m black .
	python3 -m isort .
	python3 -m flake8
	python3 -m mypy .

.PHONY: flush
flush:  ## Django flush
	python3 -m manage flush --noinput

.PHONY: local
local: pip_update  ## Install local requirements and dependencies
	python3 -m piptools sync requirements/local.txt

.PHONY: migrate
migrate:  ## Django migrate
	python3 -m manage migrate --noinput

.PHONY: migrations
migrations: ## Django makemigrations
	python3 -m manage makemigrations --no-header

.PHONY: outdated
outdated:  ## Check outdated requirements and dependencies
	python3 -m pip list --outdated

.PHONY: pip
pip: pip_update  ## Compile requirements
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/common.txt requirements/common.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/local.txt requirements/local.in
	python3 -m piptools compile --generate-hashes --no-header --quiet --upgrade --output-file requirements/test.txt requirements/test.in

.PHONY: pip_update
pip_update:  ## Update requirements and dependencies
	python3 -m pip install -q -U pip~=22.3.0 pip-tools~=6.9.0 setuptools~=65.5.0 wheel~=0.37.0

.PHONY: precommit
precommit:  ## Fix code formatting, linting and sorting imports
	python3 -m pre_commit run --all-files

.PHONY: precommit_update
precommit_update:  ## Update pre_commit
	python3 -m pre_commit autoupdate

.PHONY: report
report:  ## Run coverage report
	python3 -m coverage combine
	python3 -m coverage html
	python3 -m coverage report

.PHONY: simpletest
simpletest:  ## Run debugging test
	python3 -m manage test --timing --shuffle --failfast --pdb --debug-sql --verbosity 3

.PHONY: test
test:  check coverage report ## Run test

.PHONY: update
update: pip precommit_update ## Run update

.PHONY: help
help:
	@echo "[Help] Makefile list commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
