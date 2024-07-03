from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from frontend.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_status(request,tpk, ppk, spk):
    if request.method == 'POST':
        statuss = status.objects.get(pk=spk)
        statuss.delete()
        messages.success(request, 'Status deleted successfully')
    return redirect(reverse('project_details', kwargs={'team_pk': tpk, 'project_pk': ppk}))

@login_required(login_url='login')
def update_status(request, tpk, ppk, spk):
    if request.method == 'POST':
        statuss = status.objects.get(pk=spk)
        statusname = request.POST.get('statusname')
        description = request.POST.get('description')
        color = request.POST.get('color')
        statuss.name = statusname
        statuss.description = description
        statuss.color = color
        statuss.save()
        messages.success(request, 'Status updated successfully')
    return redirect(reverse('project_details', kwargs={'team_pk': tpk, 'project_pk': ppk}))