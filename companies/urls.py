from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_companies_page, name="companies"),
]
