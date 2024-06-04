# employees/admin.py
from django.contrib import admin
from .models import EmployeeDetail, Team, ClientDetail, TaskSheet

admin.site.register(EmployeeDetail)
admin.site.register(Team)
admin.site.register(ClientDetail)
admin.site.register(TaskSheet)
