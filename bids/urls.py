from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_bids_page, name="bids"),
]
