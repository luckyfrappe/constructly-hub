from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserProfile
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_userprofile_page(request):
    """
    Display the user profiles page.
    """
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if user_profile is None:
        messages.info(request, "Please update your profile.")
        return HttpResponseRedirect(reverse("settings"))
    else:
        return render(
            request,
            "userprofile_page.html",
            {
                "user_profile": user_profile
                # Context variable placeholder for the user profiles page view
            },
        )

def view_settings_page(request):
    """
    Display settings page.
    If user has no profile → allow create mode.
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
                messages.error(request, "Please correct the errors and try again.")
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
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully!")
                return HttpResponseRedirect(reverse("userprofile"))
            else:
                messages.error(request, "Please correct the errors and try again.")
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
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted successfully.")
    return redirect("landing")