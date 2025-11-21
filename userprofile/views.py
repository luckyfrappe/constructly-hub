from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from bids.models import Bid
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def view_userprofile_page(request):
    """
    Displays the logged-in user's profile page.

    model: `UserProfile`, `Bid`
    form: none

    **context**
    - `user_profile`: logged-in user profile instance
    - `total_bids`: number of bids posted on user's projects

    template: `userprofile_page.html`
    """

    user_profile = UserProfile.objects.filter(user=request.user).first()

    user_projects = user_profile.user.projects.all()
    total_bids = Bid.objects.filter(project__in=user_projects).count()

    if user_profile is None:
        messages.error(request, "Please update your profile.")
        return HttpResponseRedirect(reverse("settings"))
    else:
        return render(
            request,
            "userprofile_page.html",
            {
                "user_profile": user_profile,
                "total_bids": total_bids,
            },
        )


@login_required
def view_settings_page(request):
    """
    Displays the settings page for creating or editing a user profile.

    model: `UserProfile`
    form: `UserProfileForm`

    **context**
    - `form`: form instance (create or edit mode)
    - `user_profile`: only in edit mode

    template: `settings_page.html`
    """

    user_profile = UserProfile.objects.filter(user=request.user).first()

    # Build with help from ChatGPT
    # CREATE MODE (no profile yet)
    if user_profile is None:
        if request.method == "POST":
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                new_profile = form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
                messages.success(request, "Profile created successfully!")
                return HttpResponseRedirect(reverse("userprofile"))
            else:
                messages.error(
                    request,
                    "Please correct the errors and try again.")
        else:
            form = UserProfileForm()

        return render(
            request,
            "settings_page.html",
            {
                "form": form,
            },
        )

    # EDIT MODE
    else:
        if request.method == "POST":
            form = UserProfileForm(
                request.POST,
                request.FILES,
                instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully!")
                return HttpResponseRedirect(reverse("userprofile"))
            else:
                messages.error(
                    request,
                    "Please correct the errors and try again.")
        else:
            form = UserProfileForm(instance=user_profile)

        return render(
            request,
            "settings_page.html",
            {
                "form": form,
                "user_profile": user_profile,
            },
        )


@login_required
def delete_account(request):
    """
    Deletes the logged-in user's account and redirects to landing.

    models: `User`

    redirect: `landing`
    """

    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted successfully.")
    return redirect("landing")
