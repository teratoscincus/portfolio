from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

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
