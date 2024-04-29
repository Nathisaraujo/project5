from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.core.mail import send_mail
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from profiles.models import UserProfile
from datetime import datetime

from django.db.models import Q

def event_list(request):
    events = Event.objects.all()
    now = datetime.now()

    if request.user.is_authenticated:
        saved_event_ids = Event.objects.filter(save_event=request.user).values_list('id', flat=True)
    else:
        saved_event_ids = []

    # Serialize events queryset to JSON object
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
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.add(request.user)
    event.save()

    send_event_reminders(event)

    messages.success(request, f'{event.title} to your events. A reminder email will be sent one day before the event.')

    return redirect('event_list')

def send_event_reminders(event):
    tomorrow = timezone.now() + timezone.timedelta(days=1)

    if event.date_and_time.date() == tomorrow.date():
        # Find users who have saved the event and send them reminders
        for user in event.save_event.all():
            profile = UserProfile.objects.get(user=user)
            send_mail(
                'Drawing Gratitude - Event Reminder',
                f"Don't forget, '{event.title}' is happening tomorrow!",
                'drawinggratitude@email.com',
                [profile.user.email],
                fail_silently=False,
            )
        
    event.has_passed = event.date_and_time < timezone.now()
    event.save()

@login_required
def unsave_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.save_event.remove(request.user)
    event.save()
    messages.success(request, f'Event "{event.title}" removed from saved events')
    return redirect('event_list')