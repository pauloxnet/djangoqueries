from django.db import models

from .managers import BandManager


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Band(models.Model):
    nickname = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)

    objects = BandManager()
