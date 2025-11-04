from . import views
from django.urls import path

urlpatterns = [
    path("", views.CompanyListView.as_view(), name="companies"),
]
