# Generated by Django 3.2.10 on 2022-01-20 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buybackprogram", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContractNotification",
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
                ("icon", models.CharField(max_length=64)),
                ("color", models.CharField(max_length=32)),
                ("message", models.CharField(max_length=1024)),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buybackprogram.contract",
                    ),
                ),
            ],
        ),
    ]
