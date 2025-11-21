from django.shortcuts import render


def view_landing_page(request):
    """
    Renders the public landing page.

    template: landing_page.html
    """

    return render(
        request,
        "landing_page.html",
        {
            # Context variable placeholder for the landing page view
        },
    )
