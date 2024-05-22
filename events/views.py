from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from .forms import EventForm
from .models import Event


def event_list(request):
    events = Event.objects.all()
    now = datetime.now()
    saved_event_ids = []

    if request.user.is_authenticated:
        saved_event_ids = request.user.saved_events.values_list('id', flat=True)

    context = {
        'events': events,
        'saved_event_ids': saved_event_ids,
        'now': now,
    }

    return render(request, 'events/event_list.html', context)


@login_required
def save_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.add(request.user)
    messages.info(request, f'{event.title} added to your events.')
    return redirect('event_list')


@login_required
def unsave_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.remove(request.user)
    messages.info(request, f'Event "{event.title}" removed from saved events')
    return redirect('event_list')


@login_required
def unsave_event_profile(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.remove(request.user)
    event.save()
    messages.info(request, f'Event "{event.title}" removed from saved events')
    return redirect('saved_events')


@login_required
def add_event(request):
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('event_list'))
