from django.shortcuts import render
import datetime

def teams(request):
    context = {
        'teams':'active'
    }
    return render(request, 'tmt-tool/teams.html', context)
