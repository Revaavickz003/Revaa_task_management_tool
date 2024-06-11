from django.shortcuts import redirect, render
from frontend.models import Team, EmployeeDetail
from django.contrib import messages

def create_team(request):
    if request.method == 'POST':
        team_logo = request.FILES.get('team_logo')
        team_name = request.POST.get('teamname')
        team_lead = request.POST.get('teamlead')
        team_description = request.POST.get('teamdiscriptions')
        selected_employees = request.POST.getlist('selectemployees')

        # Create a new Team object
        try:
            team_lead = EmployeeDetail.objects.get(pk=team_lead)
        except EmployeeDetail.DoesNotExist:
            messages.error(request, "Team Lead not found")
            return redirect('teams')
        
        team = Team.objects.create(
            name=team_name,
            leader=team_lead,
            description=team_description,
            team_logo=team_logo
        )

        # Add employees to the team
        for employee_id in selected_employees:
            try:
                employee = EmployeeDetail.objects.get(pk=employee_id)
                team.members.add(employee)
            except EmployeeDetail.DoesNotExist:
                messages.error(request, f"Employee with ID {employee_id} not found")
        messages.success(request, 'Team Created Succesfully')
        
    return redirect('teams')

    
