from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'city', 'website')
    search_fields = ('company_name', 'city')
    list_filter = ('city',)
    ordering = ('company_name',)
    prepopulated_fields = {'slug': ('company_name',)}