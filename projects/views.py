from django.shortcuts import render

# Create your views here.

def view_projects_page(request):
    """
    Display the projects page.

    **Context**

    ``request``
        The HTTP request object.

    **Template:**

    :template:`projects_page.html`
    """
    return render(
        request,
        "projects_page.html",
        {
            # Context variable placeholder for the projects page view
        },
    )
