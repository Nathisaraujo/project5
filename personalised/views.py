from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse


# Create your views here.

def personalised_page(request):
    """ A view to return the personalised page """
    
    return render(request, 'personalised/personalised.html')

