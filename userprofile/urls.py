from . import views
from django.urls import path

urlpatterns = [
    path("settings/", views.view_settings_page, name="settings"),
    path("delete/", views.delete_account, name="delete_account"),
    path("", views.view_userprofile_page, name="userprofile"),
]
