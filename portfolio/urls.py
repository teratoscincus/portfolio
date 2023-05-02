from django.urls import path

from .views import ProjectDetailView, ProjectsListView

app_name = "portfolio"
urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="single_project"),
]
