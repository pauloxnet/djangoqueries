"""The shows app tests."""

from django.test import TestCase

from .models import Band, Genre

DJANGO_REINHARDT = {
    "nickname": "Django Reinhardt",
    "description": (
        "Jean Reinhardt (23 January 1910 – 16 May 1953), known to all by his gypsy "
        "nickname Django (French: [dʒãŋɡo ʁɛjnaʁt] or [dʒɑ̃ɡo ʁenɑʁt]), was a "
        "Belgian-born Romani-French jazz guitarist and composer. He was the first jazz "
        "talent to emerge from Europe and remains the most significant."
    ),
}
ELLA_FITZGERALD = {
    "nickname": "Ella Fitzgerald",
    "description": (
        "Ella Jane Fitzgerald (April 25, 1917 – June 15, 1996) was an American jazz "
        "singer, sometimes referred to as the First Lady of Song, Queen of Jazz, and "
        "Lady Ella. She was noted for her purity of tone, impeccable diction, "
        "phrasing, timing, intonation, and a “horn-like” improvisational ability, "
        "particularly in her scat singing."
    ),
}
LOUIS_ARMSTRONG = {
    "nickname": "Louis Armstrong",
    "description": (
        "Louis Daniel Armstrong (August 4, 1901 – July 6, 1971), nicknamed “Satchmo”, "
        "“Satch”, and “Pops”, was an American trumpeter, composer, vocalist, and actor "
        "who was among the most influential figures in jazz. His career spanned five "
        "decades, from the 1920 to the 1960, and different eras in the history of jazz."
    ),
}


class BandTest(TestCase):
    """The band app test case."""

    def setUp(self):
        """Set up shows instances for tests."""
        blues, _ = Genre.objects.get_or_create(name="Blues")
        jazz, _ = Genre.objects.get_or_create(name="Jazz")
        swing, _ = Genre.objects.get_or_create(name="Swing")
        django_reinhardt, _ = Band.objects.get_or_create(**DJANGO_REINHARDT)
        ella_fitzgerald, _ = Band.objects.get_or_create(**ELLA_FITZGERALD)
        louis_armstrong, _ = Band.objects.get_or_create(**LOUIS_ARMSTRONG)
        django_reinhardt.genres.add(jazz)
        ella_fitzgerald.genres.add(blues)
        louis_armstrong.genres.add(blues, swing)

    def test_band_search(self):
        """Test the band search."""
        band_queryset = Band.objects.search("jazz").values_list("nickname", "rank")
        band_list = (
            ("Django Reinhardt", 0.31916170),
            ("Ella Fitzgerald", 0.075990885),
            ("Louis Armstrong", 0.075990885),
        )
        self.assertCountEqual(band_queryset, band_list)
