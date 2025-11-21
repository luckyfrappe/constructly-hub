from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the `UserProfile` model.

    Displays user profile details, including name, email, and phone,
    and allows searching and filtering by key fields.
    """

    list_display = ('user',
                    'full_name',
                    'display_email',
                    'phone',
                    'updated_on')
    search_fields = ('user__username', 'full_name', 'display_email', 'phone')
    list_filter = ('updated_on',)
    ordering = ('-updated_on',)
