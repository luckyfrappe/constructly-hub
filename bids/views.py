from django.shortcuts import get_object_or_404, redirect, render
from .models import Bid

# Create your views here.

def view_bids_page(request):
    """
    Display the bids page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`bids_page.html`
    """
    return render(
        request,
        "bids_page.html",
        {
            # Context variable placeholder for the bids page view
        },
    )

def select_bid(request, bid_id):
    project = get_object_or_404(Bid, pk=bid_id).project
    bid = get_object_or_404(Bid, pk=bid_id)
    bid.status = 'accepted'
    bid.save()
    Bid.objects.filter(project=project).exclude(pk=bid_id).update(status='rejected')
    project.status = 'completed'
    project.save()
    return redirect('project_detail', pk=project.id)
    