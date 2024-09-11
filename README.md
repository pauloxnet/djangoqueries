# 🦄️ Django Queries

[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
![Coverage](https://img.shields.io/badge/coverage-100%25-success)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/000129461?domain=https%3A%2F%2Ffosstodon.org)](https://fosstodon.org/@paulox)

Source code used in my article ["Full-Text Search in Django with PostgreSQL"](https://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql) based on the blog application defined in the Django documentation topic ["Making queries"](https://docs.djangoproject.com/en/stable/topics/db/queries/).

## 📖 Documentation

### 🗃️ Database

Creating the `djangoqueries` database in your local PostgreSQL instance:

```shell
$ createdb -U postgres -O postgres djangoqueries
```

### ⚗️ Virtualenv

Creating and activating the virtual environment:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### 🧩 Requirements

Installing the latest version of `django` _(tested from version 1.11 to 5.1)_ and `psycopg` (tested from version 2.7 to 3.2) using the requirements file:

```shell
$ python -m pip install -r requirements.txt
```

### ⬆️ Migrate

Migrating the `djangoqueries` database to create all required tables:

```shell
$ python -m manage migrate
```

### 🔬 Tests

Running the defined tests:

```shell
$ python -m manage test
```

### 📊 Data

Populating the `djangoqueries` database with demo data for the blog app:

```shell
$ python -m manage loaddata blog/fixtures/blog.json
```

## ⚖️ License

**Django Queries** is licensed under the [BSD 3-Clause License](https://github.com/pauloxnet/djangoqueries/blob/master/LICENSE.md).

## 👥 Authors

### 👤 Paolo Melchiorre

-   🌍 Blog: [www.paulox.net](https://www.paulox.net)
-   🐙 Github: [@pauloxnet](https://github.com/pauloxnet)
-   🦣 Mastodon: [@paulox@fosstodon.org](https://fosstodon.org/@paulox)
-   🐦️ Twitter: [@pauloxnet](https://twitter.com/pauloxnet)
