from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from frontend.models import EmployeeDetail
from django.urls import reverse

def messages(request):
    userr = EmployeeDetail.objects.all()
    context = {
        'messages': 'active',
        'userr' : userr,
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

def openmessagesection(request, pk):
    messagee = get_object_or_404(EmployeeDetail,pk=pk)
    userr = EmployeeDetail.objects.all()
    print(request.path)
    context = {
        'messages': 'active',
        'messagee': messagee,
        'userr' : userr,
             }
    return render(request, 'tmt-tool/messages.html', context)

