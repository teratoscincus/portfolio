from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="The title of the project.",
    )
    summary = models.TextField(
        help_text="Summarize the project.",
    )
    description = models.TextField(
        blank=True,
        help_text="A detailed description of the project.",
    )

    def __str__(self):
        return self.title
