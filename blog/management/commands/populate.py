"""A command to populate show instances."""

from django.core.management.base import BaseCommand

from blog.models import Author, Blog, Entry

AUTHOR_LIST = [
    "Terry Gilliam",
    "Terry Jones",
    "Jerry Lewis",
    "Helen Mirren",
    "Helena Bonham Carter",
    "Hélène Joy",
]
BLOG_KWARGS = {
    "lang": "french",
    "name": "Recettes",
    "tagline": "Des recettes dans toutes les langues!",
}
ENTRY_LIST = [
    {
        "headline": "Cheese on Toast recipes",
        "body_text": (
            'Cheese on toast or in Scotland "Toasted cheese" or '
            '"Roasted Cheese" is a snack made by placing cheese '
            "on slices of bread and melting the cheese under a grill."
        ),
    },
    {
        "headline": "Pizza Recipes",
        "body_text": (
            "Pizza is a yeasted flatbread typically topped with tomato sauce "
            "and cheese and baked in an oven. It is commonly topped with a "
            "selection of meats, vegetables and condiments."
        ),
    },
    {
        "headline": "Pain perdu",
        "body_text": (
            "Le pain perdu est un mets à base de pain trempé dans un mélange "
            "de lait et d'œuf puis cuit. Il est connu dans de nombreuses "
            "régions du monde sous diverses appellations comme pain doré."
        ),
    },
]


class Command(BaseCommand):
    """A command to populate database with shows related data."""

    help = "Populate database with shows related data."

    def handle(self, *args, **options):
        """Clear old instances and create new ones."""
        Blog.objects.all().delete()
        blog = Blog.objects.create(**BLOG_KWARGS)
        Author.objects.all().delete()
        Author.objects.bulk_create(Author(name=author) for author in AUTHOR_LIST)
        Entry.objects.all().delete()
        Entry.objects.bulk_create(Entry(blog=blog, **entry) for entry in ENTRY_LIST)
