"""Blog app models."""

from django.contrib.postgres import search
from django.db import models


class Blog(models.Model):
    """A blog with a name and a default language."""

    name = models.CharField(max_length=100)
    tagline = models.TextField()
    lang = models.CharField(max_length=100, default="english")

    def __str__(self) -> str:
        """Return string representation."""
        return str(self.name)


class Author(models.Model):
    """An author with is name."""

    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        """Return string representation."""
        return str(self.name)


class Entry(models.Model):
    """A blog entry with authors field."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    search_vector = search.SearchVectorField(null=True)

    def __str__(self) -> str:
        """Return the string representation."""
        return str(self.headline)
