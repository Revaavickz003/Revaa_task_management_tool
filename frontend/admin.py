# employees/admin.py
from django.contrib import admin
from .models import (
    ProductTable,
    ProjectCategories,
    Project, 
    EmployeeDetail, 
    Team, 
    TaskSheet,
    status,
)

admin.site.register(ProductTable)
admin.site.register(ProjectCategories)
admin.site.register(Project)
admin.site.register(EmployeeDetail)
admin.site.register(Team)
admin.site.register(TaskSheet)
admin.site.register(status)
