# 🦄️ Django Queries

[![Twitter: pauloxnet](https://img.shields.io/twitter/follow/pauloxnet.svg?style=social)](https://twitter.com/pauloxnet)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Build Status](https://travis-ci.org/pauloxnet/djangoqueries.svg?branch=master)](https://travis-ci.org/pauloxnet/djangoqueries)
[![Coverage Status](https://coveralls.io/repos/github/pauloxnet/djangoqueries/badge.svg?branch=master)](https://coveralls.io/github/pauloxnet/djangoqueries?branch=master)


> Source code used in my article ["Full-Text Search in Django with PostgreSQL"](https://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql) based on the blog application defined in the Django documentation topic ["Making queries"](https://docs.djangoproject.com/en/stable/topics/db/queries/).

## 📖 Documentation

### 🗃️ Database

Creating the `djangoqueries` database in your local PostgreSQL instance:

```shell
$ createdb -U postgres -O postgres djangoqueries
```

### ⚗️ Virtualenv

Creating and activating the `djangoqueries` virtual environments:

```shell
$ mkdir -p ~/.virtualenvs
$ python3 -m venv ~/.virtualenvs/djangoqueries
$ source ~/.virtualenvs/djangoqueries/bin/activate
```

### 🧩 Requirements

Installing the required python packages in the `djangoqueries` virtual environments:

```shell
$ pip install -r requirements/dev.txt
```

### ⬆️ Migrate

Migrating the `djangoqueries` database to create all required tables:

```shell
$ python manage.py migrate
```

### 🔬 Tests

Running the defined tests:

```shell
$ python manage.py test
```

### 📊 Data

Populating the `djangoqueries` database with demo data for the blog app:

```shell
$ python manage.py populate
```

## ⚖️ License

**Django Queries** is licensed under the [BSD 3-Clause License](https://github.com/pauloxnet/djangoqueries/blob/master/LICENSE.md).

## 👥 Authors

### 👤 Paolo Melchiorre

* 🐙 Github: [@pauloxnet](https://github.com/pauloxnet)
* ☕️ Website: [www.paulox.net](https://www.paulox.net)
* 🐦️ Twitter: [@pauloxnet](https://github.com/pauloxnet)
