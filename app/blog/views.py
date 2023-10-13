from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from .models import BlogPost, BlogPostParagraph, BlogPostSnippet


class BlogPostListView(ListView):
    """Overview of all blog posts."""

    model = BlogPost
    context_object_name = "blog_post_list"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag", "")
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = BlogPost.objects.filter(tags__in=[tag])
        else:
            queryset = BlogPost.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        tag_slug = self.kwargs.get("tag", "")
        if tag_slug:
            context["tag"] = get_object_or_404(Tag, slug=tag_slug)
        context["tags"] = Tag.objects.all()

        return context


class BlogPostDetailView(DetailView):
    """Detail view of a blog post."""

    model = BlogPost
    context_object_name = "blog_post"

    def get_context_data(self, **kwargs):
        blog_post = super().get_context_data(**kwargs)["blog_post"]
        blog_post.paragraphs = BlogPostParagraph.objects.filter(
            blog_post=self.get_object()
        )
        for paragraph in blog_post.paragraphs:
            paragraph.snippets = BlogPostSnippet.objects.filter(paragraph=paragraph)

        return {self.context_object_name: blog_post}
