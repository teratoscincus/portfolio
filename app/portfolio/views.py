from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Project


class ProjectsListView(ListView):
    """Overview of all showcased projects."""

    model = Project
    context_object_name = "project_list"

    def get_queryset(self):
        return Project.objects.filter(publish=True)


class ProjectDetailView(DetailView):
    """Detail view of a project."""

    model = Project
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        project = super().get_context_data(**kwargs)["project"]
        if not project.publish:
            raise Http404

        return {self.context_object_name: project}
