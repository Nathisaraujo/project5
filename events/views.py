from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from profiles.models import UserProfile
from .forms import EventForm
from .models import Event


def event_list(request):
    """
    Display a list of events, including those saved by the user.

    Retrieves all events from the database and determines if each event
    has been saved by the authenticated user. Generates JSON data for the
    events. Passes the events data to the template for rendering.
    """
    events = Event.objects.all()
    now = datetime.now()

    if request.user.is_authenticated:
        saved_event_ids = Event.objects.filter(
            save_event=request.user
        ).values_list(
            'id', flat=True
        )
    else:
        saved_event_ids = []
    events_json = serializers.serialize('json', events)

    context = {
        'events_json': events_json,
        'events': events,
        'saved_event_ids': saved_event_ids,
        'now': now,
    }

    return render(request, 'events/event_list.html', context)


@login_required
def save_event(request, event_id):
    """
    Save an event to the user's saved events list.

    Fetches the event by its ID and adds the current user to the list of users
    who have saved the event. Sends a reminder email if the event is happening
    tomorrow. Redirects to the event list page.
    """
    event = get_object_or_404(Event, pk=event_id)
    tomorrow = timezone.now() + timezone.timedelta(days=1)
    event.save_event.add(request.user)
    event.save()
    send_event_reminders(event)

    if event.date_and_time.date() == tomorrow.date():
        messages.info(
            request,
            f'{event.title} added to your events. '
            'A reminder email will be sent one day before the event.'
        )
    else:
        messages.info(request, f'{event.title} added to your events.')
    return redirect('event_list')


def send_event_reminders(event):
    tomorrow = timezone.now() + timezone.timedelta(days=1)

    if event.date_and_time.date() == tomorrow.date():
        for user in event.save_event.all():
            profile = UserProfile.objects.get(user=user)
            send_mail(
                'Drawing Gratitude - Event Reminder',
                f"Don't forget, '{event.title}' is happening tomorrow!",
                'drawinggratitude@email.com',
                [profile.user.email],
                fail_silently=False,
            )


@login_required
def unsave_event(request, event_id):
    """
    Remove an event from the user's saved events list.

    Fetches the event by its ID and removes the current user from the list
    of users who have saved the event. Redirects to the event list page.
    """
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.remove(request.user)
    event.save()
    messages.info(request, f'Event "{event.title}" removed from saved events')
    return redirect('event_list')


@login_required
def unsave_event_profile(request, event_id):
    """
    Remove an event from the user's saved events list from the profile page.

    Fetches the event by its ID and removes the current user from the list
    of users who have saved the event. Redirects to the saved events page.
    """
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.remove(request.user)
    event.save()
    messages.info(request, f'Event "{event.title}" removed from saved events')
    return redirect('saved_events')


@login_required
def add_event(request):
    """
    Add a new event.

    Allows store owners to add new events. Validates the form data and saves
    the event to the database. Redirects to the event list page upon success.

    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            date_and_time = form.cleaned_data.get('date_and_time')
            if date_and_time is not None and date_and_time < timezone.now():
                messages.error(request, "Event date must be in the future.")
                return render(request, 'events/add_event.html', {'form': form})
            else:
                event.save()
                messages.success(request, 'Successfully added event!')
                return redirect(reverse('event_list'))
        else:
            messages.error(
                request,
                'Failed to add event. Please ensure the form is valid.'
            )
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """
    Edit an existing event.

    Allows store owners to edit existing events. Validates the form data and
    updates the event in the database. Redirects to the event list page upon
    success.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect(reverse('event_list'))
        else:
            messages.error(
                request,
                'Failed to update event. Please ensure the form is valid.'
            )

    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    return render(
        request,
        'events/edit_event.html',
        {'form': form, 'event': event}
    )


@login_required
def delete_event(request, event_id):
    """
    Delete an event.

    Allows only admins to delete events. Fetches the event
    by its ID and deletes it from the database. Redirects to the event list
    page upon successful deletion.

    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('event_list'))
