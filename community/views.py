from django.shortcuts import render

# Create your views here.


def community_page(request):
    """ A view to return the home page """

    return render(request, 'community/community_page.html')
