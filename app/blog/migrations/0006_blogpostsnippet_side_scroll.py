# Generated by Django 5.0 on 2023-12-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostsnippet',
            name='side_scroll',
            field=models.BooleanField(default=False, help_text='Scrollable sideways'),
        ),
    ]
