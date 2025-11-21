from django.contrib import admin
from .models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for model Bid.

    Displays bid details such as company, price, duration,
    message, and creation date.
    """

    list_display = ('company',
                    'price_offer',
                    'duration',
                    'message',
                    'created_on')
    search_fields = ('company__name', 'message')
    list_filter = ('created_on',)
    ordering = ('created_on',)
