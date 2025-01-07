"""The shows app tests."""

from django.test import SimpleTestCase, TestCase

from shows.models import Band, Genre


class GenreTest(SimpleTestCase):
    """The genre model test case."""

    def test_str(self) -> None:
        """Test the band search."""
        self.assertEqual(str(Genre(name="Rock")), "Rock")


class BandTest(TestCase):
    """The band model test case."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Set up model instances for tests."""
        [blues, jazz, swing] = Genre.objects.bulk_create(
            [Genre(name="Blues"), Genre(name="Jazz"), Genre(name="Swing")],
        )
        [django, ella, louis] = Band.objects.bulk_create(
            [
                Band(
                    nickname="Django Reinhardt",
                    description=(
                        "Jean Reinhardt (23 January 1910 - 16 May 1953), known to all "
                        "by his gypsy nickname Django, was a Belgian-born Romani-French"
                        " jazz guitarist and composer. He was the first jazz talent to "
                        "emerge from Europe and remains the most significant."
                    ),
                ),
                Band(
                    nickname="Ella Fitzgerald",
                    description=(
                        "Ella Jane Fitzgerald (April 25, 1917 - June 15, 1996) was an "
                        "American jazz singer, sometimes referred to as the First Lady "
                        "of Song, Queen of Jazz, and Lady Ella. She was noted for her "
                        "purity of tone, impeccable diction, phrasing, timing, "
                        "intonation, and a “horn-like” improvisational ability, "
                        "particularly in her scat singing."
                    ),
                ),
                Band(
                    nickname="Louis Armstrong",
                    description=(
                        "Louis Daniel Armstrong (August 4, 1901 - July 6, 1971), "
                        "nicknamed “Satchmo”, “Satch”, and “Pops”, was an American "
                        "trumpeter, composer, vocalist, and actor who was among the "
                        "most influential figures in jazz. His career spanned five "
                        "decades, from the 1920 to the 1960, and different eras in the "
                        "history of jazz."
                    ),
                ),
            ],
        )
        Band.genres.through.objects.bulk_create(
            [
                Band.genres.through(band_id=django.id, genre_id=jazz.id),
                Band.genres.through(band_id=ella.id, genre_id=blues.id),
                Band.genres.through(band_id=louis.id, genre_id=blues.id),
                Band.genres.through(band_id=louis.id, genre_id=swing.id),
            ],
        )

    def test_str(self) -> None:
        """Test the band search."""
        self.assertEqual(str(Band(nickname="Grappelli")), "Grappelli")

    def test_band_search(self) -> None:
        """Test the band search."""
        self.assertCountEqual(
            Band.objects.search("jazz").values_list("nickname", "rank"),
            (
                ("Django Reinhardt", 0.31916170),
                ("Ella Fitzgerald", 0.075990885),
                ("Louis Armstrong", 0.075990885),
            ),
        )
