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
)

urlpatterns = [

    # Side bar
    path('', home.home, name='home'),
    path('login/', login_page.login_view, name='login'),
    path('home/<str:date>/', home.date_view, name='datehome'),
    path('project/', project.projects_page, name='project'),
    path('messages/', messages.messages, name='messages'),
    path('teams/', teams.teams, name='teams'),

    # Add employee
    path('addemployee/', add_employee.addemployee, name='addemployee'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)