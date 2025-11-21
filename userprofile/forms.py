from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile details.

    model: `UserProfile`
    fields:
    - `bio`: short user description
    - `phone`: contact number
    - `display_email`: public email address
    - `avatar`: profile image
    - `full_name`: user's full name
    """

    class Meta:
        model = UserProfile
        fields = ("bio", "phone", "display_email", "avatar", "full_name",)
