# Generated by Django 4.1.7 on 2023-03-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fuel",
            name="currency",
        ),
        migrations.AddField(
            model_name="stationfuel",
            name="currency",
            field=models.CharField(default="roubles", max_length=31),
        ),
    ]