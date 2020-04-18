from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("shows", "0001_initial")]

    operations = [TrigramExtension()]
