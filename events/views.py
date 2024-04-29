from django.shortcuts import render
from django.core import serializers  # Import the serializers module
from .models import Event

def event_list(request):
    events = Event.objects.all()

    # Serialize events queryset to JSON object
    events_json = serializers.serialize('json', events)
    
    context = {
        'events_json': events_json,
        'events': events,
    }
    
    return render(request, 'events/event_list.html', context)
