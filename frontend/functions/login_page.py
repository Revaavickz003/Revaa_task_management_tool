from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST['emailaddress']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'tmt-tool/login_page.html', {'error': 'Invalid credentials'})
    
    return render(request, 'tmt-tool/login_page.html')


def logout_view(request):
    logout(request)
    return redirect('login')