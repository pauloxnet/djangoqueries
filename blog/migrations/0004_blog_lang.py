from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("blog", "0003_entry_search_vector")]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="lang",
            field=models.CharField(default="english", max_length=100),
        ),
    ]
