from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import slugify
from django.views import generic

from .forms import CreateCompanyForm
from .models import Company


class CompanyListView(generic.ListView):
    """
    Displays a list of all companies.

    model: `Company`

    **context**
    - `companies`: queryset of all companies ordered by newest first

    template: `companies/companies_page.html`
    """

    queryset = Company.objects.order_by("-created_on")
    template_name = "companies/companies_page.html"
    context_object_name = "companies"
    paginate_by = 9


class UserCompanyListView(generic.ListView):
    """
    Displays companies owned by the logged-in user.

    model: `Company`

    **context**
    - `companies`: companies filtered by the logged-in user

    template: `companies/user_companies_page.html`
    """

    template_name = "companies/user_companies_page.html"
    context_object_name = "companies"
    paginate_by = 9

    def get_queryset(self):
        return Company.objects.filter(
            owner=self.request.user).order_by("-created_on")


def view_create_company_page(request):
    """
    Renders the company creation form and handles form submission.

    model: `Company`
    form: `CreateCompanyForm`

    **context**
    - `form`: instance of `CreateCompanyForm`

    template: `companies/create_company.html`
    """

    if request.method == "POST":
        form = CreateCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.slug = slugify(company.company_name)
            company.save()
            messages.add_message(
                request, messages.SUCCESS, "Company created successfully!")
            return HttpResponseRedirect(reverse("companies"))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Please correct the errors and try again.")
    else:
        form = CreateCompanyForm()

    return render(request, "companies/create_company.html", {"form": form})


def company_detail(request, slug):
    """
    Displays a detailed view of a single company and handles updates.

    model: `Company`
    form: `CreateCompanyForm`

    **context**
    - `company`: the selected company
    - `services_list`: list of services split on commas
    - `form`: form used for updating the company (POST only)

    template: `companies/company_detail.html`
    """

    queryset = Company.objects
    company = get_object_or_404(queryset, slug=slug)
    """ Split services into a list, help from ChatGPT """
    services_list = (
        [s.strip() for s in company.services.split(",")]
        if company.services
        else []
    )

    if request.method == "POST":
        form = CreateCompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid() and company.owner == request.user:
            company = form.save(commit=False)
            company.slug = slugify(company.company_name)
            company.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"'{company.company_name}' updated successfully!")
            return redirect("company_detail", slug=company.slug)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Please correct the errors and try again.')
            return render(
                request,
                "companies/company_detail.html",
                {"company": company,
                 "services_list": services_list,
                 "form": form}
            )

    return render(
        request,
        "companies/company_detail.html",
        {"company": company, "services_list": services_list})


def delete_company(request, company_id, slug):
    """
    Deletes a specific company owned by the logged-in user.

    model: `Company`

    **context**
    - No template rendered. Redirects after deletion.

    redirects:
    - `user_companies` on success
    - `company_detail` on unauthorized attempt
    """

    company = get_object_or_404(Company, pk=company_id, slug=slug)
    if company.owner == request.user:
        company.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            f"'{company.company_name}' deleted successfully!")
        return HttpResponseRedirect(reverse("user_companies"))
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "You can only delete your own companies!")
        return HttpResponseRedirect(
            reverse("company_detail", args=[company.slug]))
