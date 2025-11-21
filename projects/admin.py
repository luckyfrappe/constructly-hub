from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the `Project` model.

    Displays key fields, enables searching and filtering,
    and sets default ordering in the admin list view.
    """
    list_display = ('title', 'location', 'client', 'status', 'created_on')
    search_fields = ('title', 'location', 'client__username')
    list_filter = ('location', 'status', 'created_on')
    ordering = ('status', 'created_on')
