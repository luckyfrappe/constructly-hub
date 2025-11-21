from django.db import models
from django.contrib.auth.models import User


class Bid(models.Model):
    """
    Represents a bid submitted by a company for a specific project.

    model: `projects.Project`, `companies.Company`
    Stores pricing, duration, message, and bid status.

    Used throughout the app to display bids, accept/reject them,
    and filter bids by project or company.
    """

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="bids")
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="contractor")
    price_offer = models.DecimalField(
        max_digits=12,
        decimal_places=2)
    duration = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')

    class Meta:
        ordering = ["-created_on"]
