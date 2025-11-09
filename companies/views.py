from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Company
from .forms import CreateCompanyForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify

# Create your views here.

class CompanyListView(generic.ListView):
    queryset = Company.objects.order_by("-created_on")
    template_name = "companies/companies_page.html"
    context_object_name = "companies"
    paginate_by = 9

class UserCompanyListView(generic.ListView):
    template_name = "companies/user_companies_page.html"
    context_object_name = "companies"
    paginate_by = 9

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user).order_by("-created_on")

def view_create_company_page(request):
    """
    Display the company creation page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`create_company.html`
    """
    if request.method == "POST":
        form = CreateCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.slug = slugify(company.company_name)
            company.save()
            messages.success(request, "Company created successfully!")
            return HttpResponseRedirect(reverse("companies"))
    else:
        form = CreateCompanyForm()

    return render(request, "companies/create_company.html", {"form": form})

def company_detail(request, slug):
    """
    Display an individual :model:`companies.Company`.

    **Context**

    ``company``
        An instance of :model:`companies.Company`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Company.objects
    company = get_object_or_404(queryset, slug=slug)
    """ Split services into a list, help from ChatGPT """
    services_list = [s.strip() for s in company.services.split(",")] if company.services else []

    return render(request, "companies/company_detail.html", {"company": company, "services_list": services_list})
