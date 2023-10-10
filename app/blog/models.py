from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="The title of the blog post.",
    )
    intro = models.TextField(
        help_text="Introduction for the blog post.",
    )
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, default="")

    def save(self, *args, **kwargs):
        """Generate a slug field and save the instance."""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogPostParagraph(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(
        blank=True,
        help_text="A blog post paragraph.",
    )

    def __str__(self):
        return f"{self.blog_post.title} (p.{self.pk})"
