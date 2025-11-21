from django import forms
from companies.models import Company
from .models import Bid


class CreateBidForm(forms.ModelForm):
    """
    Form for submitting a bid on a project.

    model: `Bid`
    fields:
    - `company`: the company submitting the bid (hidden in the form)
    - `price_offer`: offered price
    - `duration`: projected duration
    - `message`: optional message from the bidder
    """

    class Meta:
        model = Bid
        fields = ("company", "price_offer", "duration", "message")
        widgets = {
            "company": forms.HiddenInput(),
        }
