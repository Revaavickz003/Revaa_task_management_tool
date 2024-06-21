from django.shortcuts import render, redirect, get_object_or_404
from frontend.models import *
from django.contrib import messages

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

        # Retrieve objects related to the IDs
        assigned_to = get_object_or_404(EmployeeDetail, id=assigned_to_id)
        project = get_object_or_404(Project, id=project_id)
        status = get_object_or_404(status, id=status_id)
        task_type = get_object_or_404(Type, id=task_type_id)

        # Create a new task object
        new_task = TaskSheet.objects.create(
            title=task_title,
            assigned_to=assigned_to,
            assigned_from=request.user.employeedetail,  # Assuming current user is assigning the task
            project=project,
            status=status,
            task_type=task_type,
            priority=priority,
            description=description,
            attachment=attachment
        )

        # Save the task object
        new_task.save()

        # Redirect to a success URL or render a success template
        return redirect('success_url_name')  # Replace 'success_url_name' with your actual success URL name
    else:
        # Handle GET request if needed
        return render(request, 'your_template.html', context={})
        