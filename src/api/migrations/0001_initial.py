# Generated by Django 4.1.7 on 2023-03-26 11:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fuel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("icon", models.ImageField(null=True, upload_to="")),
                ("currency", models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name="GasStation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(null=True, unique=True)),
                ("address", models.CharField(max_length=255, null=True)),
                (
                    "latitude",
                    models.DecimalField(decimal_places=5, max_digits=8, null=True),
                ),
                (
                    "longitude",
                    models.DecimalField(decimal_places=5, max_digits=8, null=True),
                ),
                (
                    "urls",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.URLField(max_length=255), null=True, size=None
                    ),
                ),
            ],
            options={
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="StationFuel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=16)),
                (
                    "fuel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.fuel"
                    ),
                ),
                (
                    "gas_station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.gasstation"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("icon", models.ImageField(null=True, upload_to="")),
                (
                    "gas_station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.gasstation"
                    ),
                ),
            ],
        ),
    ]
