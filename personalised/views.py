from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import PersonalisedForm
from django.views.generic import FormView


# Create your views here.

def personalised_page(request):
    """ A view to return the personalised page """
    
    return render(request, 'personalised/personalised.html')

class PersonalisedOrder(FormView):
    template_name = 'personalised/order.html'
    form_class = PersonalisedForm
    success_url = reverse_lazy('order_summary')

    def form_valid(self, form):
        instance = form.save(commit=False)
        size_price_mapping = {
            'A4': 30,
            'A5': 25,
            'A6': 20,
        }
        instance.price = size_price_mapping.get(instance.size, 0)
        instance.order_total = instance.price
        instance.grand_total = instance.order_total
        instance.save()
        return super().form_valid(form)