from django.shortcuts import render, redirect
from .models import AboutMe
from django.contrib.auth.decorators import login_required
from .forms import AboutMeForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def about_me(request):
    about = AboutMe.objects.all()
    context = {'about': about}
    return render(request, 'about/about_me.html', context)

@login_required
def edit_about_me(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    about, created = AboutMe.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            about = form.save()
            about.save()
            messages.success(request, 'Successfully updated about me!')
            return redirect(reverse('about_me'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = AboutMeForm(instance=about)
        messages.info(request, f'You are editing "About Me" page!')
    
    return render(request, 'about/edit_about_me.html', {'form': form, 'about': about})