from django.shortcuts import render

# Create your views here.

def personalised_page(request):
    """ A view to return the personalised page """
    
    return render(request, 'personalised/personalised.html')