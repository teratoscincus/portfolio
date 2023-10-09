from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from .models import About


class IndexView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        try:
            about = About.objects.get(featured=True).text
        except ObjectDoesNotExist:
            about = None
        return {"about": about}


class Status404View(TemplateView):
    template_name = "core/status/404.html"


class Status500View(TemplateView):
    template_name = "core/status/500.html"
