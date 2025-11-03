from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_projects_page, name="projects"),
]
