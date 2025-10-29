from django.shortcuts import render

# Create your views here.
def view_landing_page(request):
    """
    Display the landing page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`landing_page.html`
    """

    return render(
        request,
        "landing_page.html",
        {
            # Context variable placeholder for the landing page view
        },
    )