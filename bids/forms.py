from django import forms
from .models import Bid
from companies.models import Company

class CreateBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ("company", "price_offer", "duration", "message")
        widgets = {
            "company": forms.HiddenInput(), 
        }