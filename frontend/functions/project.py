from django.shortcuts import render, redirect, get_object_or_404
from frontend.models import *
from django.contrib import messages
from django.urls import reverse
import datetime as dt
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def projects_page(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        project_description = request.POST.get('discription')
        project_team = request.POST.get('selectteam')
        client_id = request.POST.get('Clientdetails')

        try:
            project = ProductTable.objects.get(pk=int(project_name))
            project_team = Team.objects.get(pk=project_team)
            client = customersTable.objects.get(pk=client_id)
        except :
            messages.error(request, 'Fill All Fields')
            return redirect('project')

        new_project = Project.objects.create(
            project_name=f"{client.companyname} {project.Product_Name}",
            project_description=project_description,
            team=project_team,
            client=client,
            created_by=request.user,
            updated_by=request.user,
        )
        new_project.save()
        statuses = [
            {'name': 'To Do', 'description': 'Task is pending', 'color': status.GRAY},
            {'name': 'On Process', 'description': 'Task is in progress', 'color': status.BLUE},
            {'name': 'Completed', 'description': 'Task is completed', 'color': status.GREEN},
        ]
        for status_data in statuses:
            status.objects.create(
                project=new_project,
                name=status_data['name'],
                description=status_data['description'],
                color=status_data['color']
            )

        messages.success(request, 'Project Created Successfully')
        return redirect('project')

    context = {
        'Project': 'active',
        'all_teams': Team.objects.all(),
        'all_projects': Project.objects.exclude(status='Closed').order_by('-id'),
        'closed_projects': Project.objects.filter(status='Closed'),
        'all_customers': customersTable.objects.all()[::-1]
    }

    return render(request, 'tmt-tool/project.html', context)

def get_projects(request, client_id):
    client = get_object_or_404(customersTable, pk=client_id)
    products = client.products.all()
    project_list = [{'id': product.id, 'name': product.Product_Name} for product in products]
    return JsonResponse({'projects': project_list})

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
        'all_projects' : Project.objects.exclude(status='Closed').filter(team=team).order_by('-id'),
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