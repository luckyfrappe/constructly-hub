from . import views
from django.urls import path

urlpatterns = [
    path("", views.CompanyListView.as_view(), name="companies"),
    path('<slug:slug>/', views.company_detail, name='post_detail'),
]
