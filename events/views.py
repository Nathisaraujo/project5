from django.shortcuts import render, redirect
from django.core import serializers  # Import the serializers module
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def event_list(request):
    events = Event.objects.all()

    # Serialize events queryset to JSON object
    events_json = serializers.serialize('json', events)
    
    context = {
        'events_json': events_json,
        'events': events,
    }
    
    return render(request, 'events/event_list.html', context)

@login_required
def save_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.save_event.add(request.user)
    event.save()
    messages.success(request, f'{event.title} to your events')

    return redirect('event_list')
