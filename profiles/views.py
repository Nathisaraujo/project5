from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, RecommendationForm
from events.models import Event
from wishlist.models import Wishlist
from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile.
    Retrieve the user's profile information.
    """
    if request.user.is_authenticated:
        user_info = UserProfile.objects.get(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'on_profile_page': True,
        'user_info': user_info,
    }

    return render(request, template, context)


@login_required
def update_profile(request):
    """Update the user's profile.
    Retrieve the user's profile and handle form submission
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """
    This view displays the user's wishlist
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, 'profiles/wishlist.html', context)


@login_required
def orders(request):
    """Display the user's orders."""
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'profiles/orders.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """Display the details of a specific order."""
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


@login_required
def recommend(request):
    """Allow users to submit recommendations."""
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            messages.success(
                request,
                'Recommendation Submitted Successfully. '
                'Thank you for your recommendation!'
            )
            return redirect('profile')
    else:
        form = RecommendationForm()

    return render(request, 'profiles/recommendation_form.html', {'form': form})


def recommendation_success(request):
    return render(request, 'profiles/recommendation_success.html')


@login_required
def saved_events(request):
    """Displays events saved by the user."""
    saved_events = Event.objects.filter(save_event=request.user)

    return render(
        request,
        'profiles/saved_events.html',
        {'saved_events': saved_events}
    )


@login_required
def management(request):
    """Displays the admin management page."""

    return render(request, 'profiles/management.html')
