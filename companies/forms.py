from .models import Company
from django import forms
from django.utils.text import slugify


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("company_name", "description", "website", "services", "logo", "full_description", "city", "country", "role",)

    # Validate that the company name is unique by checking the slug, built with help from ChatGPT
    def clean_company_name(self):
        name = self.cleaned_data.get("company_name")
        slug = slugify(name)

        # Check if a company with this slug already exists
        if Company.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A company with this name already exists.")
        return name
    
    def clean_logo(self):
        logo = self.cleaned_data.get("logo")

        # If it's a string (like "placeholder"), skip validation
        if isinstance(logo, str) or logo is None:
            return logo

        valid_extensions = ["image/jpeg", "image/png", "image/webp"]
        if logo.content_type not in valid_extensions:
            raise forms.ValidationError("Please upload a valid image (JPG, PNG, or WEBP).")

        return logo