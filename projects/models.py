from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=100, choices=[
        ('open', 'Open'),
        ('completed', 'Completed'),
    ], default='open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deadline = models.DateField()

    class Meta:
        ordering = ["created_on"]