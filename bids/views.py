from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Bid

# Create your views here.
class UserBidsListView(generic.ListView):
    template_name = "bids/bids_page.html"
    context_object_name = "bids"
    paginate_by = 9

    def get_queryset(self):
        return Bid.objects.filter(
            company__owner=self.request.user
        ).order_by("-created_on")

def select_bid(request, bid_id):
    project = get_object_or_404(Bid, pk=bid_id).project
    bid = get_object_or_404(Bid, pk=bid_id)
    bid.status = 'accepted'
    bid.save()
    Bid.objects.filter(project=project).exclude(pk=bid_id).update(status='rejected')
    project.status = 'completed'
    project.save()
    return redirect('project_detail', pk=project.id)
    