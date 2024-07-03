from django.shortcuts import render
import datetime

def home(request):
    context = {
        'home': 'active',
    }
    return render(request, 'tmt-tool/home.html', context)

def date_view(request, date):
    return render(request, 'tmt-tool/home.html', {'date': date})