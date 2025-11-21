from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_userprofile_page, name="userprofile"),
    path("settings/", views.view_settings_page, name="settings"),
    path("delete/", views.delete_account, name="delete_account"),
]
