import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("tagline", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.CharField(max_length=255)),
                ("body_text", models.TextField()),
                ("pub_date", models.DateField()),
                ("mod_date", models.DateField()),
                ("n_comments", models.IntegerField()),
                ("n_pingbacks", models.IntegerField()),
                ("rating", models.IntegerField()),
                ("authors", models.ManyToManyField(to="blog.Author")),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.Blog",
                    ),
                ),
            ],
        ),
    ]
