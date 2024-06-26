from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from frontend.models import *
from django.contrib.auth.decorators import login_required
import datetime as dt

def new_task(request, team_pk, project_pk):
    if request.method == 'POST':
        title = request.POST.get('taskname')
        assignee_id = request.POST.get('assigne')
        task_type_id = request.POST.get('tasktype')
        priority = request.POST.get('priority')
        description = request.POST.get('taskdiscriptions')
        attachment = request.FILES.get('attachment')
        project_id = request.POST.get('projectpk')
        status_id = request.POST.get('status')
        if all([title, assignee_id, task_type_id, priority, description, project_id, status_id]):
            try:
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
                    assigned_to=EmployeeDetail.objects.get(pk=assignee_id),
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


def taskopen(request, team_pk, project_pk, task_pk):
    task = TaskSheet.objects.get(pk=task_pk)
    get_team = Team.objects.get(pk=team_pk)
    get_project = Project.objects.get(pk=project_pk)
    team_members = get_team.members.all()
    Priority = TaskSheet.PRIORITY_CHOICES
    statuss = status.objects.filter(project=project_pk)
    commentss = comments.objects.filter(task=task)[::-1]
    context = {
        'teams_page': 'active',
        'task': task,
        'team': get_team,
        'get_project':get_project,
        'team_members': team_members,
        'Priority':Priority,
        'statuss':statuss,
        'commentss':commentss,
    }
    
    return render(request, 'tmt-tool/taskopen_page.html', context)

from django.http import JsonResponse

def starttimefortask(request, teampk, ppk, tpk):
    if request.method == 'POST':
        try:
            task = TaskSheet.objects.get(id=tpk)
            task.start_date_time = dt.datetime.now()
            task.save()
            return JsonResponse({'status': 'success', 'start_time': task.start_date_time})
        except TaskSheet.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def endtimefortask(request, teampk, ppk, tpk):
    if request.method == 'POST':
        try:
            task = TaskSheet.objects.get(id=tpk)
            task.end_date_time = dt.datetime.now()
            task.save()
            return JsonResponse({'status': 'success', 'end_time': task.end_date_time})
        except TaskSheet.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def deletetask(request, teampk, ppk, tpk):
    try:
        task = TaskSheet.objects.get(id=tpk)
        task.delete()
        messages.success(request, 'Task deleted success fully')
        return redirect(reverse('project_details', kwargs={'team_pk': teampk, 'project_pk': ppk}))
    except TaskSheet.DoesNotExist:
        messages.error(request, 'Task not found')
        return redirect(reverse('project_details', kwargs={'team_pk': teampk, 'project_pk': ppk}))
    
def updatetask(request, teampk, ppk, tpk):
    if request.method == 'POST':
        eta = request.POST.get('ETA')
        assignees_id = request.POST.get('Assignees')
        priority = request.POST.get('Priority')
        status_id = request.POST.get('Status')
        description = request.POST.get('description')
        attachment = request.FILES.get('Attachment')

        task = get_object_or_404(TaskSheet, pk=tpk)

        # Retrieve current values before update
        before_assignees = task.assigned_to
        before_priority = task.priority
        before_status = task.status
        before_description = task.description
        before_attachment = task.attachment

        # Update task with new values
        if eta:
            task.ETA = eta

        try:
            new_assignees = EmployeeDetail.objects.get(pk=assignees_id)
            task.assigned_to = new_assignees
            task.save()
            if before_assignees != new_assignees:
                comments.objects.create(
                    task=task,
                    comments="Changed task from",
                    BeforeAssignees=before_assignees,
                    AfterAssignees=new_assignees,
                    corrent_date_time = dt.datetime.now(),
                    user=EmployeeDetail.objects.get(user=request.user),
                )
        except EmployeeDetail.DoesNotExist:
            messages.error(request, "Invalid assignees")
            new_assignees = None

        try:
            new_status = status.objects.get(pk=status_id)
            if before_status != new_status:
                task.status = new_status
                task.save()
                comments.objects.create(
                    task=task,
                    comments=f"Status changed from",
                    BeforeStatus=before_status,
                    AfterStatus=new_status,
                    corrent_date_time = dt.datetime.now(),
                    user=EmployeeDetail.objects.get(user=request.user),
                )
        except status.DoesNotExist:
            messages.error(request, "Invalid Status")
            new_status = None

        if before_priority != priority:
            task.priority = priority
            comments.objects.create(
                task=task,
                comments="Changed priority for",
                BeforePriority=before_priority,
                AfterPriority=priority,
                corrent_date_time = dt.datetime.now(),
                user=EmployeeDetail.objects.get(user=request.user),
            )

        if before_description != description:
            task.description = description
            comments.objects.create(
                task=task,
                comments="Change description for ",
                BeforeDescription=before_description,
                AfterDescription=description,
                corrent_date_time = dt.datetime.now(),
                user=EmployeeDetail.objects.get(user=request.user),
            )

        if attachment:
            if before_attachment != attachment:
                task.attachment = attachment
                comments.objects.create(
                    task=task,
                    comments=f"Attachment changed",
                    BeforeAttachment=before_attachment,
                    AfterAttachment=attachment,
                    corrent_date_time = dt.datetime.now(),
                    user=EmployeeDetail.objects.get(user=request.user),
                )

        task.save()

        return redirect(reverse('taskopen', kwargs={'team_pk': teampk, 'project_pk': ppk, 'task_pk': tpk}))
    
def task_comments(request, teampk, ppk, tpk):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        comment_images = request.FILES.get('attachment')

        get_task = get_object_or_404(TaskSheet, pk=tpk)
        if not comment_images:
            comment_images = None
        comments.objects.create(
            task=get_task,
            user = EmployeeDetail.objects.get(user=request.user),
            comments=comment,
            comments_img = comment_images,
            corrent_date_time = dt.datetime.now()
        )

    return redirect(reverse('taskopen', kwargs={'team_pk':teampk, 'project_pk':ppk, 'task_pk':tpk}))