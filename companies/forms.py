from .models import Company
from django import forms


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("company_name", "description", "website", "services", "logo", "full_description", "city", "country", "role",)