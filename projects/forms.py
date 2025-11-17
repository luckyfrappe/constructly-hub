from .models import Project
from django import forms


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'location', 'budget', 'deadline')