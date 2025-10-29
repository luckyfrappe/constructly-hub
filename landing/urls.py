from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_landing_page, name="landing"),
]
