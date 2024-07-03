from django.shortcuts import render
import datetime
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def home(request):
    context = {
        'home': 'active',
    }
    return render(request, 'tmt-tool/home.html', context)

@login_required(login_url='login')
def date_view(request, date):
    return render(request, 'tmt-tool/home.html', {'date': date})