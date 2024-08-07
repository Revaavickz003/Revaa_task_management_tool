from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from frontend.models import *
from django.core.serializers import serialize
import json
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta, datetime

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
    events_json = serialize('json', event, fields=('id', 'name', 'description', 'meeting_url', 'color', 'start_date', 'end_date', 'typeOfEvent', 'updated_by'))
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
        messages.success(request, f"{eventType} Added successfully...")

    return redirect('calendar')



@login_required(login_url='/login')
def recurring_event(request):
    if request.method == 'POST':
        eventType = request.POST.get('eventType')
        Summary = request.POST.get('eventSummary')
        Description = request.POST.get('description')
        Background_Color = request.POST.get('bgColor')
        select_team = request.POST.getlist('selectemployees')
        all_monday = request.POST.get('monday')
        all_tuesday = request.POST.get('tuesday')
        all_wednesday = request.POST.get('wednesday')
        all_thursday = request.POST.get('thursday')
        all_friday = request.POST.get('friday')
        all_saturday = request.POST.get('saturday')

        custom_days = {
            'monday': all_monday,
            'tuesday': all_tuesday,
            'wednesday': all_wednesday,
            'thursday': all_thursday,
            'friday': all_friday,
            'saturday': all_saturday
        }

        day_indices = {
            'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday': 4,
            'saturday': 5
        }

        today = now().date()
        events_list = []

        for day, is_selected in custom_days.items():
            if is_selected:
                next_date = today + timedelta((day_indices[day] - today.weekday() + 7) % 7)
                for _ in range(4):
                    events_list.append(events(
                        typeOfEvent=eventType,
                        name=Summary,
                        description=Description,
                        color=Background_Color,
                        start_date=next_date,
                        end_date=next_date,  # Assuming end_date is the same as start_date, adjust if needed
                        created_by=request.user,
                        updated_by=request.user
                    ))
                    next_date += timedelta(days=7)

        for event in events_list:
            event.save()
            if select_team:
                event.all_team = False
                event.team.set(select_team)
            else:
                event.all_team = True

        return redirect('calendar')

@login_required(login_url='/login')
def delete_event(request, epk):
    if request.method == 'POST':
        get_event = events.objects.get(pk = epk)
        get_event.delete()
        messages.success(request, f"{get_event.typeOfEvent} Deleted successfully...")
    return redirect('calendar')