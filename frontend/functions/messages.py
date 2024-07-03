from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Q 
from frontend.models import *


def messages(request):
    userr = EmployeeDetail.objects.all()
    # chat_rooms = ChatRoom.objects.filter(members=request.user)
    context = {
        'messages': 'active',
        'userr' : userr,
        # 'chat_rooms' : chat_rooms,
          }
    if request.method == 'POST':
        message_content = request.POST.get('message', '')
        file = request.FILES.get('file')
        room_id = request.POST.get('room_id')
        print(file)
        
        if room_id:
            room = ChatRoom.objects.get(id=room_id)
        else:
            room = ChatRoom.objects.create()
            room.members.add(request.user)
            room.save() 

        if message_content:
            message = Message.objects.create(
                room=room,
                sender=request.user,
                content=message_content,
                receiver=None  # Adjust this as needed
            )
            print(f"Message: {message}")
        
        if file:
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            print(f"File uploaded: {file}")
            context['uploaded_file_url'] = uploaded_file_url
        
        context['message'] = message_content
        return render(request, 'tmt-tool/messages.html', context)

    return render(request, 'tmt-tool/messages.html', context)


from django.shortcuts import render, get_object_or_404
from frontend.models import EmployeeDetail
from django.db.models import Q

def openmessagesection(request, pk):
    messagee = get_object_or_404(EmployeeDetail, pk=pk)
    userr = EmployeeDetail.objects.all()

    # Get or create the chat room between request.user and messagee
    chat_room, created = ChatRoom.objects.get_or_create(id=f"room_{request.user.pk}_{messagee.pk}")
    if created:
        chat_room.members.add(request.user, messagee)

    # Fetch all messages between request.user and messagee
    messages = Message.objects.filter(
        Q(room=chat_room) & 
        (Q(sender=request.user, receiver=messagee) | Q(sender=messagee, receiver=request.user))
    ).order_by('created_at')

    for i in messages:
        print(i)
    context = {
        'messages': 'active',
        'messagee': messagee,
        'userr': userr,
        'messages_list': messages,
    }
    return render(request, 'tmt-tool/messages.html', context)


