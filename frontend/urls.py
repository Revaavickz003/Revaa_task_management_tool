from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from frontend.functions import (
    home,
    login_page,
    project,
    messages,
    task_details,
    teams,
    add_employee,
    project_closed_page,
    new_team_create,
    team_details,
    project_details,
    statusdetails,
)

urlpatterns = [

    # Side bar
    path('', home.home, name='home'),
    path('login/', login_page.login_view, name='login'),
    path('home/<str:date>/', home.date_view, name='datehome'),
    path('project/', project.projects_page, name='project'),
    path('get_projects/<int:client_id>/', project.get_projects, name='get_projects'),
    path('messages/', messages.messages, name='messages'),
    path('teams/', teams.teams, name='teams'),
    
    # Open project page
    path('project/closed/<int:pk>/', project.closeproject, name='closeproject'),
    path('project/<int:pk>/', project.singleprojectopen, name='singleprojectopen'),
    path('project/update_project_details/<int:pk>/', project.update_project_details, name='update_project_details'),
    path('project/update_status_details/<int:pk>/', project.update_status_details, name='update_status_details'),
    path('project/team/<str:team>/', project.openprojectteam, name='openprojectteam'),

    # Close project page
    path('project/closed/', project_closed_page.close_projects_page, name='close_projects_page'),
    path('project/closed/<str:team>/', project_closed_page.closeprojectteam, name='closeprojectteam'),
    path('project/reopen/<int:pk>/', project_closed_page.Reopen, name='reopen'),
    
    path('createprojecttype/<int:team_pk>/<int:project_pk>/', task_details.new_type, name='createprojecttype'),

    # Add employee
    path('addemployee/', add_employee.addemployee, name='addemployee'),
    path('team/employee/<int:epk>/',add_employee.showemployee, name='showemployee'),

    # Teams
    path('newteam/',new_team_create.create_team, name='create_team'),
    path('team/<int:pk>/',team_details.teams_details, name='teams_details'),
    path('team/<int:team_pk>/<int:project_pk>/', project_details.projects_details, name='project_details'),
    path('get_project_details/<int:project_id>/', project_details.get_project_details, name='get_project_details'),

    # Status
    path('createprojectstatus/<int:team_pk>/<int:project_pk>/', statusdetails.new_status, name='createprojectstatus'),
    path('team/<int:tpk>project/<int:ppk>/deletestatus/<int:spk>/', statusdetails.delete_status, name='deletestatus'),
    path('team/<int:tpk>project/<int:ppk>/update_status/<int:spk>/', statusdetails.update_status, name='update_status'),
    

    # Task
    path('newtask/<int:team_pk>/<int:project_pk>/', task_details.new_task, name='newtask'),
    path('addtask_teampage/<int:pk>/', team_details.addtask_teampage, name='addtask_teampage'),
    path('team/<int:team_pk>/<int:project_pk>/task/<int:task_pk>/', task_details.taskopen, name='taskopen'),
    path('starttimefortask/<int:teampk>/<int:ppk>/<int:tpk>/', task_details.starttimefortask, name='starttimefortask'),
    path('endtimefortask/<int:teampk>/<int:ppk>/<int:tpk>/', task_details.endtimefortask, name='endtimefortask'),
    path('deletetask/<int:teampk>/<int:ppk>/<int:tpk>/', task_details.deletetask, name='deletetask'),
    path('updatetask/<int:teampk>/<int:ppk>/<int:tpk>/', task_details.updatetask, name='updatetask'),
    path('addcomments/<int:teampk>/<int:ppk>/<int:tpk>/', task_details.task_comments, name='addcomments'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)