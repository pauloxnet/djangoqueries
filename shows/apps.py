"""Define the Django app for shows."""

from django.apps import AppConfig


class ShowsConfig(AppConfig):
    """A Django app for shows."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "shows"
