from django import forms
from .models import Company


class CreateCompanyForm(forms.ModelForm):
    """
    ModelForm for creating a new `Company`.

    model: `Company`
    Includes fields for basic company data, description, services,
    and location.
    """

    class Meta:
        model = Company
        fields = ("company_name",
                  "description",
                  "website",
                  "services",
                  "logo",
                  "full_description",
                  "city",
                  "country",
                  "role",)
