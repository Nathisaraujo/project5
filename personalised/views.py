from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import PersonalisedForm
from django.views.generic import FormView
from .models import Personalised
from django.contrib.auth.decorators import login_required

# Create your views here.

def personalised_page(request):
    """ A view to return the personalised page """
    
    return render(request, 'personalised/personalised.html')

@login_required
def PersonalisedOrder(request):
    if request.method == 'POST':
        form = PersonalisedForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            if order.size == 'A4':
                order.total_price = 30
            elif order.size == 'A6':
                order.total_price = 25
            else:
                order.total_price = 20
            order.save()
            return redirect('order_summary')
    else:
        form = PersonalisedForm()
    return render(request, 'personalised/order.html', {'form': form})

@login_required
def order_summary(request):
    orders = Personalised.objects.all()
    return render(request, 'personalised/order_summary.html', {'orders': orders})