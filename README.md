# Django Queries

Source code from the Weblog application defined in the Django Documentation Topic
[Making Queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/).

## Creating Database

```SQL
CREATE DATABASE django_queries
WITH ENCODING='UTF8'
   OWNER=postgres
   CONNECTION LIMIT=-1;
```

## Creating and Activating Virtual Environments

```Shell
$ python3.6 -m venv ~/envs/django_queries
$ source ~/envs/django_queries
```

## Installing Python Requirements

```Shell
$ pip install -r requirements.txt
```
