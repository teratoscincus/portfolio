# Generated by Django 5.0 on 2023-12-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_live_url_project_repo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
