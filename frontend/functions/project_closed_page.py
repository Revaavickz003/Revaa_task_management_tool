from django.shortcuts import render, redirect
from frontend.models import Team, Project
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def close_projects_page(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        project_description = request.POST.get('discription')
        project_team = request.POST.get('selectteam')

        try:
            project_team = Team.objects.get(pk=project_team)
        except:
            project_team = None

        new_project = Project.objects.create(
            project_name = project_name,
            project_discription = project_description,
            Team = project_team,

            created_by = request.user,
            updated_by = request.user,
        )
        new_project.save()
        return redirect('project')

    context = {
        'Project': 'active',
        'closed_project_page':True,
        'all_teams': Team.objects.all(),
        'all_projects': Project.objects.filter(status='Closed').order_by('-id'),
        'closed_projects': Project.objects.exclude(status='Closed').order_by('-id'),
    }
    
    return render(request, 'tmt-tool/project.html', context)

@login_required(login_url='login')
def Reopen(request, pk):
    project = Project.objects.get(pk=pk)
    project.status = 'On Process'
    project.save()
    messages.success(request, 'Project Reopen Successfully')
    return redirect('close_projects_page')

@login_required(login_url='login')
def closeprojectteam(request, team):
    team = Team.objects.get(name=team)
    context = {'Project': 'active',
        'team':team,
        'closed_project_page':True,
        'all_teams': Team.objects.all(),
        'all_projects' : Project.objects.filter(status='Closed').filter(Team=team).order_by('-id'),
        'closed_projects': Project.objects.filter(status='Closed'),
    }
    
    return render(request, 'tmt-tool/project.html', context)