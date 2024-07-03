from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from frontend.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def teams_details(request, pk):
    try:
        get_team = Team.objects.get(pk=pk)
        team_leader = EmployeeDetail.objects.filter(is_team_leader=True)
        team_members = get_team.members.all()
        get_project = Project.objects.filter(team=get_team)
        Priority = TaskSheet.PRIORITY_CHOICES
    except:
        messages.error(request, 'Team is not found')
        return redirect('teams')
    all_projects = Project.objects.filter(team=get_team)[::-1]
    all_customers = customersTable.objects.all()[::-1]
    context = {
        'team_leader':team_leader,
        'team_members':team_members,
        'get_project':get_project,
        'Priority':Priority,
        'teams_page': 'active',
        'get_team':get_team,
        'members':get_team.members,
        'all_projects':all_projects,
        'all_customers':all_customers,
    }
    
    return render(request, 'tmt-tool/team_details.html', context)

@login_required(login_url='login')
def addtask_teampage(request, pk):
    if request.method == 'POST':
        task_title = request.POST.get('taskname')
        assigned_to_id = request.POST.get('assignee')  # Assuming assignee is an ID
        project_id = request.POST.get('project')  # Assuming project is an ID
        status_id = request.POST.get('status')  # Assuming status is an ID
        task_type_id = request.POST.get('tasktype')  # Assuming tasktype is an ID
        priority = request.POST.get('priority')
        description = request.POST.get('taskdescription')
        attachment = request.FILES.get('attachment')  # Corrected 'Files' to 'FILES'
        if assigned_to_id and project_id and status_id and task_type_id:
            assigned_to = EmployeeDetail.objects.get(id=assigned_to_id)
            project = Project.objects.get(id=project_id)
            client=customersTable.objects.get(id=project.client.pk)
            statuss = status.objects.get(id=status_id)
            task_type = Type.objects.get(id=task_type_id)
            new_task = TaskSheet.objects.create(
                client=client,
                title=task_title,
                assigned_to=assigned_to,
                assigned_from=EmployeeDetail.objects.get(user=request.user),  # Assuming current user is assigning the task
                project=project,
                status=statuss,
                task_type=task_type,
                priority=priority,
                description=description,
                attachment=attachment
            )
            new_task.save()
            messages.success(request, 'Task added successfully')
            return redirect(reverse('taskopen', kwargs={'team_pk': pk, 'project_pk': project.pk, 'task_pk':new_task.pk}))

    else:
        # Handle GET request if needed
        return render(request, 'your_template.html', context={})
        