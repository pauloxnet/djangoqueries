from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shows", "0002_trigram"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
