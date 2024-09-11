"""The shows app tests."""

from django.test import SimpleTestCase, TestCase

from .models import Band, Genre

GENRES = ("Blues", "Jazz", "Swing")

BANDS = (
    {
        "nickname": "Django Reinhardt",
        "description": (
            "Jean Reinhardt (23 January 1910 – 16 May 1953), known to all by his gypsy "
            "nickname Django (French: [dʒãŋɡo ʁɛjnaʁt] or [dʒɑ̃ɡo ʁenɑʁt]), was a "
            "Belgian-born Romani-French jazz guitarist and composer. He was the first "
            "jazz talent to emerge from Europe and remains the most significant."
        ),
    },
    {
        "nickname": "Ella Fitzgerald",
        "description": (
            "Ella Jane Fitzgerald (April 25, 1917 – June 15, 1996) was an American jazz"
            " singer, sometimes referred to as the First Lady of Song, Queen of Jazz, "
            "and Lady Ella. She was noted for her purity of tone, impeccable diction, "
            "phrasing, timing, intonation, and a “horn-like” improvisational ability, "
            "particularly in her scat singing."
        ),
    },
    {
        "nickname": "Louis Armstrong",
        "description": (
            "Louis Daniel Armstrong (August 4, 1901 – July 6, 1971), nicknamed "
            "“Satchmo”, “Satch”, and “Pops”, was an American trumpeter, composer, "
            "vocalist, and actor who was among the most influential figures in jazz. "
            "His career spanned five decades, from the 1920 to the 1960, and different "
            "eras in the history of jazz."
        ),
    },
)


class GenreTest(SimpleTestCase):
    """The genre model test case."""

    def test_str(self):
        """Test the band search."""
        self.assertEqual(str(Genre(name="Rock")), "Rock")


class BandTest(TestCase):
    """The band model test case."""

    @classmethod
    def setUpTestData(cls):
        """Set up model instances for tests."""
        [blues, jazz, swing] = Genre.objects.bulk_create(Genre(name=n) for n in GENRES)
        [django, ella, louis] = Band.objects.bulk_create(Band(**b) for b in BANDS)
        band_genres = (
            {"band_id": django.id, "genre_id": jazz.id},
            {"band_id": ella.id, "genre_id": blues.id},
            {"band_id": louis.id, "genre_id": blues.id},
            {"band_id": louis.id, "genre_id": swing.id},
        )
        BandGenre = Band.genres.through
        BandGenre.objects.bulk_create(BandGenre(**bg) for bg in band_genres)

    def test_str(self):
        """Test the band search."""
        self.assertEqual(str(Band(nickname="Grappelli")), "Grappelli")

    def test_band_search(self):
        """Test the band search."""
        band_queryset = Band.objects.search("jazz").values_list("nickname", "rank")
        band_list = (
            ("Django Reinhardt", 0.31916170),
            ("Ella Fitzgerald", 0.075990885),
            ("Louis Armstrong", 0.075990885),
        )
        self.assertCountEqual(band_queryset, band_list)
