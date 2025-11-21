from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    Represents additional profile information for a user.

    model: `User` (OneToOneField)
    Stores personal details such as full name, avatar, public email,
    phone number, biography, and last update timestamp.

    Used across the application to display and manage extended user data.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="userprofile")
    full_name = models.CharField(max_length=255)
    avatar = CloudinaryField('image', default='default_avatar')
    display_email = models.EmailField(max_length=255, unique=True, default='')
    phone = models.CharField(max_length=20, default='')
    bio = models.TextField(max_length=1000, default='')
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]
        verbose_name_plural = "User Profiles"
