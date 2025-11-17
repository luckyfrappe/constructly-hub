from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_bids_page, name="bids"),
    path("<int:bid_id>/select-bid/", views.select_bid, name="select_bid"),
]
