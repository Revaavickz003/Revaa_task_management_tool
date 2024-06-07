from django.shortcuts import render
from frontend.models import EmployeeDetail

def teams(request):
    context = {
        'teams':'active',
        "all_employees": EmployeeDetail.objects.all()
    }
    return render(request, 'tmt-tool/teams.html', context)

