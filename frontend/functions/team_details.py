from django.shortcuts import render, redirect
from frontend.models import *
from django.contrib import messages

def teams_details(request, pk):
    try:
        get_team = Team.objects.get(pk=pk)
    except:
        messages.error(request, 'Team is not found')
        return redirect('teams')
    all_projects = Project.objects.filter(team=get_team)[::-1]
    all_customers = customersTable.objects.all()[::-1]
    context = {
        'teams_page': 'active',
        'get_team':get_team,
        'all_projects':all_projects,
        'all_customers':all_customers,
    }
    
    return render(request, 'tmt-tool/team_details.html', context)
