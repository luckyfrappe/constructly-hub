from .models import Company
from django import forms


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name", "description", "website", "services", "logo", "full_description", "city", "country", "role")