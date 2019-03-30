# Django Queries

[![Build Status](https://travis-ci.org/pauloxnet/django_queries.svg?branch=master)](https://travis-ci.org/pauloxnet/django_queries) 

Source code used in my article ["Full-Text Search in Django with PostgreSQL"](https://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql) based on the blog application defined in the Django documentation topic ["Making queries"](https://docs.djangoproject.com/en/stable/topics/db/queries/).

## Documentation

### Database

Creating the `django_queries` database in your local PostgreSQL instance.

```shell
$ createdb -U postgres -O postgres django_queries
```

### Virtualenv

Creating and activating the `django_queries` virtual environments.

```shell
$ mkdir -p ~/.venvs
$ python3 -m venv ~/.venvs/django_queries
$ source ~/.venvs/django_queries/bin/activate
```

### Requirements

Installing the required python packages in the `django_queries` virtual environments.

```shell
(django_queries) $ pip install -r requirements.txt
```

### Migrate

Migrating the `django_queries` database to create all required tables.

```shell
(django_queries) $ python manage.py migrate
```

### Tests

Running the defined tests.

```shell
(django_queries) $ python manage.py test
```

### Data

Populating the `django_queries` database with demo data for the blog app.

```shell
(django_queries) $ python manage.py populate
```

## License

**Django Queries** is licensed under the [BSD 3-Clause License](https://github.com/pauloxnet/django_queries/blob/master/LICENSE)

## Authors

**Django Queries** is designed, authored, reviewed and tested by:
- [@pauloxnet](https://github.com/pauloxnet)