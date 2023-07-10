# Generated by Django 4.2.3 on 2023-07-03 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Creator",
            fields=[
                (
                    "account_id",
                    models.OneToOneField(
                        db_column="account_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="creator",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("earnings", models.PositiveIntegerField(default=0)),
                ("channel_id", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Creator",
                "verbose_name_plural": "Creators",
                "db_table": "creators",
            },
        ),
    ]
