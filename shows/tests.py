from collections import OrderedDict

from django.test import TestCase

from .models import Band, Genre


class BandTest(TestCase):
    def setUp(self):
        # Genres
        blues, _ = Genre.objects.get_or_create(name="Blues")
        jazz, _ = Genre.objects.get_or_create(name="Jazz")
        swing, _ = Genre.objects.get_or_create(name="Swing")
        # Bands
        ella_fitzgerald, _ = Band.objects.get_or_create(
            nickname="Ella Fitzgerald",
            description=(
                "Ella Jane Fitzgerald (25 Apr 1917-15 Jun 1996) was an American jazz "
                "singer often referred to as the First Lady of Song, Queen of Jazz and "
                "Lady Ella. She was noted for her purity of tone, impeccable diction, "
                "phrasing and intonation, and a horn-like improvisational ability, "
                "particularly in her scat singing."
            ),
        )
        django_reinhardt, _ = Band.objects.get_or_create(
            nickname="Django Reinhardt",
            description=(
                "Jean Django Reinhardt (23 Jan 1910-16 May 1953) was a Belgian-born, "
                "Romani French jazz guitarist and composer, regarded as one of the "
                "greatest musicians of the twentieth century. He was the first jazz "
                "talent to emerge from Europe and remains the most significant."
            ),
        )
        louis_armstrong, _ = Band.objects.get_or_create(
            nickname="Louis Armstrong",
            description=(
                "Louis Armstrong (4 Aug 1901-6 Jul 1971), nicknamed Satchmo, Satch and "
                "Pops, was an American trumpeter, composer, singer and occasional "
                "actor who was one of the most influential figures in jazz. His career "
                "spanned five decades, from the 1920s to the 1960s, and different eras "
                "in the history of jazz."
            ),
        )
        # Bands and Genres
        ella_fitzgerald.genres.add(blues)
        django_reinhardt.genres.add(jazz)
        louis_armstrong.genres.add(blues, swing)

    def test_band_search(self):
        band_queryset = Band.objects.search("jazz").values_list("nickname", "rank")
        band_objects = list(OrderedDict(band_queryset).items())
        band_list = [
            ("Django Reinhardt", 0.26512378),
            ("Ella Fitzgerald", 0.075990885),
            ("Louis Armstrong", 0.075990885),
        ]
        self.assertSequenceEqual(band_objects, band_list)
