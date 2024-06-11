from django.shortcuts import render, redirect
from django.contrib import messages
from frontend.models import *
def projects_details(request, team_pk, project_pk):
    try:
        get_team = Team.objects.get(pk=team_pk)
    except:
        messages.error(request, 'Team is not found')
        return redirect('teams')
    all_projects = Project.objects.filter(Team=get_team)
    context = {
        'teams_page': 'active',
        'get_team':get_team,
        'all_projects':all_projects,
    }
    return render(request, 'tmt-tool/project_details.html', context)
