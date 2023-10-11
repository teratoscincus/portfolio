from django.contrib import admin

from .models import BlogPost, BlogPostParagraph


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    exclude = ["slug"]


admin.site.register(BlogPostParagraph)
