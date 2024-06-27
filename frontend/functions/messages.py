from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def messages(request):
    context = {
        'messages': 'active'
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
    pass