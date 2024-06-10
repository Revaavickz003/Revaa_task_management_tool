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

    # Add employee
    path('addemployee/', add_employee.addemployee, name='addemployee'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)