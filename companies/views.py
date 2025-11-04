from django.shortcuts import render
from django.views import generic
from .models import Company

# Create your views here.

class CompanyListView(generic.ListView):
    queryset = Company.objects.order_by("-created_on")
    template_name = "companies/companies_page.html"
    context_object_name = "companies"
    paginate_by = 9
