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
    tasktimeing,
    comments,
    events,
)

admin.site.register(ProductTable)
admin.site.register(Project)
admin.site.register(EmployeeDetail)
admin.site.register(Team)
admin.site.register(TaskSheet)
admin.site.register(status)
admin.site.register(Type)
admin.site.register(customersTable)
admin.site.register(tasktimeing)
admin.site.register(comments)
admin.site.register(events)
