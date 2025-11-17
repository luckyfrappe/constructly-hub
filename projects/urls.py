from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="projects"),
]
