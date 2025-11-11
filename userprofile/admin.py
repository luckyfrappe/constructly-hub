from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'display_email', 'phone', 'updated_on')
    search_fields = ('user', 'full_name', 'display_email', 'phone')
    list_filter = ('updated_on',)
    ordering = ('-updated_on',)