from django.shortcuts import render, redirect
from frontend.models import EmployeeDetail, Team, Project
from django.contrib import messages

def teams_details(request, pk):
    try:
        get_team = Team.objects.get(pk=pk)
    except:
        messages.error(request, 'Team is not found')
        return redirect('teams')
    all_projects = Project.objects.filter(Team=get_team)[::-1]
    context = {
        'teams_page': 'active',
        'get_team':get_team,
        'all_projects':all_projects,
    }
    
    return render(request, 'tmt-tool/team_details.html', context)
