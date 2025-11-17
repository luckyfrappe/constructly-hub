from django.contrib import admin
from .models import Bid

# Register your models here.
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('company', 'price_offer', 'duration', 'message', 'created_on')
    search_fields = ('company__name', 'message')
    list_filter = ('created_on',)
    ordering = ('created_on',)