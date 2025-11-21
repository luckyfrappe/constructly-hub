from django import forms
from .models import Project


class CreateProjectForm(forms.ModelForm):
    """
    Form for creating and editing a project.

    model: `Project`
    Used in views where users can submit project details.
    """

    class Meta:
        model = Project
        fields = ('title', 'description', 'location', 'budget', 'deadline')
