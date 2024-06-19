from django.shortcuts import render, redirect
from frontend.models import *
from django.contrib import messages
from django.urls import reverse
import datetime as dt

def projects_page(request):
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
        messages.success(request, 'Project Created Successfully')
        return redirect('project')

    context = {
        'Project': 'active',
        'all_teams': Team.objects.all(),
        'all_projects': Project.objects.exclude(status='Closed').order_by('-id'),
        'closed_projects': Project.objects.filter(status='Closed'),
    }
    
    return render(request, 'tmt-tool/project.html', context)

def closeproject(request, pk):
    project = Project.objects.get(pk=pk)
    project.status = 'Closed'
    project.save()
    messages.success(request, 'Project Closed Successfully')
    return redirect('project')

def openprojectteam(request, team):
    team = Team.objects.get(name=team)
    context = {'Project': 'active',
        'team':team,
        'all_teams': Team.objects.all(),
        'all_projects' : Project.objects.exclude(status='Closed').filter(Team=team).order_by('-id'),
        'closed_projects': Project.objects.filter(status='Closed'),
    }
    
    return render(request, 'tmt-tool/project.html', context)

def singleprojectopen(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = TaskSheet.objects.filter(project =project)[::-1]
    statuses = [status for status, _ in Project.STATUS_CHOICES]
    prioritis = [priority for priority, _ in Project.PRIORITY_CHOICES]
    
    context = {
        'Project': 'active',
        'project': project,
        'tasks':tasks,
        'statuses':statuses,
        'prioritis':prioritis,
        
    }
    return render(request, 'tmt-tool/singleprojectopen.html', context)  

def update_project_details(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        project_description = request.POST.get('project_discription')

        project.project_name = project_name
        project.project_discription = project_description
        project.updated_by = request.user
        project.updated_date = dt.datetime.today()
        project.save()

        messages.success(request, 'Project Details Updated Successfully')
        return redirect(reverse('singleprojectopen', kwargs={'pk': pk}))
    else:
        return redirect(reverse('singleprojectopen', kwargs={'pk': pk}))
    
def update_status_details(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        startdate = request.POST.get('start_date')
        enddate = request.POST.get('end_date')
        status = request.POST.get('projectstatus')
        priority = request.POST.get('projectpriority')

        project.start_date = startdate
        project.end_of_date = enddate
        project.status = status
        project.priority = priority
        project.updated_by = request.user
        project.updated_date = dt.datetime.today()
        project.save()

        messages.success(request, 'Project status Updated Successfully')
        return redirect(reverse('singleprojectopen', kwargs={'pk': pk}))
    else:
        return redirect(reverse('singleprojectopen', kwargs={'pk': pk}))