from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=500)
    full_description = models.TextField(max_length=2000, blank=True, null=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = CloudinaryField('image', default='placeholder')
    services = models.CharField(max_length=255, help_text="Comma-separated list of services offered")
    role = models.CharField(max_length=255, help_text="Owner's role in the company")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
        verbose_name_plural = "Companies"
    def __str__(self):
        return self.company_name
    