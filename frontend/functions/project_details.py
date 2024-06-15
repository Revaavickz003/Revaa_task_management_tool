from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from frontend.models import *
def projects_details(request, team_pk, project_pk):
    try:
        get_team = Team.objects.get(pk=team_pk)
        get_project = Project.objects.get(pk=project_pk)
        statuss = status.objects.filter(project=get_project)
        types = Type.objects.filter(project=get_project)
        team_members = get_team.members.all()
        Priority = TaskSheet.PRIORITY_CHOICES
        tasks = TaskSheet.objects.filter(project=get_project)
        
    except:
        messages.error(request, "Invalid team or project")
        messages.error(request, 'Team is not found')
        return redirect('teams')
    
    context = {
        'teams_page': 'active',
        'get_team':get_team,
        'get_project':get_project,
        'statuss':statuss,
        'types':types,
        'team_members':team_members,
        'Priority':Priority,
        'tasks':tasks,
    }
    return render(request, 'tmt-tool/project_details.html', context)

def new_status(request, team_pk, project_pk):
    if request.method == 'POST':
        statusname = request.POST.get('statusname')
        description = request.POST.get('description')
        color = request.POST.get('color')
        
        try:
            project = Project.objects.get(pk=project_pk)
            new_status = status.objects.create(
                name=statusname,
                description=description,
                color=color,
                project=project
            )
            new_status.save()
            messages.success(request, 'New status added successfully')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
        except Project.DoesNotExist:
            messages.error(request, 'Project not found')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
        except Exception as e:
            messages.error(request, f'Error adding new status: {str(e)}')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
        

def new_type(request, team_pk, project_pk):
    if request.method == 'POST':
        typename = request.POST.get('typename')
        color = request.POST.get('color')
        
        try:
            project = Project.objects.get(pk=project_pk)
            new_status = Type.objects.create(
                name=typename,
                color=color,
                project=project
            )
            new_status.save()
            messages.success(request, f'Type {new_status.name} added successfully')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
        except Project.DoesNotExist:
            messages.error(request, 'Project not found')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
        except Exception as e:
            messages.error(request, f'Error adding new type: {str(e)}')
            return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
    