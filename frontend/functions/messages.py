from django.shortcuts import render, redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from frontend.models import *

def messages(request):

    users = EmployeeDetail.objects.all()
    
    context = {
        'messages': 'active',
        "userr" : users,
        'primary_key' : primary_key,
    }
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        file = request.FILES.get('file')

        print(file)
        
        if message:
            print(f"Message: {message}")
        
        if file:
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            print(f"File uploaded: {file}")
            context['uploaded_file_url'] = uploaded_file_url
        
        context['message'] = message
        return render(request, 'tmt-tool/messages.html', context)

    return render(request, 'tmt-tool/messages.html', context)

def update(request,pk):
    primary_key = get_object_or_404(EmployeeDetail, pk=pk)
    context = {
        'primary_key' : primary_key
    }
    return render(request, 'tmt-tool/messages.html', context)