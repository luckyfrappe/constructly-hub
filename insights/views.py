from django.shortcuts import render

# Create your views here.

def view_insights_page(request):
    """
    Display the insights page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`insights_page.html`
    """
    return render(
        request,
        "insights_page.html",
        {
            # Context variable placeholder for the insights page view
        },
    )
