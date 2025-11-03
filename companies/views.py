from django.shortcuts import render

# Create your views here.
def view_companies_page(request):
    """
    Display the companies page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`companies_page.html`
    """
    return render(
        request,
        "companies_page.html",
        {
            # Context variable placeholder for the companies page view
        },
    )
