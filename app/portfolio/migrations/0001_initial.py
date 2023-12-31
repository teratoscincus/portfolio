# Generated by Django 4.2 on 2023-05-03 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                (
                    "title",
                    models.CharField(
                        help_text="The title of the project.",
                        max_length=50,
                        unique=True,
                    ),
                ),
                ("summary", models.TextField(help_text="Summarize the project.")),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A detailed description of the project."
                    ),
                ),
                ("slug", models.SlugField(default="", unique=True)),
            ],
        ),
    ]
