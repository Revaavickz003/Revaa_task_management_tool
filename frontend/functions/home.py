from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from frontend.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
import json

@login_required(login_url='/login')
def home(request):
    context = {
        'home': 'active',
        'nav-link-calender': 'custom-nav-link',
    }
    return render(request, 'tmt-tool/home.html', context)

@login_required(login_url='/login')
def date_view(request, date=None):
    if date is None:
        date = timezone.now().date()
    return render(request, 'tmt-tool/home.html', {'date': date})

@login_required(login_url='/login')
def calendar(request):
    event = events.objects.all()
    # Serialize the queryset to JSON
    events_json = serialize('json', event, fields=('id', 'name', 'description', 'color', 'start_date', 'end_date', 'typeOfEvent'))
    context = {
        'home': 'active',
        'nav-link-calender': 'custom-nav-link',
        'events_types': events.TYPE_OF_EVENT_CHOICES,
        'teams': Team.objects.all(),
        'events': events_json,
    }
    return render(request, 'tmt-tool/Calendar.html', context)

@login_required(login_url='/login')
def add_event(request):
    if request.method == 'POST':
        Summary = request.POST.get('name')
        Description = request.POST.get('description')
        Background_Color = request.POST.get('bgColor')
        eventType = request.POST.get('eventType')
        Start_Date = request.POST.get('start_date')
        satrt_time = request.POST.get('starttime')
        End_Date = request.POST.get('end_date')
        end_time = request.POST.get('endtime')
        
        if not satrt_time:
            satrt_time = "00:00"
        if not end_time:
            end_time = "00:00"

        event = events.objects.create(
            typeOfEvent = eventType,
            name=Summary, 
            description=Description, 
            color=Background_Color,
            start_date = Start_Date,
            satrt_time = satrt_time,
            end_date = End_Date,
            end_time = end_time,
            created_by = request.user,
            weekday = False,
        )
        event.save()

    return redirect('calendar')