# employees/admin.py
from django.contrib import admin
from .models import (
    ProductTable,
    Project, 
    EmployeeDetail, 
    Team, 
    TaskSheet,
    status,
    Type,
    customersTable,
)

admin.site.register(ProductTable)
admin.site.register(Project)
admin.site.register(EmployeeDetail)
admin.site.register(Team)
admin.site.register(TaskSheet)
admin.site.register(status)
admin.site.register(Type)
admin.site.register(customersTable)
