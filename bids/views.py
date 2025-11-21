from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Bid


class UserBidsListView(generic.ListView):
    """
    Displays all bids submitted by the logged-in user's companies.

    model: `Bid`

    **context**
    - `bids`: queryset of bids related to companies owned by the user

    template: `bids/bids_page.html`
    """

    template_name = "bids/bids_page.html"
    context_object_name = "bids"
    paginate_by = 9

    def get_queryset(self):
        return Bid.objects.filter(
            company__owner=self.request.user
        ).order_by("-created_on")


def select_bid(request, bid_id):
    """
    Marks a bid as accepted, rejects all other bids for the same project,
    and marks the project as completed.

    model: `Bid`

    redirects:
    - `project_detail` after processing
    """

    project = get_object_or_404(Bid, pk=bid_id).project
    bid = get_object_or_404(Bid, pk=bid_id)
    bid.status = 'accepted'
    bid.save()
    Bid.objects.filter(
        project=project).exclude(pk=bid_id).update(status='rejected')
    project.status = 'completed'
    project.save()
    return redirect('project_detail', pk=project.id)
