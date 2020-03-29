"""Define tests for blog models."""

from django.test import SimpleTestCase

from blog.models import Author, Blog, Entry


class BlogTest(SimpleTestCase):
    """Test blog models."""

    def setUp(self):
        """Prepare initial data for testing."""
        self.author = Author(name="Dante Alighieri")
        self.blog = Blog(
            lang="italian",
            name="Divina Commedia",
            tagline="The Divine Comedy is a Italian narrative poem by Dante Alighieri.",
        )
        self.entry = Entry(
            blog=self.blog,
            headline="Inferno - Canto primo",
            body_text=(
                "Nel mezzo del cammin di nostra vita "
                "mi ritrovai per una selva oscura, "
                "ché la diritta via era smarrita."
            ),
        )

    def test_string(self):
        """Test returning string representation for a blog models."""
        self.assertEqual(str(self.author), "Dante Alighieri")
        self.assertEqual(str(self.blog), "Divina Commedia")
        self.assertEqual(str(self.entry), "Inferno - Canto primo")
