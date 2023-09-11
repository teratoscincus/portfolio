from django.views.generic import DetailView, ListView

from .models import Project


class ProjectsListView(ListView):
    """Overview of all showcased projects."""

    model = Project
    context_object_name = "project_list"


class ProjectDetailView(DetailView):
    """Detail view of a project."""

    model = Project
    context_object_name = "project"
