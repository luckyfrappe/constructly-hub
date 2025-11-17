from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="projects"),
    path("my-projects/", views.UserProjectListView.as_view(), name="user_projects"),
    path("create/", views.view_create_project_page, name="create_project"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
