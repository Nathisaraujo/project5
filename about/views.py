from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import AboutMe
from .forms import AboutMeForm


# Create your views here.


def about_me(request):
    """
    View function to render the About Me page.
    Retrieves all AboutMe objects and passes them to the template.
    """
    about = AboutMe.objects.all()
    context = {'about': about}
    return render(request, 'about/about_me.html', context)


@login_required
def edit_about_me(request):
    """
    View function to edit the About Me page.
    Admin can edit the About Me page content.
    """
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
            messages.error(
                request,
                'Failed to add event. Please ensure the form is valid.'
            )
    else:
        form = AboutMeForm(instance=about)
        messages.info(request, f'You are editing "About Me" page!')

    return render(request, 'about/edit_about_me.html',
                  {'form': form, 'about': about})
