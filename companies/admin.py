from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Customises the Django admin interface for the `Company` model.

    model: `Company`
    Displays name, city and website in the admin list,
    enables search and filtering,
    and auto-generates slugs from the company name.
    """
    list_display = ('company_name', 'city', 'website')
    search_fields = ('company_name', 'city')
    list_filter = ('city',)
    ordering = ('company_name',)
    prepopulated_fields = {'slug': ('company_name',)}
