from django.db import models


class About(models.Model):
    """An about section for the website."""

    featured = models.BooleanField(default=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        """Ensure only one instance is featured and that one always is featured."""
        if self.featured:
            About.objects.update(featured=False)
        else:
            try:
                About.objects.get(featured=True)
            except self.DoesNotExist:
                self.featured = True

        return super().save(*args, **kwargs)
