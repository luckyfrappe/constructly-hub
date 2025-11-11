from django.shortcuts import redirect, render
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
    user_profile = get_object_or_404(UserProfile, user=request.user)

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
    Display the settings page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`settings_page.html`
    """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid() and user_profile.user == request.user:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully!")
        else:
            messages.add_message(request, messages.ERROR, "Please correct the errors and try again.")

    return render(
        request,
        "settings_page.html",
        {
            "user_profile": user_profile
            # Context variable placeholder for the settings page view
        },
    )

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account has been deleted successfully.")
    return redirect("landing")