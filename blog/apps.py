"""Define the Django app for blog."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """A Django app for blog."""

    default_auto_field = "django.db.models.AutoField"
    name = "blog"
