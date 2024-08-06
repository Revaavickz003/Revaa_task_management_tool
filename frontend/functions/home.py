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
    events_json = serialize('json', event, fields=('id', 'name', 'description', 'color', 'start_date', 'end_date'))
    context = {
        'home': 'active',
        'nav-link-calender': 'custom-nav-link',
        'events': events_json  # Pass the JSON data to the template
    }
    return render(request, 'tmt-tool/Calendar.html', context)

@login_required(login_url='/login')
def add_event(request):
    if request.method == 'POST':
        Summary = request.POST.get('name')
        Description = request.POST.get('description')
        Background_Color = request.POST.get('bgColor')
        Start_Date = request.POST.get('start_date')
        End_Date = request.POST.get('end_date')
        
        event = events.objects.create(
            name=Summary, 
            description=Description, 
            color=Background_Color,
            start_date = Start_Date,
            end_date = End_Date,
            created_by = request.user,
        )
        event.save()

    return redirect('calendar')