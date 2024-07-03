from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='/login')
def home(request):
    context = {
        'home': 'active',
    }
    return render(request, 'tmt-tool/home.html', context)

@login_required(login_url='/login')
def date_view(request, date=None):
    if date is None:
        date = timezone.now().date()
    return render(request, 'tmt-tool/home.html', {'date': date})


