from django.shortcuts import render
from .models import AboutMe

# Create your views here.

def about_me(request):
    about = AboutMe.objects.all()
    context = {'about': about}
    return render(request, 'about/about_me.html', context)
