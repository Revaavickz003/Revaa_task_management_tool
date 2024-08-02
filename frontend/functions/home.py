from django.shortcuts import render
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

from django.forms.models import model_to_dict
def calendar(request):
    event = events.objects.all()
    # Serialize the queryset to JSON
    events_json = serialize('json', event, fields=('id', 'summary', 'description', 'bgColor', 'start_date', 'end_date'))
    context = {
        'home': 'active',
        'nav-link-calender': 'custom-nav-link',
        'events': events_json  # Pass the JSON data to the template
    }
    return render(request, 'tmt-tool/Calendar.html', context)