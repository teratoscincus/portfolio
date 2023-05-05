from django.views.generic import TemplateView

from .models import About


class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        return {"about": About.objects.get(featured=True).text}
