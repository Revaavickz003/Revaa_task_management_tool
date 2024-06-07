# employees/admin.py
from django.contrib import admin
from .models import (
    ProductTable,
    ProjectCategories,
    CustomerTable, 
    EmployeeDetail, 
    Team, 
    TaskSheet,
)

admin.site.register(ProductTable)
admin.site.register(ProjectCategories)
admin.site.register(CustomerTable)
admin.site.register(EmployeeDetail)
admin.site.register(Team)
admin.site.register(TaskSheet)
