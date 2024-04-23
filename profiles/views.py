from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, RecommendationForm

from checkout.models import Order

# Create your views here.

def profile(request):
    """ Display the user's profile. """
    if request.user.is_authenticated:
        user_info = UserProfile.objects.get(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'on_profile_page': True,
        'user_info': user_info,
    }

    return render(request, template, context)

def update_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)

def orders(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()
    template = 'profiles/orders.html'

    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def recommend(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            return redirect('recommendation_success')
    else:
        form = RecommendationForm()
    return render(request, 'profiles/recommendation_form.html', {'form': form})

def recommendation_success(request):
    return render(request, 'profiles/recommendation_success.html')