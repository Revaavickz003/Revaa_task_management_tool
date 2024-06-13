from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from frontend.functions import (
    home,
    login_page,
    project,
    messages,
    teams,
    add_employee,
    project_closed_page,
    new_team_create,
    team_details,
    project_details,
)

urlpatterns = [

    # Side bar
    path('', home.home, name='home'),
    path('login/', login_page.login_view, name='login'),
    path('home/<str:date>/', home.date_view, name='datehome'),
    path('project/', project.projects_page, name='project'),
    path('messages/', messages.messages, name='messages'),
    path('teams/', teams.teams, name='teams'),
    
    # Open project page
    path('project/closed/<int:pk>/', project.closeproject, name='closeproject'),
    path('project/team/<str:team>/', project.openprojectteam, name='openprojectteam'),

    # Close project page
    path('project/closed/', project_closed_page.close_projects_page, name='close_projects_page'),
    path('project/closed/<str:team>/', project_closed_page.closeprojectteam, name='closeprojectteam'),
    path('project/reopen/<int:pk>/', project_closed_page.Reopen, name='reopen'),
    path('createprojectstatus/<int:team_pk>/<int:project_pk>/', project_details.new_status, name='createprojectstatus'),
    path('createprojecttype/<int:team_pk>/<int:project_pk>/', project_details.new_type, name='createprojecttype'),

    # Add employee
    path('addemployee/', add_employee.addemployee, name='addemployee'),

    # Teams
    path('newteam/',new_team_create.create_team, name='create_team'),
    path('team/<int:pk>/',team_details.teams_details, name='teams_details'),
    path('team/<int:team_pk>/<int:project_pk>/', project_details.projects_details, name='project_details'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)