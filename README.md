# Django Queries

[![Build Status](https://travis-ci.org/pauloxnet/django_queries.svg?branch=master)](https://travis-ci.org/pauloxnet/django_queries) 

Source code used in my article ["Full-Text Search in Django with PostgreSQL"](http://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql) based on the Weblog application defined in the Django Documentation Topic
["Making Queries"](https://docs.djangoproject.com/en/2.0/topics/db/queries/).

## Creating Database

In `SQL`

```SQL
CREATE DATABASE django_queries WITH ENCODING='UTF8' OWNER=postgres CONNECTION LIMIT=-1;
```

or in your `Shell`

```Shell
$ createdb -U postgres -O postgres django_queries
```

## Creating and Activating Virtual Environments

```Shell
$ python3 -m venv ~/venvs/django_queries
$ source ~/venvs/django_queries/bin/activate
```

## Installing Python Requirements

```Shell
$ pip install -r requirements.txt
```

## Data population

```Shell
$ python manage.py populate
```

