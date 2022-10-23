# 🦄️ Django Queries

[![Twitter: pauloxnet](https://img.shields.io/twitter/follow/pauloxnet.svg?style=social)](https://twitter.com/pauloxnet)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

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

Installing the required python packages in the `djangoqueries` virtual environments:

```shell
$ python3 -m pip install -r requirements/local.txt
```

### ⬆️ Migrate

Migrating the `djangoqueries` database to create all required tables:

```shell
$ python3 -m manage migrate
```

### 🔬 Tests

Running the defined tests:

```shell
$ python3 -m manage test
```

### 📊 Data

Populating the `djangoqueries` database with demo data for the blog app:

```shell
$ python3 -m manage populate
```

## ⚖️ License

**Django Queries** is licensed under the [BSD 3-Clause License](https://github.com/pauloxnet/djangoqueries/blob/master/LICENSE.md).

## 👥 Authors

### 👤 Paolo Melchiorre

-   🌍 Blog: [www.paulox.net](https://www.paulox.net)
-   🐙 Github: [@pauloxnet](https://github.com/pauloxnet)
-   🐦️ Twitter: [@pauloxnet](https://twitter.com/pauloxnet)
