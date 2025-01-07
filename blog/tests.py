"""Define tests for blog models."""

from django.test import SimpleTestCase

from blog.models import Author, Blog, Entry


class BlogTest(SimpleTestCase):
    """Test blog models."""

    def test_string(self) -> None:
        """Test returning string representation for a blog models."""
        author = Author(name="Dante Alighieri")
        self.assertEqual(str(author), "Dante Alighieri")
        blog = Blog(lang="italian", name="Divina Commedia", tagline="Poema allegorico…")
        self.assertEqual(str(blog), "Divina Commedia")
        entry = Entry(blog=blog, headline="Inferno Canto primo", body_text="Nel mezzo…")
        self.assertEqual(str(entry), "Inferno Canto primo")
