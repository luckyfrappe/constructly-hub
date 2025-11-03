from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_insights_page, name="insights"),
]
