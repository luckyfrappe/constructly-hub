from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from projects.forms import CreateProjectForm
from .models import Project

# Create your views here.

class ProjectListView(generic.ListView):
    queryset = Project.objects.order_by("-created_on")
    template_name = "projects/projects_page.html"
    context_object_name = "projects"
    paginate_by = 9

class UserProjectListView(generic.ListView):
    template_name = "projects/projects_page.html"
    context_object_name = "projects"
    paginate_by = 9

    def get_queryset(self):
        return Project.objects.filter(client=self.request.user).order_by("-created_on")
    
def view_create_project_page(request):
    """
    Display the project creation page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`create_project.html`
    """
    if request.method == "POST":
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated:
            if form.cleaned_data['deadline'] < timezone.now().date() + timezone.timedelta(days=1):
                messages.add_message(request, messages.ERROR, "Deadline must be in the future.")
                return render(request, "projects/create_project.html", {"form": form,})
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            messages.add_message(request, messages.SUCCESS, "Project created successfully!")
            return HttpResponseRedirect(reverse("projects"))
        else:
            messages.add_message(request, messages.ERROR, "Please correct the errors and try again.")
    else:
        form = CreateProjectForm()

    return render(request, "projects/create_project.html", {"form": form,})
