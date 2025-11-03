"""
URL configuration for constructly_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("bids/", include("bids.urls"), name="bids-urls"),
    path("companies/", include("companies.urls"), name="companies-urls"),
    path("insights/", include("insights.urls"), name="insights-urls"),
    path("projects/", include("projects.urls"), name="projects-urls"),
    path("userprofile/", include("userprofile.urls"), name="userprofile-urls"),
    path("", include("landing.urls"), name="landing-urls"),
]
