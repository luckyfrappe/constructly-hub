from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("bids/", include("bids.urls"), name="bids-urls"),
    path("companies/", include("companies.urls"), name="companies-urls"),
    path("projects/", include("projects.urls"), name="projects-urls"),
    path("userprofile/", include("userprofile.urls"), name="userprofile-urls"),
    path("", include("landing.urls"), name="landing-urls"),
]
