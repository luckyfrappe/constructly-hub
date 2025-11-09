from . import views
from django.urls import path

urlpatterns = [
    path("create-company/", views.view_create_company_page, name="create_company"),
    path("my-companies/", views.UserCompanyListView.as_view(), name="user_companies"),
    path('<slug:slug>/delete_company/<int:company_id>', views.delete_company, name='delete_company'),
    path('<slug:slug>/', views.company_detail, name='company_detail'),
    path("", views.CompanyListView.as_view(), name="companies"),
]
