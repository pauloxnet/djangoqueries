.PHONY: check coverage dumpblog fix flush loadblog migrate migrations pip_compile pip_outdated pip_sync pip_update precommit_install precommit_run precommit_update runserver simpletest test update

check:
	python -m manage check
	python -m manage makemigrations --dry-run --check
	python -m ruff format --check .
	python -m ruff check .
	python -m bandit --configfile pyproject.toml --quiet --recursive .
	python -m pip_audit --disable-pip --require-hashes --requirement requirements/common.txt

coverage:
	python -m coverage run manage.py test --buffer --noinput --parallel --shuffle
	python -m coverage combine
	python -m coverage html
	python -m coverage report

dumpblog:
	python -m manage dumpdata blog --natural-foreign --natural-primary --output blog/fixtures/blog.json

fix:
	python -m ruff format .
	python -m ruff check --fix .

flush:
	python3 -m manage flush --noinput

loadblog:
	python -m manage loaddata blog/fixtures/blog.json

migrate:
	python -m manage migrate --noinput

migrations:
	python -m manage makemigrations --no-header

pip_compile: pip_update
	python -m uv pip compile --allow-unsafe --generate-hashes --no-header --quiet --resolver=backtracking --strip-extras --upgrade --output-file requirements/common.txt requirements/common.in
	python -m uv pip compile --allow-unsafe --generate-hashes --no-header --quiet --resolver=backtracking --strip-extras --upgrade --output-file requirements/local.txt requirements/local.in
	python -m uv pip compile --allow-unsafe --generate-hashes --no-header --quiet --resolver=backtracking --strip-extras --upgrade --output-file requirements/test.txt requirements/test.in

pip_outdated:
	python -m uv pip list --outdated

pip_sync: pip_update
	python -m uv pip sync requirements/local.txt

pip_update:
	python -m pip install --quiet --upgrade pip uv

precommit_install:
	python -m pre_commit install

precommit_run:
	python -m pre_commit run --all-files

precommit_update:
	python -m pre_commit autoupdate

runserver:
	python3 -m manage runserver 0:8000

simpletest:
	python -m manage test --debug-sql --duration 10 --failfast --pdb --shuffle --timing --verbosity 2

test: check coverage

update: pip_compile precommit_update
