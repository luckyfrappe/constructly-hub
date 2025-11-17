from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'client', 'status', 'created_on')
    search_fields = ('title', 'location', 'client__username')
    list_filter = ('location', 'status', 'created_on')
    ordering = ('status', 'created_on')