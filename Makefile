# Develop

check:
	black --check .
	isort --check-only .
	flake8
	mypy .

collectstatic:
	python manage.py collectstatic --clear --noinput

dev:
	pip install -q -U pip~=20.2.0 pip-tools~=5.3.0
	pip-sync requirements/dev.txt

fix:
	black .
	isort .
	flake8
	mypy .

migrate:
	python manage.py migrate --noinput

migrations:
	python manage.py makemigrations --no-header

pip:
	pip install -q -U pip~=20.2.0 pip-tools~=5.3.0
	pip-compile $(p) -q -U -o requirements/common.txt requirements/common.ini
	pip-compile $(p) -q -U -o requirements/dev.txt requirements/dev.ini
	pip-compile $(p) -q -U -o requirements/tests.txt requirements/tests.ini

test:
	tox -e coverage,reporthtml,report
