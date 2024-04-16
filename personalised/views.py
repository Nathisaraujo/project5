from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import OrderPersonalised
from .forms import PersonalisedOrderForm


# Create your views here.

def personalised_page(request):
    """ A view to return the personalised page """
    
    return render(request, 'personalised/personalised.html')

# def order_page(request):
#     """ A view to return the personalised design order page """
    
#     return render(request, 'personalised/order.html')

def personalised_order(request):
    
    if request.method == 'POST':
        personalised_order_form = PersonalisedOrderForm(request.POST, request.FILES)
        if personalised_order_form.is_valid():
            personalised_order = personalised_order_form.save(commit=False)
            personalised_order.price = personalised_order.calculate_total_price()
            personalised_order.save()

            # Add personalised order to bag
            bag = request.session.get('bag', {})
            bag_item = {
                'product_id': personalised_order.id,
                'quantity': 1,
                'price': personalised_order.price,
            }
            bag['personalised_order'] = bag_item
            request.session['bag'] = bag

            messages.success(request, 'Personalised product added to your bag!')
            return redirect('personalised')  # Redirect to personalised page after adding to bag
        else:
            messages.error(request, 'Error occurred. Please check your form data.')
    else:
        personalised_order_form = PersonalisedOrderForm()

    context = {
        'personalised_order_form': personalised_order_form,
    }
    return render(request, 'personalised/order.html', context)