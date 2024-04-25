from django.shortcuts import render

# Create your views here.

def blog(request):
    """ A view to return the home page """
    
    return render(request, 'blog/blog.html')
