from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.

class ProjectListView(generic.ListView):
    queryset = Project.objects.order_by("-created_on")
    template_name = "projects/projects_page.html"
    context_object_name = "projects"
    paginate_by = 9
