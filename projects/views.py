from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from bids.forms import CreateBidForm
from bids.models import Bid
from projects.forms import CreateProjectForm
from .models import Project


class ProjectListView(generic.ListView):
    """
    Displays a list of all projects and auto-closes expired ones.

    model: `Project`

    **context**
    - `projects`: queryset of all projects ordered by most recent

    template: `projects/projects_page.html`
    """

    template_name = "projects/projects_page.html"
    context_object_name = "projects"
    paginate_by = 9

    def get_queryset(self):
        today = timezone.now().date()

        # Auto-update all expired open projects in ONE query, help from ChatGPT
        Project.objects.filter(
            status="open",
            deadline__lt=today).update(status="completed")

        return Project.objects.order_by("-created_on")


class UserProjectListView(generic.ListView):
    """
    Displays projects owned by the logged-in user, auto-closing expired ones.

    model: `Project`

    **context**
    - `projects`: queryset filtered by logged-in user

    template: `projects/projects_page.html`
    """

    template_name = "projects/projects_page.html"
    context_object_name = "projects"
    paginate_by = 9

    def get_queryset(self):
        today = timezone.now().date()

        Project.objects.filter(
            client=self.request.user,
            status="open",
            deadline__lt=today
        ).update(status="completed")

        return Project.objects.filter(
            client=self.request.user).order_by("-created_on")


def view_create_project_page(request):
    """
    Displays the project creation form and handles form submission.

    model: `Project`
    form: `CreateProjectForm`

    **context**
    - `form`: instance of `CreateProjectForm`

    template: `projects/create_project.html`
    """
    if request.method == "POST":
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['deadline'] < timezone.now().date() + timezone.timedelta(days=1):
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Deadline must be in the future.")
                return render(
                    request,
                    "projects/create_project.html",
                    {"form": form, })

            project = form.save(commit=False)
            project.client = request.user
            project.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Project created successfully!")
            return HttpResponseRedirect(reverse("projects"))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Please correct the errors and try again.")
    else:
        form = CreateProjectForm()

    return render(request, "projects/create_project.html", {"form": form, })


def project_detail(request, pk):
    """
    Displays a detailed view of a single project and handles bid submissions.

    model: `Project`
    form: `CreateBidForm`

    **context**
    - `project`: selected project instance
    - `bids`: all bids related to the project
    - `user_bids`: bids belonging to the logged-in user
    - `bid_form`: form for submitting a bid

    template: `projects/project_details.html`
    """

    queryset = Project.objects
    project = get_object_or_404(queryset, pk=pk)

    if request.method == "POST":
        bid_form = CreateBidForm(request.POST)
        if bid_form.is_valid() and request.user.is_authenticated:
            bid = bid_form.save(commit=False)
            bid.project = project
            bid.company_id = request.POST.get("company")
            bid.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Bid submitted successfully!")
            return redirect("project_detail", pk=project.pk)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Please correct the errors and try again.")
            return render(
                request,
                "projects/project_details.html",
                {"project": project, "bid_form": bid_form},
            )

    bid_form = CreateBidForm()
    bids = Bid.objects.filter(project=project).order_by("-created_on")
    user_bids = bids.filter(company__owner=request.user) if request.user.is_authenticated else Bid.objects.none()

    return render(
        request,
        "projects/project_details.html",
        {"project": project,
         "bids": bids,
         "bid_form": bid_form,
         "user_bids": user_bids})
