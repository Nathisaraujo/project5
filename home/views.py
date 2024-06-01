from django.shortcuts import render

# Create your views here.


def home_page(request):
    """ A view to return the home page """

    return render(request, 'home/home_page.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
