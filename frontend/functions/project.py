from django.shortcuts import render
import datetime

def project(request):
    context = {
        'Project':'active'
    }
    return render(request, 'tmt-tool/project.html', context)

