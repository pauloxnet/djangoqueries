"""Show models."""

from django.db import models

from .managers import BandManager


class Genre(models.Model):
    """A music genre name."""

    name = models.CharField(max_length=255)


class Band(models.Model):
    """A band with its genres."""

    nickname = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField("Genre")

    objects = BandManager()
