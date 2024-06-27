from django.shortcuts import render
from frontend.models import EmployeeDetail, Team, Project

def teams(request):
    # Get all teams
    all_teams = Team.objects.all()
    team_leader = EmployeeDetail.objects.filter(is_team_leader=True)
    
    # Add project count to each team
    teams_with_project_count = []
    for team in all_teams:
        project_count = Project.objects.filter(team=team).count()
        teams_with_project_count.append({
            'team': team,
            'project_count': project_count
        })
    context = {
        'teams_page': 'active',
        'team_leaders' : team_leader,
        'all_employees' : EmployeeDetail.objects.filter(user__is_superuser=False),
        'teams_with_project_count': teams_with_project_count,
    }
    
    return render(request, 'tmt-tool/teams.html', context)
