from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from frontend.models import *
from django.contrib.auth.decorators import login_required

def new_task(request, team_pk, project_pk):
    if request.method == 'POST':
        title = request.POST.get('taskname')
        assignee_id = request.POST.get('assigne')
        task_type_id = request.POST.get('tasktype')
        priority = request.POST.get('priority')
        description = request.POST.get('taskdiscriptions')
        attachment = request.FILES.get('attachment')
        project_id = request.POST.get('projectpk')
        status_id = request.POST.get('statuspk')
        if all([title, assignee_id, task_type_id, priority, description, project_id, status_id]):
            try:
                assignee = EmployeeDetail.objects.get(pk=assignee_id)
                project = Project.objects.get(pk=project_id)
                client = customersTable.objects.get(pk=project.client.pk)
                task_type = Type.objects.get(pk=task_type_id)
                task_status = status.objects.get(pk=status_id)
                task = TaskSheet.objects.create(
                    client=client,
                    title=title,
                    description=description,
                    attachment=attachment,
                    project=project,
                    status=task_status,
                    assigned_to=assignee,
                    task_type=task_type,
                    priority=priority,
                    assigned_from=EmployeeDetail.objects.get(user=request.user.pk),
                )
                task.save()
                messages.success(request, f'Task #{task.pk} {task.title} created successfully')
            except EmployeeDetail.DoesNotExist:
                messages.error(request, 'Invalid assignee')
            except Project.DoesNotExist:
                messages.error(request, 'Invalid project')
            except Type.DoesNotExist:
                messages.error(request, 'Invalid task type')
            except status.DoesNotExist:
                messages.error(request, 'Invalid status')
            except Exception as e:
                messages.error(request, f'Failed to create task: {e}') 
                #ailed to create task: Cannot assign "<User: vignesh@gmail.com>": "TaskSheet.assigned_to" must be a "EmployeeDetail" instance.
        else:
            messages.error(request, "Please fill all the fields")

    return redirect(reverse('project_details', kwargs={'team_pk': team_pk, 'project_pk': project_pk}))
