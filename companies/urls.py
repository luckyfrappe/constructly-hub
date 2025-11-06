from . import views
from django.urls import path

urlpatterns = [
    path("create-company/", views.view_create_company_page, name="create_company"),
    path("my-companies/", views.UserCompanyListView.as_view(), name="user_companies"),
    path("", views.CompanyListView.as_view(), name="companies"),
    path('<slug:slug>/', views.company_detail, name='post_detail'),
]
