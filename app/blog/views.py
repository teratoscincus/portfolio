from django.views.generic import DetailView, ListView

from .models import BlogPost, BlogPostParagraph


class BlogPostListView(ListView):
    """Overview of all blog posts."""

    model = BlogPost
    context_object_name = "blog_post_list"


class BlogPostDetailView(DetailView):
    """Detail view of a blog post."""

    model = BlogPost
    context_object_name = "blog_post"

    def get_context_data(self, **kwargs):
        blog_post = super().get_context_data(**kwargs)["blog_post"]
        blog_post.paragraphs = BlogPostParagraph.objects.filter(
            blog_post=self.get_object()
        )
        return {self.context_object_name: blog_post}
